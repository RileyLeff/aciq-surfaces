"""Plot the June 22 indoor Morella test: more blue light at 420 ppm, then 275 and 125 ppm, then back to 420."""

from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt

from photo26.curves import read_licor_export

ROOT = Path(__file__).resolve().parents[1]
LOG = ROOT / "data/2026-06-22-1405_logdata_morcer_afternoon_bluelight_indoors"
FIGURE = ROOT / "outputs/morella_low_co2_blue.png"


def main() -> None:
    frame = read_licor_export(LOG).sort_values("elapsed").reset_index(drop=True).copy()
    frame["minute"] = frame["elapsed"] / 60
    # A treatment step is a jump in reference CO2 or blue light between logged points.
    steps = frame.loc[frame["CO2_r"].diff().abs().gt(20) | frame["Q_blue"].diff().abs().gt(20), "minute"]

    plt.rcParams.update({"font.size": 10, "axes.spines.top": False, "axes.spines.right": False})
    fig, axes = plt.subplots(6, 1, figsize=(7.5, 9.6), sharex=True, constrained_layout=True,
                             gridspec_kw={"height_ratios": [1.2, 1, 1.2, 1, 0.6, 0.6]})
    ink, muted = "#1f2933", "#7b8794"
    axes[0].plot(frame["minute"], frame["CO2_r"], color=ink, lw=1.6, label="Reference CO₂")
    axes[0].plot(frame["minute"], frame["Ci"], color="#2478a6", lw=1.2, label="Ci")
    axes[0].set_ylabel("CO₂ (ppm)")
    axes[0].set_ylim(0, 520)
    axes[0].legend(frameon=False, loc="lower left", ncol=2)
    axes[1].plot(frame["minute"], frame["Q_red"], color="#c0392b", lw=1.4, label="Red")
    axes[1].plot(frame["minute"], frame["Q_blue"], color="#3b5bdb", lw=1.4, label="Blue")
    axes[1].set_ylabel("Q\n(µmol m⁻² s⁻¹)")
    axes[1].set_ylim(0, 1000)
    axes[1].legend(frameon=False, loc="upper right", ncol=2)
    axes[2].plot(frame["minute"], frame["gsw"], color=ink, lw=1.4)
    axes[2].set_ylabel("gsw (mol m⁻² s⁻¹)")
    axes[2].set_ylim(0, 0.2)
    axes[3].plot(frame["minute"], frame["A"], color=ink, lw=1.4)
    axes[3].axhline(0, color=muted, lw=0.8)
    axes[3].set_ylabel("A (µmol m⁻² s⁻¹)")
    axes[3].set_ylim(-1, 12)
    axes[4].plot(frame["minute"], frame["VPDleaf"], color=ink, lw=1.2)
    axes[4].set_ylabel("VPD (kPa)")
    axes[4].set_ylim(0, 2)
    axes[5].plot(frame["minute"], frame["Tleaf"], color=ink, lw=1.2)
    axes[5].set_ylabel("Tleaf (°C)")
    axes[5].set_ylim(20, 30)
    for ax in axes:
        ax.grid(axis="y", color="#e4e7eb", lw=0.8)
        for minute in steps:
            ax.axvline(minute, color=muted, lw=0.8, ls="--", zorder=0)
    axes[5].set_xlabel("Minutes since start, June 22 (14:05)")
    fig.savefig(FIGURE, dpi=240)
    print(FIGURE)
    print("steps (min):", [round(m, 1) for m in steps])


if __name__ == "__main__":
    main()
