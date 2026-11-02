"""Plot the first Morella A/Q and A/Ci curves (June 15) with their joint FvCB fit, and gsw under each.

The fit is the saved PhoTorch fit from `fit_morella_photorch.py --run june`; this script
re-evaluates it along each curve. Needs the photorch extra.
"""

from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import torch
from photorch import fvcb

from photo26.curves import read_licor_export

ROOT = Path(__file__).resolve().parents[1]
AQ_LOG = ROOT / "data/2026-06-15-1020_logdata_morcer_test1"
ACI_LOG = ROOT / "data/2026-06-15-1053_logdata_morcertest2_Acicurve (1)"
FIT_SUMMARY = ROOT / "outputs/morella_photorch_june_primary_summary.csv"
FIT_PREDICTIONS = ROOT / "outputs/morella_photorch_june_primary_predictions.csv"
FIGURE = ROOT / "outputs/morella_initial_curves.png"


def fvcb_curve(frame: pd.DataFrame, fit: pd.Series) -> np.ndarray:
    """Net A from the saved fit at each (Ci, Qin, Tleaf) row, using the same PhoTorch model settings."""
    # PhoTorch sorts rows by Ci within a curve; one ID per row keeps the input order.
    data = frame.reset_index(drop=True).assign(FittingGroup="Morella", A=0.0)
    data["CurveID"] = data.index + 1
    lcd = fvcb.initLicordata(data, preprocess=False, printout=False)
    model = fvcb.model(lcd, LightResp_type=2, TempResp_type=1, onefit=True, fitRd=False, printout=False)
    with torch.no_grad():
        model.Vcmax25.fill_(fit["Vcmax25"])
        model.Jmax25.fill_(fit["Jmax25"])
        model.TPU25.fill_(fit["TPU25"])
        model.LightResponse.alpha.fill_(fit["alpha_incident"])
        model.LightResponse.theta.fill_(fit["theta"])
        return model()[0].numpy()


def main() -> None:
    aq = read_licor_export(AQ_LOG).sort_values("Qin")
    aci = read_licor_export(ACI_LOG).sort_values("Ci")
    fit = pd.read_csv(FIT_SUMMARY).iloc[0]

    # Check the re-evaluation against the saved fitted values before drawing anything.
    saved = pd.read_csv(FIT_PREDICTIONS)
    check = saved.rename(columns={"Q": "Qin"})[["Ci", "Qin", "Tleaf"]]
    assert np.allclose(fvcb_curve(check, fit), saved["A_model"], atol=1e-6)

    ci = np.linspace(aci["Ci"].min(), aci["Ci"].max(), 300)
    aci_grid = pd.DataFrame({"Ci": ci, "Qin": aci["Qin"].median(), "Tleaf": aci["Tleaf"].median()})
    # Ci drifted during the A/Q, so the fitted line follows the logged Ci between light steps.
    q = np.linspace(0, aq["Qin"].max(), 300)
    aq_grid = pd.DataFrame({"Ci": np.interp(q, aq["Qin"], aq["Ci"]), "Qin": q, "Tleaf": aq["Tleaf"].median()})

    plt.rcParams.update({"font.size": 10, "axes.spines.top": False, "axes.spines.right": False})
    fig, axes = plt.subplots(2, 2, figsize=(8.5, 5.6), sharex="col", constrained_layout=True,
                             gridspec_kw={"height_ratios": [1.4, 1]})
    ink, muted, model_color = "#1f2933", "#7b8794", "#2478a6"
    for column, (frame, grid, x) in enumerate([(aq, aq_grid, "Qin"), (aci, aci_grid, "Ci")]):
        axes[0, column].plot(grid[x], fvcb_curve(grid, fit), color=model_color, lw=1.4, label="FvCB fit")
        axes[0, column].plot(frame[x], frame["A"], color=ink, lw=0, marker="o", ms=4, label="Measured")
        axes[0, column].axhline(0, color=muted, lw=0.8)
        axes[1, column].plot(frame[x], frame["gsw"], color=ink, lw=1.4, marker="o", ms=4)
        # Fixed ranges shared by both curves so the low values read as low.
        axes[0, column].set_ylim(-3, 20)
        axes[1, column].set_ylim(0, 0.2)
    axes[0, 0].legend(frameon=False, loc="upper left")
    axes[0, 1].text(
        0.98, 0.95,
        f"Vcmax25 = {fit['Vcmax25']:.0f}\nJmax25 = {fit['Jmax25']:.0f}\nTPU25 = {fit['TPU25']:.1f}\n"
        f"R² = {fit['r_squared']:.2f}",
        transform=axes[0, 1].transAxes, ha="right", va="top", color=ink,
    )
    axes[0, 0].set_ylabel("A (µmol m⁻² s⁻¹)")
    axes[1, 0].set_ylabel("gsw (mol m⁻² s⁻¹)")
    axes[1, 0].set_xlabel("Q (µmol m⁻² s⁻¹)")
    axes[1, 1].set_xlabel("Ci (ppm)")
    axes[0, 0].set_title("A/Q", loc="left")
    axes[0, 1].set_title("A/Ci", loc="left")
    for ax in axes.flat:
        ax.grid(axis="y", color="#e4e7eb", lw=0.8)
    fig.savefig(FIGURE, dpi=240)
    print(FIGURE)
    print(fit.to_string())


if __name__ == "__main__":
    main()
