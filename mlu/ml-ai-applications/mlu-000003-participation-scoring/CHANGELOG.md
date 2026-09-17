# Changelog — mlu-000003

All notable changes to this contribution. Versions follow [semantic versioning](https://semver.org).

## [1.0.0] — 2026-09-17

First publication in the DTCC-MLU repository.

### Added
- `participation-scoring-lab.ipynb` — transcript parsing, grounded relevance judgment, 0–4 scoring,
  and `.md` + `.csv` export, with a mandatory human review step in Part 5.
- `mlu_utils/transcript_tools.py` — VTT parsing and per-speaker aggregation.
- A fabricated sample transcript, roster, and lesson PDF spanning every participation tier, so the
  tool can be evaluated without touching real student records.
- Podium walkthrough with expected outputs for the sample.

### Notes
- Carried over from the AWS-MLU Faculty Fellows Impact Inventory. Materials were reorganised into
  the standard contribution layout; the notebook itself is unchanged.
