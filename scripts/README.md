# Script index

Run scripts from the repository root with `uv run --frozen python scripts/NAME.py`.
For Bayesian code/posterior summaries add `--extra bayes` to uv. Scripts write to
outputs/ and may overwrite existing results. The directory stays flat because
research scripts import one another by name.

## Supported cohort pipeline

| Script | Role |
| --- | --- |
| reproduce.py | Dry-run/execute orchestration in dependency order |
| analyze_phrag_brownsville_biochemical_limits.py | Shared final-protocol loaders, pulse masks, flash alignment; historical two-run entry point |
| analyze_phrag_brownsville_cohort.py | All 15 runs, metadata/QC, derived tables and diagnostic figures |
| analyze_phrag_brownsville_tier_a.py | Empirical comparisons and order summaries |
| fit_phrag_brownsville_tier_b_plantecophys.R | Conventional R benchmark; run before Python Tier B |
| analyze_phrag_brownsville_tier_b.py | Joint FvCB variants, exploratory variable-J gm |
| analyze_phrag_brownsville_tier_c_bayesian.py | Joint hierarchical model and sensitivity fit |
| summarize_phrag_brownsville_order_standardization.py | Pooled-order posterior comparison |
| plot_phrag_brownsville_capacity_envelopes_literature.py | Capacity envelopes and external comparison |
| plot_phrag_brownsville_npq.py | NPQ across light and Ci |
| analyze_phrag_brownsville_additive_yields.py | Additive fluorescence yields and figures |
| test_phrag_brownsville_npq_zone_difference.py | Statistical analysis, NOT a software test |

## Reproducing the cohort analysis

Install Git LFS and uv; clone and run `git lfs pull`. The sole LFS dependency is
the generated cohort points CSV; the cohort stage can regenerate it from raw logs.
Use Python 3.13.7 and the committed uv lock.

```sh
uv sync --frozen --extra bayes
uv run --frozen --extra bayes python -m unittest discover -s tests -v
uv run --frozen --extra bayes python scripts/release_manifest.py --check
```

Tier B also requires R and `plantecophys` (the original environment used R 4.2.2
and plantecophys 1.4.6; the uv lock does not lock R packages).

The runner prints commands by default. A single selected stage does not rerun
prerequisites automatically.

```sh
uv run --frozen --extra bayes python scripts/reproduce.py
uv run --frozen --extra bayes python scripts/reproduce.py --stage cohort --execute
uv run --frozen --extra bayes python scripts/reproduce.py --stage tier-a --execute
uv run --frozen --extra bayes python scripts/reproduce.py --stage tier-b --execute
uv run --frozen --extra bayes python scripts/reproduce.py --stage fluorescence --execute
uv run --frozen --extra bayes python scripts/reproduce.py --stage posterior-figures --execute
```

The last command uses the saved posterior files. Refit them only intentionally
with `--stage bayes` and `--stage sensitivity`. `--stage all --skip-bayes --execute`
runs the non-sampling sequence. Outputs are overwritten: use a separate clone.
The Bayesian default is four chains, 1,500 tuning iterations, 1,000 draws per chain,
target_accept 0.93, and seeds 20260803 + chain index.

A full non-sampling rerun on October 27, 2026 reproduced 23 of 32 output CSVs at
rtol=1e-7; the other nine differ by small optimizer/rounding amounts (largest
change in modeled A about 0.0006 µmol m⁻² s⁻¹). Some weakly identified parameters
on inactive limiting branches move more (P13 fixed-gm no-TPU Jmax25: 74 vs 155),
so don't treat every converged parameter as identified. The comparison tables are
in [docs/release-audit/](../docs/release-audit/).

## Method development and earlier runs

These entry points preserve the investigation and are not interchangeable with
the final cohort analysis. Source filenames/constants identify their specific inputs.

- analyze_bptest_dynamic_ramp.py
- analyze_h2o_flash_diagnostic.py
- analyze_morella_aqc_surface.py
- analyze_morella_capacities.py
- analyze_morella_outside_regular.py
- analyze_morella_tpu_step_test.py
- analyze_phrag_aq_dark_rerun.py
- analyze_phrag_brownsville_salinity_edge.py
- analyze_phrag_brownsville_upland.py
- analyze_phrag_brownsville_upland_late_repeat.py
- analyze_phrag_bucket_highq.py
- analyze_phrag_crc_fixed_h2or_async.py
- analyze_phrag_crc_indoor_controller_test.py
- analyze_phrag_crc_indoor_vpd_flow600.py
- analyze_phrag_indoor_tpu_controller_test.py
- compare_morella_regular_runs.py
- compare_phrag_brownsville_positions.py
- compare_phrag_brownsville_upland_repeat.py
- fit_morella_photorch.py (requires photorch extra)
- fit_phrag_dat_2021_method.R (requires plantecophys)
- fit_phrag_fvcb_surface.py
- plot_phrag_dat_2021_fit.py
- plot_phrag_qci_surface.py

## Exports

- export_blog_interactives.py: machine-readable plot data for the blog.
- try_xy_photosynthesis.py: plotting experiment; requires xy extra.

## Release tools

- release_manifest.py: standard-library checksum/index writing and verification.
- audit_release_inventory.py: whole local workspace inventory; includes local-only
  material when present. The October 27 audit is a historical snapshot, not the
  public release manifest.
- package_valid_phrag_leaves.py: historical valid-only convenience ZIP. It excludes
  suspect raw files and changes paths; the complete data/ tree is preferred for
  reproduction. This packager is not the whole release.

Software regression tests live in ../tests/, not in scripts/.
