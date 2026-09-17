#!/usr/bin/env python3
"""Check links across the repository.

Two kinds:
  * Local links in Markdown — resolved against the filesystem. A broken one fails the run,
    because it is always a mistake and always fixable here.
  * Public http(s) links — requested with a HEAD, falling back to GET. These are *reported*,
    never failed: an external site being down is not a defect in this repository.

Usage:
  python3 scripts/check_links.py              # local links only, fast, safe for PR validation
  python3 scripts/check_links.py --external   # also check public links (used by the scheduled job)
  python3 scripts/check_links.py --external --format=markdown   # issue-ready report
"""
from __future__ import annotations

import concurrent.futures
import re
import sys
import urllib.error
import urllib.request
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parent.parent
SKIP_DIRS = {".git", "__pycache__", ".ipynb_checkpoints", "node_modules"}
LINK_RE = re.compile(r"\[[^\]]*\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")
TIMEOUT = 20
USER_AGENT = "DTCC-MLU-link-check/1.0 (+https://github.com/DTC-Consortium/DTC-Consortium-MLU)"


def markdown_files() -> list[Path]:
    out = []
    for p in ROOT.rglob("*.md"):
        if not SKIP_DIRS.intersection(p.parts):
            out.append(p)
    return sorted(out)


def collect() -> tuple[list[tuple[Path, int, str]], set[str]]:
    local, external = [], set()
    for f in markdown_files():
        for i, line in enumerate(f.read_text(encoding="utf-8", errors="replace").splitlines(), 1):
            for target in LINK_RE.findall(line):
                if target.startswith(("http://", "https://")):
                    external.add(target)
                elif target.startswith(("#", "mailto:", "tel:", "data:")):
                    continue
                else:
                    local.append((f, i, target))
    return local, external


def check_local(local) -> list[str]:
    bad = []
    for f, line, target in local:
        path = target.split("#", 1)[0]
        if not path:
            continue
        # ../../issues/new?template=... is GitHub's relative-URL form, valid only once hosted.
        if "?" in path or path.lstrip("./").startswith(("issues", "pull", "compare")):
            continue
        if not (f.parent / path).exists():
            bad.append(f"{f.relative_to(ROOT)}:{line}: {target}")
    return bad


def check_one(url: str) -> tuple[str, str | None]:
    req = urllib.request.Request(url, method="HEAD", headers={"User-Agent": USER_AGENT})
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT):
            return url, None
    except urllib.error.HTTPError as e:
        if e.code == 401:
            # The page exists; it just wants a login. Not broken.
            return url, None
        if e.code in (403, 405, 501):  # many hosts refuse HEAD
            try:
                req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
                with urllib.request.urlopen(req, timeout=TIMEOUT):
                    return url, None
            except Exception as e2:  # noqa: BLE001
                return url, f"{type(e2).__name__}: {e2}"
        return url, f"HTTP {e.code}"
    except Exception as e:  # noqa: BLE001
        return url, f"{type(e).__name__}: {e}"


def main() -> int:
    as_markdown = "--format=markdown" in sys.argv
    do_external = "--external" in sys.argv
    local, external = collect()

    bad_local = check_local(local)
    print(f"Checked {len(local)} local link(s) across {len(markdown_files())} Markdown file(s).")
    for b in bad_local:
        print(f"error: broken local link: {b}", file=sys.stderr)

    failures: list[tuple[str, str]] = []
    if do_external:
        print(f"Checking {len(external)} public link(s)…")
        with concurrent.futures.ThreadPoolExecutor(max_workers=8) as pool:
            for url, problem in pool.map(check_one, sorted(external)):
                if problem:
                    failures.append((url, problem))

        if as_markdown:
            print("\n---\n")
            if not failures:
                print("All public links resolved. No action needed.")
            else:
                print(f"**{len(failures)} public link(s) did not resolve.** "
                      "These are flagged for review, not auto-corrected. "
                      "Transient failures are common; a link that fails twice in a row is worth chasing.\n")
                print("| Link | Result | Where |")
                print("|---|---|---|")
                where = {}
                for f in markdown_files():
                    text = f.read_text(encoding="utf-8", errors="replace")
                    for url, _ in failures:
                        if url in text:
                            where.setdefault(url, []).append(str(f.relative_to(ROOT)))
                for url, problem in failures:
                    locs = ", ".join(f"`{w}`" for w in where.get(url, [])[:3]) or "—"
                    print(f"| {url} | {problem} | {locs} |")
        else:
            for url, problem in failures:
                print(f"warning: {url} -> {problem}")
            print(f"\n{len(failures)} public link(s) did not resolve (reported, not failed).")

    if bad_local:
        print(f"\n{len(bad_local)} broken local link(s).", file=sys.stderr)
        return 1
    print("\nNo broken local links.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
