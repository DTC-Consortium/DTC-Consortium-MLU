#!/usr/bin/env python3
"""Validate every mlu-contribution.yml in the repository.

Checks, in order:
  1. Schema conformance against schemas/mlu-contribution.schema.json.
  2. ID uniqueness, and that the ID matches the directory name and ID-REGISTER.md.
  3. That the contribution sits under the directory for its declared category.
  4. That every required sibling file exists (README, CHANGELOG, LICENSE, CITATION).
  5. That every local path in the materials manifest exists on disk.
  6. That parent_id, related_ids, and collection_ids resolve to things that exist.
  7. Taxonomy values, as warnings only.

Read-only. Never imports or executes contributed code.

Exit code 0 when there are no errors; 1 otherwise. Warnings never fail the run.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    sys.exit("PyYAML is required: pip install -r scripts/requirements.txt")
try:
    from jsonschema import Draft202012Validator
except ImportError:
    sys.exit("jsonschema is required: pip install -r scripts/requirements.txt")

ROOT = Path(__file__).resolve().parent.parent
SCHEMA = ROOT / "schemas" / "mlu-contribution.schema.json"
TAXONOMY = ROOT / "catalog" / "taxonomy.yml"
REGISTER = ROOT / "ID-REGISTER.md"
COLLECTIONS = ROOT / "collections"
REQUIRED_SIBLINGS = ["README.md", "CHANGELOG.md", "LICENSE.md", "CITATION.cff"]

errors: list[str] = []
warnings: list[str] = []


def err(where: Path, msg: str) -> None:
    errors.append(f"{where.relative_to(ROOT)}: {msg}")


def warn(where: Path, msg: str) -> None:
    warnings.append(f"{where.relative_to(ROOT)}: {msg}")


def registered_ids() -> set[str]:
    if not REGISTER.exists():
        return set()
    return set(re.findall(r"\bmlu-\d{6}\b", REGISTER.read_text(encoding="utf-8")))


def known_collections() -> set[str]:
    return {p.stem for p in COLLECTIONS.glob("*.yml")}


def main() -> int:
    schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
    validator = Draft202012Validator(schema)
    taxonomy = yaml.safe_load(TAXONOMY.read_text(encoding="utf-8"))
    in_register = registered_ids()
    collections = known_collections()

    files = sorted(ROOT.glob("mlu/*/*/mlu-contribution.yml"))
    if not files:
        print("No contributions found under mlu/. Nothing to validate.")
        return 0

    seen: dict[str, Path] = {}
    docs: dict[str, dict] = {}

    for path in files:
        cdir = path.parent
        try:
            doc = yaml.safe_load(path.read_text(encoding="utf-8"))
        except yaml.YAMLError as exc:
            err(path, f"is not valid YAML: {exc}")
            continue
        if not isinstance(doc, dict):
            err(path, "did not parse to a mapping")
            continue

        # 1. schema
        schema_errors = sorted(validator.iter_errors(doc), key=lambda e: list(e.path))
        for e in schema_errors:
            loc = "/".join(str(p) for p in e.path) or "(root)"
            err(path, f"schema: {loc}: {e.message}")
        if schema_errors:
            continue

        cid = doc["id"]
        docs[cid] = doc

        # 2. ID uniqueness, directory agreement, register
        if cid in seen:
            err(path, f"duplicate ID {cid}, already used by {seen[cid].relative_to(ROOT)}")
        seen[cid] = path
        if not cdir.name.startswith(f"{cid}-"):
            err(path, f"ID {cid} does not match directory name {cdir.name!r}")
        if in_register and cid not in in_register:
            err(path, f"ID {cid} is not recorded in ID-REGISTER.md")

        # 3. category placement
        if cdir.parent.name != doc["category"]:
            err(path, f"category {doc['category']!r} but the directory sits under {cdir.parent.name!r}")

        # 4. required siblings
        for name in REQUIRED_SIBLINGS:
            if not (cdir / name).exists():
                err(path, f"missing required file {name}")

        # 5. materials manifest
        for item in doc["materials"]:
            p = item["path"]
            if item.get("external") or p.startswith(("http://", "https://")):
                if not item.get("access"):
                    warn(path, f"external material {p} has no access instructions")
                continue
            if not (cdir / p).exists():
                err(path, f"materials manifest lists {p}, which does not exist")

        # licence data paths
        for entry in doc.get("licenses", {}).get("data") or []:
            if not (cdir / entry["path"]).exists():
                err(path, f"licenses.data lists {entry['path']}, which does not exist")

        # download_url must not be advertised before the release exists
        gh = doc["github"]
        if gh.get("download_url") and doc["version"] not in gh["download_url"]:
            err(path, "github.download_url does not reference the declared version")
        if gh["path"] != str(cdir.relative_to(ROOT)):
            err(path, f"github.path {gh['path']!r} does not match the actual location")

        # 7. taxonomy, warnings only
        subtypes = taxonomy["categories"][doc["category"]]["subtypes"]
        if doc["subtype"] not in subtypes:
            warn(path, f"subtype {doc['subtype']!r} is not in the taxonomy for {doc['category']}")
        for field, key in (("disciplines", "disciplines"), ("tools", "tools"), ("audience", "audiences")):
            for value in doc[field]:
                if value not in taxonomy[key]:
                    warn(path, f"{field} value {value!r} is not in the taxonomy")

    # 6. cross-references, once every doc is loaded
    for cid, doc in docs.items():
        path = seen[cid]
        parent = doc.get("parent_id")
        if parent and parent not in docs:
            err(path, f"parent_id {parent} does not resolve to a contribution in this repository")
        for rel in doc.get("related_ids") or []:
            if rel == cid:
                err(path, "related_ids lists the contribution's own ID")
            elif rel not in docs:
                err(path, f"related_ids lists {rel}, which does not resolve")
        for coll in doc.get("collection_ids") or []:
            if collections and coll not in collections:
                err(path, f"collection_ids lists {coll}, which has no collections/{coll}.yml")

    for w in warnings:
        print(f"warning: {w}")
    for e in errors:
        print(f"error: {e}", file=sys.stderr)

    print(f"\n{len(files)} contribution(s): {len(errors)} error(s), {len(warnings)} warning(s)")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
