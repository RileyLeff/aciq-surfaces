"""Plot apparent Vcmax25 and Jmax25 against gsw for the 12 usable Brownsville leaves, next to Nguyen et al. (2013) haplotype M.

Vcmax25 and Jmax25 are the Ci-basis joint multi-light fit (Tier B, joint_appCi_noTPU). Theta sits at
its lower bound in most leaves, which pushes Jmax up. gsw is the median during ramps at PPFD >= 350.
Nguyen haplotype M: Vcmax 84 +/- 6, Jmax 116 +/- 10 (Table 3, mean +/- SE); gs approximated as
Amax / WUEi = 22.4 / 57.4 (Table 2), a ratio of means.

Right panel: gm sensitivity. The Rubisco-limited A/Ci curve implied by each Ci-basis Vcmax and Rd
(Ci 100-250: Nguyen's Rubisco-limited range, above the compensation point so A > 0) is re-read on a Cc basis, Cc = Ci - A/gm, at an assumed gm
and refit with Bernacchi 2002 Cc-basis constants. Applied the same way to Nguyen haplotype M (their
constants: Kc 406.8, Ko 275.7, G* 28.7, Rd 2.27) and to our saturating leaves (Tier B constants).
The shaded band is the gm range from the joint A + ETR fit (fit_phrag_joint_gm.py).
"""

from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.optimize import least_squares

ROOT = Path(__file__).resolve().parents[1]
FITS = ROOT / "outputs/phrag_brownsville_tier_b_joint_fvcb_fits.csv"
GM_FITS = ROOT / "outputs/phrag_brownsville_joint_gm_fits.csv"
POINTS = ROOT / "outputs/phrag_brownsville_cohort_points.csv"
FIGURE = ROOT / "outputs/phrag_vcmax_vs_gsw.png"
SENSITIVITY = ROOT / "outputs/phrag_vcmax_gm_sensitivity.csv"

SATURATING = ["P01", "P02", "P04", "P10", "P12"]
LINEAR = ["P03", "P06", "P07", "P08", "P11", "P13", "P14"]
NGUYEN = {"Vcmax25": (84.0, 6.0), "Jmax25": (116.0, 10.0)}
NGUYEN_GS = 22.4 / 57.4
NGUYEN_CI_BASIS = (84.0, 2.27, 28.7, 406.8 * (1 + 210 / 275.7))  # Vcmax, Rd, G*, Kc(1 + O/Ko)
TIER_B_CONSTANTS = (42.75, 404.9 * (1 + 210 / 278.4))
CC_GSTAR, CC_KM = 37.4, 272.4 * (1 + 210 / 165.8)
CI_RUBISCO = np.arange(100, 251, 10.0)
ASSUMED_GM = np.geomspace(0.02, 1.0, 40)

INK, MUTED, GRID = "#1f2933", "#7b8794", "#e4e7eb"
COLORS = {"saturating": "#2478a6", "linear": "#d9822b"}
LABEL_SHIFT = {
    "Vcmax25": {"P10": (-0.03, 0), "P08": (-0.006, -2.5), "P11": (0, 1.5)},
    "Jmax25": {},
}
YLIM = {"Vcmax25": 100, "Jmax25": 200}


def cc_basis_vcmax(vcmax, rd, gstar, km, gm):
    """Refit Vcmax on Cc at an assumed gm; NaN if Cc would fall to G*."""
    a = vcmax * (CI_RUBISCO - gstar) / (CI_RUBISCO + km) - rd
    cc = CI_RUBISCO - a / gm
    if np.any(cc <= CC_GSTAR + 1):
        return np.nan
    fit = least_squares(lambda v: v[0] * (cc - CC_GSTAR) / (cc + CC_KM) - rd - a, [vcmax], bounds=([1], [2000]))
    return fit.x[0]


def gm_sensitivity(fits: pd.DataFrame) -> pd.DataFrame:
    sources = {"Nguyen haplotype M": NGUYEN_CI_BASIS}
    for run in SATURATING:
        sources[run] = (fits.loc[run, "Vcmax25"], fits.loc[run, "Rd"], *TIER_B_CONSTANTS)
    rows = [{"source": name, "assumed_gm": gm, "Vcmax25_Cc": cc_basis_vcmax(*params, gm)}
            for name, params in sources.items() for gm in ASSUMED_GM]
    return pd.DataFrame(rows)


