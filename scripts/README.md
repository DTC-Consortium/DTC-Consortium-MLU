# Scripts

Validation, catalog generation, link checking, and packaging. All are plain Python with two
dependencies; install them with `pip install -r requirements.txt`.

| Script | What it does | Writes |
|---|---|---|
| `validate_contributions.py` | Schema conformance, ID uniqueness and registration, category placement, required files, materials manifest paths, cross-references, taxonomy warnings | nothing |
| `generate_boilerplate.py` | Regenerates each contribution's `LICENSE.md` and `CITATION.cff` from its metadata | contributions |
| `build_catalog.py` | Regenerates the catalog, the category indexes, the collections index, and the root README's category table | catalog, indexes |
| `check_links.py` | Local Markdown links always; public links with `--external` | nothing |
| `package_contribution.py` | Builds one contribution's release ZIP | `dist/` |

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

## Two things these scripts will not do

**They never execute contributed code.** Metadata validation parses YAML and checks paths; it does
not import a contributor's module or run a notebook. A reviewer running a notebook deliberately, in
an environment they control, is a different thing — see [`../docs/review.md`](../docs/review.md).

**`check_links.py` never fails on an external link.** A public site being down is not a defect in
this repository. External failures are reported for a human to judge; only broken *local* links
fail the run.
