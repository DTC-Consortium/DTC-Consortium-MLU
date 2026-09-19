# Changelog — mlu-000010

All notable changes to this contribution. Versions follow [semantic versioning](https://semver.org).

## [1.0.0] — 2026-09-19

First publication in the DTCC-MLU repository.

### Added
- `using-the-app.md` — what the app does, the quick start, what the three redesign levels mean, the
  pattern the redesigns follow, and the responsible-use limits.
- `app-build-example.md` — a recorded run of two of the author's real assignments through the app,
  with the input instructions and rubrics and the app's own output screenshots.
- `everyday-bureaucracy-analysis.md` — full redesign output for a reflective applied assignment at a
  60% AI-grade ceiling, with per-criterion changes and rationale at all three strength levels.
- `exploratory-research-analysis.md` — full redesign output for a source-based research assignment
  at a 70% ceiling, showing how recommendations shift when evidence requirements differ.
- Eleven interface and output screenshots under `materials/media/`.

### Known gaps
- **The app itself is linked, not bundled.** An Amazon Quick app is a hosted object rather than a
  file. The published app can be changed or removed by its owner, and the build prompt that produced
  it is not included — only the recorded build example.
- **One screenshot is missing.** In the author's source repository, the "Heightened Security"
  image for the Everyday Bureaucracy example is a byte-identical duplicate of the Minimum
  Robustness image, so no recorded screenshot of that level exists. The duplicate was dropped
  rather than republished under the wrong caption; the full text of that redesign level is in
  `everyday-bureaucracy-analysis.md`.
- **Last tested September 2026.** Model behaviour behind the app changes over time; re-run the
  worked examples before relying on the recorded output as a benchmark.

### Notes
- Contributed through the AWS-MLU Faculty Fellows programme. Developed at Oklahoma City Community
  College through work on generative and agentic AI, assessment design, and faculty workforce
  upskilling.
- Three edits were made to the example files when moving them into the repository: Obsidian-style
  `![[image]]` embeds were rewritten as relative Markdown image links with descriptive alt text, two
  dangling wiki-links were replaced with links to the published analyses, and a rubric table that
  had been mangled into escaped HTML by an earlier export was rebuilt as a standard Markdown table.
  No wording was changed.