def main() -> None:
    fits = pd.read_csv(FITS)
    fits = fits.loc[fits["variant"].eq("joint_appCi_noTPU"), ["run_code", "Vcmax25", "Jmax25", "Rd"]]
    points = pd.read_csv(POINTS, low_memory=False, usecols=["run_code", "Q_level", "is_measured_ramp", "gsw"])
    points = points.loc[points["is_measured_ramp"].astype(bool) & points["Q_level"].ge(350)]
    gsw = points.groupby("run_code")["gsw"].median().rename("gsw")
    fitted_gm = pd.read_csv(GM_FITS)["gm"]
    leaves = fits.set_index("run_code").join(gsw).loc[SATURATING + LINEAR]
    print(leaves.round(3).to_string())

    plt.rcParams.update({"font.size": 10, "axes.spines.top": False, "axes.spines.right": False})
    fig, (vcmax_ax, jmax_ax, sens_ax) = plt.subplots(1, 3, figsize=(15, 4.4), constrained_layout=True)
    for ax, column in [(vcmax_ax, "Vcmax25"), (jmax_ax, "Jmax25")]:
        for name, runs in [("saturating", SATURATING), ("linear", LINEAR)]:
            group = leaves.loc[runs]
            ax.plot(group["gsw"], group[column], "o", color=COLORS[name], ms=6, label=name)
            for run, row in group.iterrows():
                dx, dy = LABEL_SHIFT[column].get(run, (0, 0))
                ax.text(row["gsw"] + 0.006 + dx, row[column] + dy, run, fontsize=7, color=MUTED, va="center")
        value, se = NGUYEN[column]
        ax.errorbar(NGUYEN_GS, value, yerr=se, fmt="s", color=INK, ms=6, capsize=3,
                    label="Nguyen et al. 2013, haplotype M")
        ax.grid(axis="y", color=GRID, lw=0.6)
        ax.set_xlim(0, 0.45)
        ax.set_ylim(0, YLIM[column])
        ax.set_xlabel("gsw (mol m⁻² s⁻¹)")
        ax.set_ylabel(f"{column} (µmol m⁻² s⁻¹)")
    vcmax_ax.legend(frameon=False, loc="lower right")

    sensitivity = gm_sensitivity(leaves)
    sensitivity.to_csv(SENSITIVITY, index=False)
    sens_ax.axvspan(fitted_gm.min(), fitted_gm.max(), color=GRID, lw=0)
    sens_ax.text(np.sqrt(fitted_gm.min() * fitted_gm.max()), 12, "our fitted gm", fontsize=7, color=MUTED, ha="center")
    for name, curve in sensitivity.groupby("source", sort=False):
        nguyen = name.startswith("Nguyen")
        sens_ax.plot(curve["assumed_gm"], curve["Vcmax25_Cc"], color=INK if nguyen else COLORS["saturating"],
                     lw=1.6 if nguyen else 1.0)
        last = curve.dropna().iloc[-1]
        nudge = {"P12": 1.15, "P10": 1.07, "P02": 0.92, "P01": 0.83}.get(name, 1)
        sens_ax.text(last["assumed_gm"] * 1.06, last["Vcmax25_Cc"] * nudge, "Nguyen M" if nguyen else name,
                     fontsize=7, color=MUTED, va="center")
    sens_ax.set_xscale("log")
    sens_ax.set_xticks([0.02, 0.05, 0.1, 0.2, 0.5, 1.0], ["0.02", "0.05", "0.1", "0.2", "0.5", "1"])
    sens_ax.set_yscale("log")
    sens_ax.set_yticks([10, 20, 50, 100, 200, 500, 1000], ["10", "20", "50", "100", "200", "500", "1000"])
    sens_ax.minorticks_off()
    sens_ax.set_ylim(10, 1000)
    sens_ax.grid(axis="y", color=GRID, lw=0.6)
    sens_ax.set_xlabel("Assumed gm (mol m⁻² s⁻¹)")
    sens_ax.set_ylabel("Vcmax25, Cc basis (µmol m⁻² s⁻¹)")
    print(sensitivity.pivot(index="assumed_gm", columns="source", values="Vcmax25_Cc").iloc[::6].round(1).to_string())
    fig.savefig(FIGURE, dpi=220)
    print(FIGURE)


if __name__ == "__main__":
    main()
