"""Plot a few Brownsville ramp-start gsw blips next to the instrument channels logged at the same rows."""

from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
POINTS = ROOT / "outputs/phrag_brownsville_cohort_points.csv"
FIGURE = ROOT / "outputs/phrag_gsw_blip_channels.png"
EXAMPLES = [("P10", 100.0), ("P01", 1000.0), ("P12", 350.0)]
WINDOW_SECONDS = 60


def main() -> None:
    points = pd.read_csv(POINTS, low_memory=False)
    points = points.loc[points["is_measured_ramp"].astype(bool)].copy()

    plt.rcParams.update({"font.size": 9, "axes.spines.top": False, "axes.spines.right": False})
    fig, axes = plt.subplots(4, len(EXAMPLES), figsize=(10, 7.5), sharex=True, sharey="row",
                             constrained_layout=True)
    ink, muted, accent = "#1f2933", "#7b8794", "#c0392b"
    for column, (run, level) in enumerate(EXAMPLES):
        ramp = points.loc[points["run_code"].eq(run) & points["Q_level"].eq(level)]
        ramp = ramp.assign(second=ramp["phase_minute"] * 60)
        ramp = ramp.loc[ramp["second"].le(WINDOW_SECONDS)]
        spike = ramp.loc[ramp["gsw"].idxmax(), "second"]
        # Nothing is logged between the pre-ramp row and the ramp start; don't draw a line across it.
        gaps = ramp.loc[ramp["second"].diff().gt(5), ["second"]] - 0.01
        ramp = pd.concat([ramp, gaps]).sort_values("second")
        ax = axes[:, column]
        ax[0].plot(ramp["second"], ramp["gsw"], color=ink, lw=1.2, marker="o", ms=2.5)
        ax[1].plot(ramp["second"], ramp["dHs/dt"], color=ink, lw=1.2, marker="o", ms=2.5)
        ax[2].plot(ramp["second"], ramp["H2O_s"], color=ink, lw=1.2, marker="o", ms=2.5, label="Sample")
        ax[2].plot(ramp["second"], ramp["H2O_r"], color=muted, lw=1.2, marker="o", ms=2.5, label="Reference")
        ax[3].plot(ramp["second"], ramp["CO2_r"], color=ink, lw=1.2, marker="o", ms=2.5)
        for a in ax:
            a.axvline(spike, color=accent, lw=0.8, ls="--", zorder=0)
            a.grid(axis="y", color="#e4e7eb", lw=0.6)
        ax[0].set_title(f"{run}, Q {level:.0f}", loc="left")
    axes[0, 0].set_ylabel("gsw\n(mol m⁻² s⁻¹)")
    axes[1, 0].set_ylabel("dHs/dt\n(mmol mol⁻¹ s⁻¹)")
    axes[2, 0].set_ylabel("H₂O\n(mmol mol⁻¹)")
    axes[3, 0].set_ylabel("Reference CO₂\n(ppm)")
    axes[2, 0].legend(frameon=False, loc="lower right")
    axes[3, 0].set_xlim(0, WINDOW_SECONDS)
    fig.supxlabel("Seconds into ramp")
    fig.savefig(FIGURE, dpi=220)
    print(FIGURE)


if __name__ == "__main__":
    main()
