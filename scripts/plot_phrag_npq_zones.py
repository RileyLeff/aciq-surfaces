"""Plot NPQ by elevation zone for the seven sun leaves with usable fluorescence.

Writes two figures:
- NPQ and ETR against light at a common Ci of 800, per leaf and zone median.
- Per-leaf mean NPQ (flashes at Ci >= 350) by zone, marked by A/Ci shape group.

Sun leaves only, matching plot_phrag_brownsville_npq.py and test_phrag_brownsville_npq_zone_difference.py:
the shade pilot leaves (P01, P04, P07, P08) are all High, and P02's flashes overlapped.
"""

from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
COMMON = ROOT / "outputs/phrag_brownsville_cohort_fluorescence_at_common_ci.csv"
LEAF_MEANS = ROOT / "outputs/phrag_brownsville_npq_overall_leaf_means.csv"
LIGHT_FIGURE = ROOT / "outputs/phrag_npq_zones_light.png"
LEAF_FIGURE = ROOT / "outputs/phrag_npq_zones_leaves.png"

ZONES = {"Low": ["P03", "P06", "P10", "P11"], "High": ["P12", "P13", "P14"]}
SATURATING = ["P01", "P02", "P04", "P10", "P12"]

INK, MUTED, GRID = "#1f2933", "#7b8794", "#e4e7eb"
COLORS = {"Low": "#7a4fa3", "High": "#2f8f6f"}
LABELS = {"Low": "Low elevation", "High": "High elevation"}
LABEL_SHIFT = {"P03": 0.04, "P10": -0.04, "P13": 0.03, "P14": -0.03}


def plot_light() -> None:
    common = pd.read_csv(COMMON)
    fig, axes = plt.subplots(1, 2, figsize=(10, 4), constrained_layout=True)
    for ax, column, ylabel in [(axes[0], "NPQ_at_Ci800", "NPQ"), (axes[1], "ETR_at_Ci800", "ETR (µmol m⁻² s⁻¹)")]:
        for zone, runs in ZONES.items():
            leaves = common.loc[common["run_code"].isin(runs)]
            for run, leaf in leaves.groupby("run_code"):
                ax.plot(leaf["Q_level"], leaf[column], color=COLORS[zone], lw=0.8, alpha=0.4)
            median = leaves.groupby("Q_level")[column].median()
            ax.plot(median.index, median, color=COLORS[zone], lw=2, marker="o", ms=4, label=LABELS[zone])
        ax.grid(axis="y", color=GRID, lw=0.6)
        ax.set_xlim(0, 2100)
        ax.set_ylim(0, None)
        ax.set_xlabel("PPFD (µmol m⁻² s⁻¹)")
        ax.set_ylabel(f"{ylabel} at Ci 800")
    axes[0].legend(frameon=False, loc="upper left")
    fig.savefig(LIGHT_FIGURE, dpi=220)
    print(LIGHT_FIGURE)


def plot_leaves() -> None:
    means = pd.read_csv(LEAF_MEANS).set_index("run_code")
    print(means.round(3).to_string())
    fig, ax = plt.subplots(figsize=(4.2, 3.8), constrained_layout=True)
    for x, (zone, runs) in enumerate(ZONES.items()):
        for run in runs:
            saturating = run in SATURATING
            ax.plot(x, means.loc[run, "NPQ"], "o", color=COLORS[zone], ms=7,
                    mfc=COLORS[zone] if saturating else "white", mew=1.4)
            ax.text(x + 0.08, means.loc[run, "NPQ"] + LABEL_SHIFT.get(run, 0), run, fontsize=7, color=MUTED, va="center")
        ax.plot([x - 0.22, x - 0.04], [means.loc[runs, "NPQ"].mean()] * 2, color=INK, lw=1.2)
    ax.plot([], [], "o", color=MUTED, ms=6, label="saturating")
    ax.plot([], [], "o", color=MUTED, mfc="white", mew=1.4, ms=6, label="linear")
    ax.legend(frameon=False, loc="upper right")
    ax.set_xticks(range(len(ZONES)), [LABELS[zone] for zone in ZONES])
    ax.set_xlim(-0.5, 1.6)
    ax.set_ylim(0, 2.5)
    ax.grid(axis="y", color=GRID, lw=0.6)
    ax.set_ylabel("Mean NPQ per leaf (Ci ≥ 350)")
    fig.savefig(LEAF_FIGURE, dpi=220)
    print(LEAF_FIGURE)


def main() -> None:
    plt.rcParams.update({"font.size": 10, "axes.spines.top": False, "axes.spines.right": False})
    plot_light()
    plot_leaves()


if __name__ == "__main__":
    main()
