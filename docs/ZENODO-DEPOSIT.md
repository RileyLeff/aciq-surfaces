# Zenodo deposit draft

Upload preparation for the existing Zenodo draft, DOI 10.5281/zenodo.23785367.
Reservation is not publication; use this draft rather than creating another record.

## Record fields

- **Title:** A/Ci/Q Surfaces: LI-6800 programs, coastal photosynthesis data, and analyses
- **Resource type:** Dataset
- **Creators, in order:** Riley Leff; Acadia Conboy; Keryn Gedan
- **Affiliations:** Riley Leff and Keryn Gedan: George Washington University; Acadia Conboy: James Madison University (as listed on the published protocol).
- **Access:** Open
- **Licenses:** CC BY 4.0 for research data, original figures, and documentation; MIT for source code. Preserve this scope in the record description and included license files.
- **Keywords:** photosynthesis; stomatal conductance; chlorophyll fluorescence; LI-6800; dynamic assimilation; Phragmites australis; Morella cerifera; coastal forest; salinity gradient
- **Language:** English
- **Version:** 1.0.0
- **Publication date:** Actual publication date.
- **Funding acknowledgement:** Open release supported by the Astera Institute Hidden Science Competition. Add grant identifiers only if confirmed.

Add ORCIDs only if confirmed; do not infer identifiers from names.

## Description

If a leaf isn't photosynthesizing, how can we tell if it's incapable or unwilling?
We used low CO2 to encourage stomatal opening, then measured gas exchange and
chlorophyll fluorescence across CO2 ramps at multiple light levels. This
deposit preserves the instrument programs, raw measurements, metadata, analysis
code, processed data, and figures from that work at Brownsville Preserve on the
Eastern Shore of Virginia.

The archive includes Morella cerifera and Phragmites australis method-development
experiments and a final 15-run Phragmites cohort spanning higher-elevation,
lower-salinity habitat and lower-elevation, higher-salinity habitat. Twelve runs
were retained for some analyses, containing 62,326 raw gas-exchange observations
and 668 flash JSON records. Excluded runs are included with their QC records.

The README is the technical report. The data guide maps files to samples, and
scripts/README.md explains how to run the analyses.
Research data, original figures, and documentation are CC BY 4.0; source code
is MIT-licensed.

The operating protocol is published at
https://doi.org/10.17504/protocols.io.92ld3bnong5b/v1.

## Related works

- Maintained repository: https://github.com/RileyLeff/aciq-surfaces
- Narrative article: https://rileyleff.com/blog/forcing-plants-to-participate
- Protocol: https://doi.org/10.17504/protocols.io.92ld3bnong5b/v1 (relation: Is documented by; identifier type: DOI).

## Upload and publication

1. Build the local package with `uv run --frozen python scripts/prepare_zenodo.py --destination /absolute/path/to/new-upload-folder`.
2. Read the generated `README.txt`, technical report, and `deposit-fields.md`.
3. Open the existing Zenodo draft for 10.5281/zenodo.23785367. Do not create a new record.
4. Confirm both DOI cross-links and version 1.0.0. The archive manifest records
   the base commit and exact file hashes, including local documentation additions.
5. Upload the ZIP, `README.txt`, `TECHNICAL-REPORT.pdf`, and `SHA256SUMS.txt`.
   `deposit-fields.md` is a form-filling aid, not an upload artifact.
6. Review author details, licenses, links, and files before publishing. No upload
   or publication is performed by the packaging script.

Zenodo instructions: https://help.zenodo.org/docs/deposit/create-new-upload/
File guidance: https://help.zenodo.org/docs/deposit/manage-files/

## Editing the report

Edit `README.md` (the technical report), then run from the repository root:

```sh
uv run --frozen python scripts/render_technical_report.py
```

This creates `docs/TECHNICAL-REPORT.pdf` using Pandoc and Typst (on macOS,
`brew install pandoc typst`). `scripts/prepare_zenodo.py` also rebuilds the PDF
before packaging, so the upload always reflects the current Markdown.
