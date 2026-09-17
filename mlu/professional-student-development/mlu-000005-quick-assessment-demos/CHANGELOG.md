# Changelog — mlu-000005

All notable changes to this contribution. Versions follow [semantic versioning](https://semver.org).

## [0.1.0] — 2026-09-17

First publication in the DTCC-MLU repository, at **pilot** maturity.

### Added
- 90-minute session deck as `.pdf` and editable `.pptx`, with `build_deck.py` to regenerate it.
- Per-slide talk track covering preconditions, talking points, and the thread to protect under time
  pressure.
- Opening participant handout.
- Sample pack: one assignment, one course reading, a deliberately weak rubric, a golden rubric in
  `mlu-rubric/1` format, four papers, and a five-student roster.
- `rubric-format.md` documenting `mlu-rubric/1`, which loads unchanged into `mlu-000004`.

### Known gaps
- **Expected outcomes in `sample-pack/README.md` are hand-scored predictions, not recorded
  results.** Replace them after the first rehearsal; model output varies run to run.
- The session has not yet been delivered to a room. Move to `classroom-tested` only after it has,
  with the resulting revisions folded back in.

### Notes
- Working notes (`PLAN.md`) were left out of the published contribution.
