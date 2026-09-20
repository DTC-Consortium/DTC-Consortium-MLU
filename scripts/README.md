# Scripts

Validation, catalog generation, link checking, packaging, and the printable handbook. Install
with `pip install -r requirements.txt`.

The first five are plain Python with two dependencies and run anywhere. `build_handbook.py` is the
exception: it needs a few more packages and a copy of Google Chrome. That is deliberate — see
below.

| Script | What it does | Writes |
|---|---|---|
| `validate_contributions.py` | Schema conformance, ID uniqueness and registration, category placement, required files, materials manifest paths, cross-references, taxonomy warnings | nothing |
| `generate_boilerplate.py` | Regenerates each contribution's `LICENSE.md` and `CITATION.cff` from its metadata | contributions |
| `build_catalog.py` | Regenerates the catalog, the category indexes, the collections index, and the root README's category table | catalog, indexes |
| `check_links.py` | Local Markdown links always; public links with `--external` | nothing |
| `package_contribution.py` | Builds one contribution's release ZIP | `dist/` |
| `build_handbook.py` | Builds the printable Faculty Handbook — every contribution in full, one branded PDF | `dist/` |

## The usual sequence

```bash
pip install -r scripts/requirements.txt
python3 scripts/generate_boilerplate.py
python3 scripts/build_catalog.py
python3 scripts/validate_contributions.py
python3 scripts/check_links.py
```

`generate_boilerplate.py` and `build_catalog.py` both take `--check`, which fails without writing.
CI uses that to catch metadata changes whose generated output was never regenerated.

## The handbook

```bash
python3 scripts/build_handbook.py          # -> dist/dtcc-mlu-handbook-YYYY.MM.pdf
python3 scripts/build_handbook.py --skip-appendices   # faster, prose only
python3 scripts/build_handbook.py --keep-html         # keep the intermediate HTML to debug layout
```

It renders every contribution's README, materials and notebooks into one document, merges each
contribution's instructional slide decks and readings in as appendices, and stamps running
furniture and a PDF outline. Expect a few minutes and roughly 500 pages.

Three things worth knowing before you change it:

**It needs Chrome.** The handbook has to match the branding on dtcconsortium.org, which means
rendering real CSS. Chrome is the only renderer on hand that does that faithfully — pandoc has no
PDF engine installed, and a pure-Python drawing library would mean rebuilding the brand by hand.
Set `CHROME` if the binary is somewhere unusual.

**It runs three passes.** The first locates every section, the second re-renders so the contents
page can carry true page numbers, and the third drops the internal section markers so they never
reach the reader's text selection. If the third pass changes pagination, the build says so and
keeps the second.

**Its output is a build artifact.** The PDF belongs in `dist/`, never committed, and the handbook
build is *not* part of the pull-request check — a PDF is not byte-reproducible, so `--check` on one
would fail at random.

## Two things these scripts will not do

**They never execute contributed code.** Metadata validation parses YAML and checks paths; it does
not import a contributor's module or run a notebook. A reviewer running a notebook deliberately, in
an environment they control, is a different thing — see [`../docs/review.md`](../docs/review.md).

**`check_links.py` never fails on an external link.** A public site being down is not a defect in
this repository. External failures are reported for a human to judge; only broken *local* links
fail the run.
