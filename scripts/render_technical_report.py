"""Compile the README (the technical report) to PDF using Pandoc and Typst."""

import argparse
from pathlib import Path
import shutil
import subprocess

ROOT = Path(__file__).resolve().parents[1]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=ROOT / "docs/TECHNICAL-REPORT.pdf")
    args = parser.parse_args()
    for tool in ("pandoc", "typst"):
        if shutil.which(tool) is None:
            parser.error(f"Install {tool} first (macOS: brew install pandoc typst).")
    output = args.output.resolve()
    output.parent.mkdir(parents=True, exist_ok=True)
    subprocess.run([
        "pandoc", str(ROOT / "README.md"),
        "--from=markdown+autolink_bare_uris", "--pdf-engine=typst",
        "--include-in-header", str(ROOT / "docs/report-style.typ"),
        "--variable=papersize:us-letter", "--variable=mainfont:Helvetica",
        "--variable=fontsize:10.5pt", "--variable=page-numbering:1",
        "--metadata=lang:en", "--output", str(output),
    ], cwd=ROOT, check=True)
    print(output)


if __name__ == "__main__":
    main()
