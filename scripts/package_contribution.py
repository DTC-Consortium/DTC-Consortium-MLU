#!/usr/bin/env python3
"""Package one approved contribution and version as a release ZIP.

  python3 scripts/package_contribution.py mlu-000001 [--out dist]

Produces dist/<id>-v<version>.zip containing that contribution's documentation, metadata,
licences, and distributable materials — and nothing else.

Deliberately excluded: caches, checkpoints, OS cruft, and any local run output. External
resources are not bundled; they are written into RESOURCES.md inside the ZIP with access
instructions, from the external entries in the materials manifest.
"""
from __future__ import annotations

import argparse
import sys
import zipfile
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
EXCLUDE_DIRS = {"__pycache__", ".ipynb_checkpoints", ".git", ".venv", "node_modules"}
EXCLUDE_NAMES = {".DS_Store", "Thumbs.db"}
EXCLUDE_SUFFIXES = {".pyc", ".pyo"}
TOP_LEVEL = ["README.md", "mlu-contribution.yml", "CHANGELOG.md", "LICENSE.md", "CITATION.cff"]


def find(cid: str) -> Path:
    matches = [p.parent for p in ROOT.glob(f"mlu/*/{cid}-*/mlu-contribution.yml")]
    if not matches:
        sys.exit(f"No contribution directory found for {cid}.")
    if len(matches) > 1:
        sys.exit(f"{cid} resolves to more than one directory: {matches}")
    return matches[0]


def includable(p: Path) -> bool:
    if EXCLUDE_DIRS.intersection(p.parts):
        return False
    return p.name not in EXCLUDE_NAMES and p.suffix not in EXCLUDE_SUFFIXES


def resources_md(doc: dict) -> str | None:
    """A manifest of everything hosted outside the ZIP."""
    ext = [m for m in doc["materials"]
           if m.get("external") or str(m["path"]).startswith(("http://", "https://"))]
    if not ext:
        return None
    out = [
        f"# External resources — {doc['id']} v{doc['version']}",
        "",
        "These materials are part of this contribution but are **not included in this package** —",
        "videos and large datasets are kept in approved external hosting. Access each one below.",
        "",
    ]
    for m in ext:
        out += [f"## {m['description']}", "", f"- **Location:** {m['path']}"]
        if m.get("access"):
            out.append(f"- **Access:** {m['access']}")
        out.append("")
    return "\n".join(out)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("id", help="Contribution ID, e.g. mlu-000001")
    ap.add_argument("--out", default="dist", help="Output directory (default: dist)")
    args = ap.parse_args()

    cdir = find(args.id)
    doc = yaml.safe_load((cdir / "mlu-contribution.yml").read_text(encoding="utf-8"))

    missing = [n for n in TOP_LEVEL if not (cdir / n).exists()]
    if missing:
        sys.exit(f"{args.id} is missing required file(s): {', '.join(missing)}")
    if not (cdir / "materials").is_dir():
        sys.exit(f"{args.id} has no materials/ directory.")

    stem = f"{doc['id']}-v{doc['version']}"
    out_dir = (ROOT / args.out) if not Path(args.out).is_absolute() else Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / f"{stem}.zip"

    files: list[Path] = [cdir / n for n in TOP_LEVEL]
    for extra in ("examples", "media", "references"):
        if (cdir / extra).is_dir():
            files += [p for p in (cdir / extra).rglob("*") if p.is_file()]
    files += [p for p in (cdir / "materials").rglob("*") if p.is_file()]
    files = [p for p in files if includable(p)]

    with zipfile.ZipFile(target, "w", zipfile.ZIP_DEFLATED) as z:
        for p in files:
            z.write(p, arcname=str(Path(stem) / p.relative_to(cdir)))
        res = resources_md(doc)
        if res:
            z.writestr(str(Path(stem) / "RESOURCES.md"), res)

    with zipfile.ZipFile(target) as z:
        broken = z.testzip()
        if broken:
            sys.exit(f"Archive is corrupt at {broken}")
        count = len(z.namelist())

    size = target.stat().st_size
    print(f"{target.relative_to(ROOT) if target.is_relative_to(ROOT) else target}")
    print(f"  {count} file(s), {size / 1_048_576:.1f} MiB")
    print(f"  release tag: {stem}")
    if not doc["github"].get("download_url"):
        print("\n  Reminder: after the release exists, set github.download_url in")
        print("  mlu-contribution.yml and rerun scripts/build_catalog.py, or the catalog")
        print("  will keep showing this contribution as not yet released.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
