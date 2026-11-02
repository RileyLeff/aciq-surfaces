"""Plot the July 9 upland Brownsville leaf: first ascending-light run vs the identical schedule repeated right after.

Left: A/Ci at PPFD 200, median A in 100 ppm Ci bins (bins with >= 3 points), as in
compare_phrag_brownsville_upland_repeat.py. Right: 95th percentile A per light block from the saved summary.
"""

from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
RUNS = {
    "first run (15:59–18:15)": ROOT / "outputs/phrag_brownsville_upland_points.csv",
    "repeat (18:49–21:04)": ROOT / "outputs/phrag_brownsville_upland_late_repeat_points.csv",
}
SUMMARY = ROOT / "outputs/phrag_brownsville_upland_repeat_summary.csv"
FIGURE = ROOT / "outputs/phrag_upland_test_retest.png"
ACI_LIGHT = 200.0
BIN = 100

INK, MUTED, GRID = "#1f2933", "#7b8794", "#e4e7eb"
COLORS = dict(zip(RUNS, ["#9aa5b1", INK]))


def binned_aci(path: Path) -> pd.DataFrame:
    points = pd.read_csv(path, low_memory=False)
    points = points.loc[points["sane_for_curve"].astype(bool) & points["Q_level"].eq(ACI_LIGHT)
                        & points["Ci"].between(0, 1800)].copy()
    points["Ci_center"] = np.floor(points["Ci"] / BIN) * BIN + BIN / 2
    curve = points.groupby("Ci_center").agg(A=("A", "median"), n=("A", "size")).reset_index()
    return curve.loc[curve["n"].ge(3)]


def main() -> None:
    summary = pd.read_csv(SUMMARY)
    plt.rcParams.update({"font.size": 10, "axes.spines.top": False, "axes.spines.right": False})
    fig, (aci_ax, light_ax) = plt.subplots(1, 2, figsize=(10, 4), constrained_layout=True)
    for (label, path), position in zip(RUNS.items(), ["First run", "Late repeat"]):
        curve = binned_aci(path)
        aci_ax.plot(curve["Ci_center"], curve["A"], color=COLORS[label], lw=1.8, marker="o", ms=3, label=label)
        blocks = summary.loc[summary["position"].eq(position)]
        light_ax.plot(blocks["Q_level"], blocks["A_p95"], color=COLORS[label], lw=1.8, marker="o", ms=4, label=label)
    print(summary.pivot(index="Q_level", columns="position", values=["A_p95", "gsw_median"]).round(3).to_string())

    aci_ax.set_xlim(0, 1900)
    aci_ax.set_ylim(0, None)
    aci_ax.set_xlabel("Ci (µmol mol⁻¹)")
    aci_ax.set_ylabel(f"A at PPFD {ACI_LIGHT:.0f} (µmol m⁻² s⁻¹)")
    aci_ax.legend(frameon=False, loc="upper left")
    light_ax.set_xlim(0, 2100)
    light_ax.set_ylim(0, None)
    light_ax.set_xlabel("PPFD (µmol m⁻² s⁻¹)")
    light_ax.set_ylabel("95th percentile A per light block (µmol m⁻² s⁻¹)")
    for ax in (aci_ax, light_ax):
        ax.grid(axis="y", color=GRID, lw=0.6)
    fig.savefig(FIGURE, dpi=220)
    print(FIGURE)


if __name__ == "__main__":
    main()
