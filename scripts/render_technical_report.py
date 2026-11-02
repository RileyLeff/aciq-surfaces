"""Compile the README (the technical report) to PDF using Pandoc and Typst."""

import argparse
from pathlib import Path
import re
import shutil
import subprocess

ROOT = Path(__file__).resolve().parents[1]
# Relative links work on GitHub but not in a PDF, so point them at the tagged release.
REPO = "https://github.com/RileyLeff/aciq-surfaces"
TAG = "v1.0.0"


def absolute_link(match):
    target = match.group(1)
    if re.match(r"[a-z]+:|#", target):
        return match.group(0)
    kind = "tree" if target.endswith("/") else "blob"
    return f"]({REPO}/{kind}/{TAG}/{target})"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=ROOT / "docs/TECHNICAL-REPORT.pdf")
    args = parser.parse_args()
    for tool in ("pandoc", "typst"):
        if shutil.which(tool) is None:
            parser.error(f"Install {tool} first (macOS: brew install pandoc typst).")
    output = args.output.resolve()
    output.parent.mkdir(parents=True, exist_ok=True)
    markdown = re.sub(r"\]\(([^)\s]+)\)", absolute_link, (ROOT / "README.md").read_text())
    subprocess.run([
        "pandoc", "-",
        "--from=markdown+autolink_bare_uris", "--pdf-engine=typst",
        "--include-in-header", str(ROOT / "docs/report-style.typ"),
        "--variable=papersize:us-letter", "--variable=mainfont:Helvetica",
        "--variable=fontsize:10.5pt", "--variable=page-numbering:1",
        "--metadata=lang:en", "--output", str(output),
    ], cwd=ROOT, check=True, input=markdown, text=True)
    print(output)


if __name__ == "__main__":
    main()
