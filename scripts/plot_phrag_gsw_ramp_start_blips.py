"""Plot raw gsw at the start of every Brownsville cohort ramp: one row per leaf, one column per light level.

Also writes, per ramp, the gsw low and high points near the ramp start and the
instrument channels logged at those rows.
"""

from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
POINTS = ROOT / "outputs/phrag_brownsville_cohort_points.csv"
FIGURE = ROOT / "outputs/phrag_gsw_ramp_start_blips.png"
SUMMARY = ROOT / "outputs/phrag_gsw_ramp_start_blips_summary.csv"
WINDOW_MINUTES = 3.0


def main() -> None:
    points = pd.read_csv(POINTS, low_memory=False)
    ramps = points.loc[points["is_measured_ramp"].astype(bool) & points["phase_minute"].le(WINDOW_MINUTES)]
    runs = sorted(ramps["run_code"].unique())
    levels = sorted(ramps["Q_level"].unique())

    rows = []
    for (run, level), ramp in ramps.groupby(["run_code", "Q_level"]):
        start = ramp.loc[ramp["phase_minute"].le(1)]
        low, high = start.loc[start["gsw"].idxmin()], start.loc[start["gsw"].idxmax()]
        rows.append({
            "run_code": run, "Q_level": level,
            "gsw_settled": ramp.loc[ramp["phase_minute"].between(1, WINDOW_MINUTES), "gsw"].median(),
            "low_seconds": low["phase_minute"] * 60, "low_gsw": low["gsw"], "low_Flow_s": low["Flow_s"],
            "high_seconds": high["phase_minute"] * 60, "high_gsw": high["gsw"], "high_dHs_dt": high["dHs/dt"],
            "high_CO2_r": high["CO2_r"],
        })
    summary = pd.DataFrame(rows)
    summary.to_csv(SUMMARY, index=False)

    plt.rcParams.update({"font.size": 8, "axes.spines.top": False, "axes.spines.right": False})
    fig, axes = plt.subplots(len(runs), len(levels), figsize=(12, 1.05 * len(runs) + 0.6),
                             sharex=True, sharey=True, constrained_layout=True)
    ink = "#1f2933"
    for i, run in enumerate(runs):
        for j, level in enumerate(levels):
            ax = axes[i, j]
            ramp = ramps.loc[ramps["run_code"].eq(run) & ramps["Q_level"].eq(level)]
            ax.plot(ramp["phase_minute"], ramp["gsw"], color=ink, lw=0.8, marker="o", ms=1.6)
            ax.grid(axis="y", color="#e4e7eb", lw=0.6)
            if i == 0:
                ax.set_title(f"Q {level:.0f}", fontsize=9)
            if j == 0:
                ax.set_ylabel(run, rotation=0, ha="right", va="center", fontsize=9)
    axes[0, 0].set_ylim(0, 0.6)
    axes[0, 0].set_xlim(0, WINDOW_MINUTES)
    fig.supxlabel("Minutes into ramp")
    fig.supylabel("gsw (mol m⁻² s⁻¹)")
    fig.savefig(FIGURE, dpi=200)
    print(FIGURE)
    print(summary[["low_seconds", "low_gsw", "low_Flow_s", "high_seconds", "high_gsw", "gsw_settled"]]
          .describe().round(3).to_string())


if __name__ == "__main__":
    main()
