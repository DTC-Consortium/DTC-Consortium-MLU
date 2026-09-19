# Changelog — mlu-000007

All notable changes to this contribution. Versions follow [semantic versioning](https://semver.org).

## [1.0.0] — 2026-09-19

First publication in the DTCC-MLU repository.

### Added
- `phishing-detector-assignment.md` — the student handout: PartyRock build instructions with the
  required structured-output fields, the human-vs-AI results table, the Fool the AI adversarial log,
  and the five reflection prompts.
- `phishing-detector-assignment.docx` — the author's original Word version, unchanged, carrying both
  the student handout (Part A) and the instructor guide (Part B) in one file.
- `instructor-facilitation-guide.md` — prep checklist, facilitation notes for all four phases,
  debrief discussion questions, a common-pitfalls table, and the responsible-use guardrail.
- `phishing-detector-rubric.md` — the 100-point rubric, separated out so it can be dropped into an
  LMS on its own.

### Known gaps
- **The ground-truth email bank is not included.** The assignment requires at least 15 pre-labelled
  emails, which each instructor must assemble from vetted phishing-awareness archives or
  institutional security training material. The specification is in the facilitation guide. Sample
  emails were not bundled because a licence-clean, openly redistributable phishing corpus was not
  available to ship with the contribution.

### Notes
- Contributed through the AWS-MLU Faculty Fellows programme and delivered in *AI Essentials* at
  Oklahoma City Community College, where it runs in week 7.
- The Markdown files are a faithful transcription of the author's Word document, split into student
  handout, instructor guide, and rubric to match the repository's contribution layout. Content is
  unchanged; the original `.docx` ships alongside so the two can be compared.
