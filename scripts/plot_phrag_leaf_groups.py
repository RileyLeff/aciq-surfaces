"""Plot the saturating vs linear A/Ci split in the Brownsville cohort.

Writes three figures:
- A/Ci at one light for all 12 usable leaves, colored by group.
- gsw per leaf at PPFD >= 350, colored by group.
- Electrons per CO2, ETR / (A + Rd), at the two highest-Ci flashes of each ramp vs light.
  Rd = 1 is assumed and the LI-6800 default ETR scaling is used. P02 is left out because its
  flashes overlapped.

Groups follow the October 31 surface notes in the research repo.
"""

from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
CURVES = ROOT / "outputs/phrag_brownsville_cohort_binned_curves.csv"
POINTS = ROOT / "outputs/phrag_brownsville_cohort_points.csv"
FLASHES = ROOT / "outputs/phrag_brownsville_cohort_flashes.csv"
ACI_FIGURE = ROOT / "outputs/phrag_leaf_groups_aci.png"
GSW_FIGURE = ROOT / "outputs/phrag_leaf_groups_gsw.png"
ELECTRONS_FIGURE = ROOT / "outputs/phrag_leaf_groups_electrons.png"

SATURATING = ["P01", "P02", "P04", "P10", "P12"]
LINEAR = ["P03", "P06", "P07", "P08", "P11", "P13", "P14"]
ACI_LIGHT = 1000.0  # mid-run; light steps go up through the day, so 2000 is the last ramp
RD = 1.0

INK, MUTED, GRID = "#1f2933", "#7b8794", "#e4e7eb"
COLORS = {"saturating": "#2478a6", "linear": "#d9822b"}


def group(run: str) -> str:
    return "saturating" if run in SATURATING else "linear"


def legend(ax, loc: str) -> None:
    for name, color in COLORS.items():
        ax.plot([], [], color=color, lw=1.4, marker="o", ms=3, label=name)
    ax.legend(frameon=False, loc=loc)


def plot_aci() -> None:
    curves = pd.read_csv(CURVES)
    curves = curves.loc[curves["Q_level"].eq(ACI_LIGHT) & curves["run_code"].isin(SATURATING + LINEAR)]
    fig, ax = plt.subplots(figsize=(6, 4.2), constrained_layout=True)
    for run, curve in curves.groupby("run_code"):
        ax.plot(curve["Ci"], curve["A"], color=COLORS[group(run)], lw=1.2)
        last = curve.iloc[-1]
        ax.text(last["Ci"] + 20, last["A"], run, fontsize=7, color=MUTED, va="center")
    ax.axhline(0, color=MUTED, lw=0.6)
    ax.grid(axis="y", color=GRID, lw=0.6)
    ax.set_xlim(0, 1900)
    ax.set_xlabel("Ci (µmol mol⁻¹)")
    ax.set_ylabel("A (µmol m⁻² s⁻¹)")
    legend(ax, "upper left")
    fig.savefig(ACI_FIGURE, dpi=220)
    print(ACI_FIGURE)


def plot_gsw() -> None:
    points = pd.read_csv(POINTS, low_memory=False, usecols=["run_code", "Q_level", "is_measured_ramp", "gsw"])
    points = points.loc[points["is_measured_ramp"].astype(bool) & points["Q_level"].ge(350)
                        & points["run_code"].isin(SATURATING + LINEAR)]
    leaves = points.groupby("run_code")["gsw"].quantile([0.25, 0.5, 0.75]).unstack()
    leaves = leaves.sort_values(0.5)
    print(leaves.round(3).to_string())
    fig, ax = plt.subplots(figsize=(6, 3.6), constrained_layout=True)
    for y, (run, row) in enumerate(leaves.iterrows()):
        color = COLORS[group(run)]
        ax.plot([row[0.25], row[0.75]], [y, y], color=color, lw=1.4)
        ax.plot(row[0.5], y, "o", color=color, ms=5)
    ax.set_yticks(range(len(leaves)), leaves.index)
    ax.grid(axis="x", color=GRID, lw=0.6)
    ax.set_xlim(0, 0.3)
    ax.set_xlabel("gsw at PPFD ≥ 350 (mol m⁻² s⁻¹), median and interquartile range")
    legend(ax, "lower right")
    fig.savefig(GSW_FIGURE, dpi=220)
    print(GSW_FIGURE)


def plot_electrons() -> None:
    flashes = pd.read_csv(FLASHES)
    flashes = flashes.loc[flashes["flash_kind"].eq("active") & flashes["standard_flash"]
                          & ~flashes["overlapping_flash"] & flashes["run_code"].isin(SATURATING + LINEAR)
                          & flashes["run_code"].ne("P02")].copy()
    # The two highest-Ci flashes in each ramp (about 1100-1600 ppm).
    flashes["step"] = flashes.groupby(["run_code", "Q_level"])["gas_Ci"].rank(ascending=False, method="first")
    high = flashes.loc[flashes["step"].le(2)].copy()
    high["electrons"] = high["ETR"] / (high["gas_A"] + RD)
    by_light = high.groupby(["run_code", "Q_level"])["electrons"].mean().reset_index()
    print(high.groupby("run_code")["gas_Ci"].agg(["min", "max"]).round(0).to_string())
    print(by_light.groupby("run_code")["electrons"].agg(["min", "max"]).round(1).to_string())

    fig, ax = plt.subplots(figsize=(6, 4.2), constrained_layout=True)
    ax.axhspan(4.3, 4.5, color=GRID, lw=0)
    ax.text(600, 4.2, "expected, about 4.3–4.5", fontsize=7, color=MUTED, va="center")
    for run, leaf in by_light.groupby("run_code"):
        ax.plot(leaf["Q_level"], leaf["electrons"], color=COLORS[group(run)], lw=1.2, marker="o", ms=3)
        last = leaf.iloc[-1]
        nudge = {"P08": 1.03, "P11": 0.97}.get(run, 1)
        ax.text(last["Q_level"] * 1.05, last["electrons"] * nudge, run, fontsize=7, color=MUTED, va="center")
    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.set_xticks([50, 100, 200, 350, 600, 1000, 2000], ["50", "100", "200", "350", "600", "1000", "2000"])
    ax.set_yticks([4, 5, 6, 8, 10, 15, 20], ["4", "5", "6", "8", "10", "15", "20"])
    ax.minorticks_off()
    ax.grid(axis="y", color=GRID, lw=0.6)
    ax.set_xlabel("PPFD (µmol m⁻² s⁻¹)")
    ax.set_ylabel("ETR / (A + Rd), electrons per CO₂")
    legend(ax, "upper left")
    fig.savefig(ELECTRONS_FIGURE, dpi=220)
    print(ELECTRONS_FIGURE)


def main() -> None:
    plt.rcParams.update({"font.size": 10, "axes.spines.top": False, "axes.spines.right": False})
    plot_aci()
    plot_gsw()
    plot_electrons()


if __name__ == "__main__":
    main()
