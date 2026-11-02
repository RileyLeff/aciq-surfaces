"""Build and verify a local Zenodo upload; never contacts or publishes to Zenodo."""

import argparse
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import sys
import zipfile

ROOT = Path(__file__).resolve().parents[1]
PREFIX = "aciq-surfaces"
ADDITIONS = {
    "scripts/prepare_zenodo.py",
    "docs/ZENODO-DEPOSIT.md",
    "scripts/render_technical_report.py",
    "docs/report-style.typ",
    "docs/TECHNICAL-REPORT.pdf",
}
EXCLUDED = set()


def git(*args):
    return subprocess.check_output(["git", *args], cwd=ROOT)


def sha256(path):
    with path.open("rb") as stream:
        return hashlib.file_digest(stream, "sha256").hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--destination", required=True, type=Path)
    args = parser.parse_args()
    destination = args.destination.resolve()
    if destination == ROOT or ROOT in destination.parents:
        parser.error("Use a new destination outside the source repository.")
    if destination.exists():
        parser.error("Destination already exists; use a new folder to preserve previous builds.")

    subprocess.run([sys.executable, str(ROOT / "scripts/render_technical_report.py")], check=True)
    subprocess.run(
        ["uv", "run", "--frozen", "python", "scripts/release_manifest.py", "--check"],
        cwd=ROOT, check=True,
    )
    paths = sorted((set(git("ls-files", "-z").decode().strip("\0").split("\0")) | ADDITIONS) - EXCLUDED)
    records = []
    for name in paths:
        path = ROOT / name
        if path.is_symlink() or not path.is_file():
            raise ValueError(f"Missing, symlinked, or non-file source: {name}")
        with path.open("rb") as stream:
            if stream.read(128).startswith(b"version https://git-lfs.github.com/spec/v1"):
                raise ValueError(f"Unhydrated LFS pointer: {name}")
        records.append({"path": name, "bytes": path.stat().st_size, "sha256": sha256(path)})

    provenance = {
        "source_commit": git("rev-parse", "HEAD").decode().strip(),
        "repository": "https://github.com/RileyLeff/aciq-surfaces",
        "snapshot_kind": "tracked files at source_commit plus the rendered technical report; see working_tree_status",
        "version": "1.0.0",
        "doi": "10.5281/zenodo.23785367",
        "protocol_doi": "10.17504/protocols.io.m6gp8em98lzp/v1",
        "working_tree_status": git("status", "--short").decode(),
        "explicit_additions": sorted(ADDITIONS),
        "excluded_editorial_drafts": sorted(EXCLUDED),
        "note": "File hashes describe the included bytes; source_commit alone does not describe uncommitted additions or edits.",
        "files": records,
    }
    destination.mkdir(parents=True)
    archive = destination / f"{PREFIX}.zip"
    with zipfile.ZipFile(archive, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=6) as output:
        for record in records:
            path = ROOT / record["path"]
            output.write(path, f"{PREFIX}/{record['path']}")
        output.writestr(f"{PREFIX}/ARCHIVE-MANIFEST.json", json.dumps(provenance, indent=2) + "\n")

    # Check the archived bytes, not just the source files or ZIP CRCs.
    with zipfile.ZipFile(archive) as bundle:
        for record in records:
            with bundle.open(f"{PREFIX}/{record['path']}") as stream:
                actual = hashlib.file_digest(stream, "sha256").hexdigest()
            if actual != record["sha256"]:
                raise ValueError(f"Archive/source mismatch: {record['path']}")
        assert len(bundle.infolist()) == len(records) + 1

    shutil.copy2(ROOT / "docs/TECHNICAL-REPORT.pdf", destination / "TECHNICAL-REPORT.pdf")
    (destination / "deposit-fields.md").write_text((ROOT / "docs/ZENODO-DEPOSIT.md").read_text())
    (destination / "README.txt").write_text(
        "Coupled A/Ci/Q and chlorophyll fluorescence surfaces for Phragmites australis across a coastal marsh elevation gradient\n"
        "Riley Leff, Acadia Conboy, Keryn Gedan\n\n"
        "Archive version: 1.0.0\n"
        "Archive DOI: https://doi.org/10.5281/zenodo.23785367\n"
        "Operating protocol: https://doi.org/10.17504/protocols.io.m6gp8em98lzp/v1\n"
        f"Source base commit: {provenance['source_commit']}\n"
        "The ZIP holds the tracked files at that commit plus the rendered TECHNICAL-REPORT.pdf.\n"
        "ARCHIVE-MANIFEST.json inside the ZIP records exact files, hashes, and working-tree status.\n\n"
        "Extract aciq-surfaces.zip. Start with README.md (the technical\n"
        "report), docs/DATA.md, and scripts/README.md.\n"
        "Edit README.md and rebuild the PDF with:\n"
        "  uv run --frozen python scripts/render_technical_report.py\n"
        "Requires Pandoc and Typst (macOS: brew install pandoc typst).\n"
        "The large cohort CSV is included as real data; Git LFS is not needed to read it.\n\n"
        "Data, original figures and documentation: CC BY 4.0. Source code: MIT.\n"
        "See LICENSE, LICENSE-DATA.md and THIRD_PARTY.md inside the archive.\n\n"
        "Verify uploaded files with: shasum -a 256 -c SHA256SUMS.txt\n"
        "deposit-fields.md is an editorial aid and is not part of the upload set.\n"
    )
    upload_files = [archive, destination / "README.txt", destination / "TECHNICAL-REPORT.pdf"]
    (destination / "SHA256SUMS.txt").write_text(
        "".join(f"{sha256(path)}  {path.name}\n" for path in upload_files)
    )
    print(json.dumps({"destination": str(destination), "archived_files": len(records),
                      "uncompressed_bytes": sum(r["bytes"] for r in records),
                      "zip_bytes": archive.stat().st_size, "verified": True}, indent=2))


if __name__ == "__main__":
    main()
