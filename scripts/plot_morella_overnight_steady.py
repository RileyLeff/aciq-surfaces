"""Plot the June 22 overnight Morella log at 420 ppm, up to when the CO2 cartridge ran out."""

from __future__ import annotations

from pathlib import Path

import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
LOG = ROOT / "data/2026-06-22-1756_logdata_morcer_indoor_overnight"
FIGURE = ROOT / "outputs/morella_overnight_steady.png"
SUMMARY = ROOT / "outputs/morella_overnight_steady_summary.csv"


def load_log(path: Path) -> pd.DataFrame:
    lines = path.read_text(encoding="utf-8", errors="replace").splitlines()
    start = next(i for i, line in enumerate(lines) if line.startswith("[Data]"))
    header = lines[start + 2].split("\t")
    rows = [line.split("\t") for line in lines[start + 4:] if len(line.split("\t")) == len(header)]
    frame = pd.DataFrame(rows, columns=header)
    frame = frame.loc[:, ~frame.columns.duplicated()]
    for column in ["elapsed", "CO2_r", "Ci", "A", "gsw", "Qin", "Tleaf", "VPDleaf"]:
        frame[column] = pd.to_numeric(frame[column], errors="coerce")
    # The June row `date` field runs one day ahead of the header's "File opened"; trust the header.
    opened = next(line.split("\t")[1] for line in lines[:start] if line.startswith("File opened"))
    first = pd.Timestamp(f"{opened[:10]} {frame['hhmmss'].iloc[0]}")
    frame["time"] = first + pd.to_timedelta(frame["elapsed"], unit="s")
    return frame


def main() -> None:
    frame = load_log(LOG)
    # The reference CO2 left its 420 setpoint when the cartridge emptied; stop there.
    ran_out = frame.loc[frame["CO2_r"].lt(400), "time"].iloc[0]
    frame = frame.loc[frame["time"].lt(ran_out)]
    settled = frame.loc[frame["elapsed"].ge(3600)]
    summary = pd.DataFrame(
        [
            {"period": name, "start": part["time"].min(), "end": part["time"].max(),
             "hours": (part["time"].max() - part["time"].min()).total_seconds() / 3600,
             "CO2_r_median": part["CO2_r"].median(), "Qin_median": part["Qin"].median(),
             "Tleaf_median": part["Tleaf"].median(), "VPDleaf_median": part["VPDleaf"].median(),
             "VPDleaf_min": part["VPDleaf"].min(), "VPDleaf_max": part["VPDleaf"].max(),
             "A_median": part["A"].median(), "A_start": part["A"].iloc[0],
             "A_end": part["A"].iloc[-1], "gsw_median": part["gsw"].median(),
             "gsw_sd": part["gsw"].std()}
            for name, part in [("whole run at 420", frame), ("after first hour", settled)]
        ]
    )
    summary.to_csv(SUMMARY, index=False)

    plt.rcParams.update({"font.size": 10, "axes.spines.top": False, "axes.spines.right": False})
    fig, axes = plt.subplots(6, 1, figsize=(7.5, 9.6), sharex=True, constrained_layout=True,
                             gridspec_kw={"height_ratios": [1.2, 1, 1, 0.6, 0.6, 0.6]})
    ink, muted = "#1f2933", "#7b8794"
    axes[0].plot(frame["time"], frame["CO2_r"], color=ink, lw=1.6, label="Reference CO₂")
    axes[0].plot(frame["time"], frame["Ci"], color="#2478a6", lw=1.2, label="Ci")
    axes[0].set_ylabel("CO₂ (ppm)")
    axes[0].set_ylim(0, 520)
    axes[0].legend(frameon=False, loc="lower right", ncol=2)
    axes[1].plot(frame["time"], frame["gsw"], color=ink, lw=1.4)
    axes[1].set_ylabel("gsw (mol m⁻² s⁻¹)")
    axes[1].set_ylim(0, None)
    axes[2].plot(frame["time"], frame["A"], color=ink, lw=1.4)
    axes[2].axhline(0, color=muted, lw=0.8)
    axes[2].set_ylabel("A (µmol m⁻² s⁻¹)")
    # Fixed, generous ranges so instrument noise doesn't read as drift.
    axes[3].plot(frame["time"], frame["VPDleaf"], color=ink, lw=1.2)
    axes[3].set_ylabel("VPD (kPa)")
    axes[3].set_ylim(0, 2)
    axes[4].plot(frame["time"], frame["Tleaf"], color=ink, lw=1.2)
    axes[4].set_ylabel("Tleaf (°C)")
    axes[4].set_ylim(20, 30)
    axes[5].plot(frame["time"], frame["Qin"], color=ink, lw=1.2)
    axes[5].set_ylabel("Q\n(µmol m⁻² s⁻¹)")
    axes[5].set_ylim(0, 1000)
    for ax in axes:
        ax.grid(axis="y", color="#e4e7eb", lw=0.8)
    axes[5].xaxis.set_major_formatter(mdates.DateFormatter("%H:%M"))
    axes[5].set_xlabel("Clock time, June 22–23")
    fig.savefig(FIGURE, dpi=240)
    print(FIGURE)
    print(summary.to_string(index=False))


if __name__ == "__main__":
    main()
