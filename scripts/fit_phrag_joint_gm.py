"""Fit A and fluorescence ETR jointly on a Cc basis, with mesophyll conductance (gm) free.

Ported from the October 31, 2026 exploratory surface analysis (research repo,
tmp/surface-analysis-2026-10-31/agent_joint_fit, model M0_joint). Fits the four saturating
leaves with usable fluorescence (P01, P04, P10, P12) on the standard active flashes.

Per leaf:
  J(Q)  = non-rectangular hyperbola (alpha, Jmax, theta)
  A     = min(Ac, Aj) on Cc = Ci - A/gm (Bernacchi 2002 Cc-basis constants, 25 C)
  ETR   = (A + Rd)(4Cc + 8G*) / (Cc - G*) / s
Gaussian likelihood with separate unknown noise for A and ETR, fitted by iteratively
reweighted least squares from 18 starting points.
"""

from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd
from scipy.optimize import least_squares

ROOT = Path(__file__).resolve().parents[1]
FLASHES = ROOT / "outputs/phrag_brownsville_cohort_flashes.csv"
OUTPUT = ROOT / "outputs/phrag_brownsville_joint_gm_fits.csv"

LEAVES = ["P01", "P04", "P10", "P12"]
GSTAR = 37.4
KM = 272.4 * (1 + 210 / 165.8)
NAMES = ["Vcmax", "Jmax", "alpha", "theta", "Rd", "log_gm", "s"]
LOWER = [1, 10, 0.02, 0.0, 0.0, np.log(0.003), 0.2]
UPPER = [800, 600, 0.9, 0.999, 8, np.log(20), 3.0]


def hyperbola(Q, alpha, jmax, theta):
    aq = alpha * Q
    return 2 * aq * jmax / (aq + jmax + np.sqrt(np.maximum((aq + jmax) ** 2 - 4 * theta * aq * jmax, 0)))


def limited_rate(X, Y, Ci, gm, Rd):
    """Net A for one FvCB branch with Cc = Ci - A/gm (the lower root of the quadratic)."""
    b = gm * (Ci + Y) + X - Rd
    c = gm * (Rd * (Ci + Y) - X * (Ci - GSTAR))
    return (b - np.sqrt(np.maximum(b * b + 4 * c, 0))) / 2


def predict(p, Q, Ci):
    vcmax, jmax, alpha, theta, Rd, log_gm, s = p
    gm = np.exp(log_gm)
    J = hyperbola(Q, alpha, jmax, theta)
    A = np.minimum(limited_rate(vcmax, KM, Ci, gm, Rd), limited_rate(J / 4, 2 * GSTAR, Ci, gm, Rd))
    Cc = Ci - A / gm
    etr = (A + Rd) * (4 * Cc + 8 * GSTAR) / np.maximum(Cc - GSTAR, 1e-3) / s
    return A, etr


def starts():
    for vcmax in (40, 120, 300):
        for gm in (0.02, 0.08, 0.5):
            for theta in (0.4, 0.85):
                yield [vcmax, 150, 0.3, theta, 1.0, np.log(gm), 0.8]


def fit(leaf: pd.DataFrame) -> dict:
    Q, Ci, A, E = leaf["Q_level"].values, leaf["gas_Ci"].values, leaf["gas_A"].values, leaf["ETR"].values
    n = len(A)
    best = None
    for x in starts():
        x = np.clip(x, np.array(LOWER) + 1e-9, np.array(UPPER) - 1e-9)
        sigma_a, sigma_e = 0.4, 3.0
        for _ in range(8):
            def residuals(p):
                a, e = predict(p, Q, Ci)
                return np.concatenate([(a - A) / sigma_a, (e - E) / sigma_e])
            x = least_squares(residuals, x, bounds=(LOWER, UPPER), x_scale="jac", max_nfev=3000).x
            a, e = predict(x, Q, Ci)
            new_a, new_e = np.sqrt(np.mean((a - A) ** 2)), np.sqrt(np.mean((e - E) ** 2))
            converged = abs(new_a / sigma_a - 1) < 1e-3 and abs(new_e / sigma_e - 1) < 1e-3
            sigma_a, sigma_e = max(new_a, 1e-4), max(new_e, 1e-4)
            if converged:
                break
        a, e = predict(x, Q, Ci)
        m2ll = n * np.log(np.mean((a - A) ** 2)) + n * np.log(np.mean((e - E) ** 2))
        if best is None or m2ll < best["m2ll"]:
            best = dict(zip(NAMES, x), m2ll=m2ll, rmse_A=np.sqrt(np.mean((a - A) ** 2)),
                        rmse_ETR=np.sqrt(np.mean((e - E) ** 2)), n_flashes=n)
    best["gm"] = np.exp(best.pop("log_gm"))
    return best


def main() -> None:
    flashes = pd.read_csv(FLASHES)
    flashes = flashes.loc[flashes["flash_kind"].eq("active") & flashes["standard_flash"]
                          & ~flashes["overlapping_flash"] & flashes["run_code"].isin(LEAVES)]
    rows = [{"run_code": run, **fit(leaf)} for run, leaf in flashes.groupby("run_code")]
    fits = pd.DataFrame(rows)
    fits.to_csv(OUTPUT, index=False)
    print(fits.round(3).to_string())
    print(OUTPUT)


if __name__ == "__main__":
    main()
