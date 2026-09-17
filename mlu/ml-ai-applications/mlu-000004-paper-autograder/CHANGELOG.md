# Changelog — mlu-000004

All notable changes to this contribution. Versions follow [semantic versioning](https://semver.org).

## [1.0.0] — 2026-09-17

First publication in the DTCC-MLU repository.

### Added
- `paper-grading-lab.ipynb` — per-criterion tiering with quoted evidence, grounded correctness
  judgment, weighted grade computed in code, and `.csv` / `.md` / per-student feedback export, with
  a mandatory human review step in Part 5.
- A fully local Ollama path alongside the Bedrock path, so papers need never leave the machine.
- `mlu_utils/paper_tools.py` — paper loading, rubric parsing, and grading.
- Three fabricated sample papers — one strong, one fluent-but-wrong, one off-topic — a rubric, a
  roster, and course material.
- A recorded sample run under `materials/evaluation/` for comparison against a fresh install.
- Podium walkthrough with expected outputs for the sample.

### Notes
- Carried over from the AWS-MLU Faculty Fellows Impact Inventory. Materials were reorganised into
  the standard contribution layout; the notebook itself is unchanged.
