# Changelog — mlu-000005

All notable changes to this contribution. Versions follow [semantic versioning](https://semver.org).

## [0.2.0] — 2026-09-21

The session no longer assumes four apps exist. **The room builds three of them, live, from
prompts** — which is also what attendees can take home and use again.

### Added
- `materials/prompts/` — five prompts. Three the room builds its own tools from, two the
  facilitator prepares. Each states the outputs it must produce on the sample pack before you
  rehearse, because the session turns on three specific results and a build that misses them
  looks fine and teaches nothing.
- `materials/prompts/MASTER-FOLLOW-ALONG.md` — the single document attendees follow. Every step
  is self-contained; nothing sends them to another file mid-task.
- `materials/prompts/DRIVE-FOLDER.md` — the shared folder's layout, sharing settings, and what
  must **not** go in it before the session starts.
- `materials/prompts/facilitator/RUN-KIRO.md` — presenter runbook for the watched segment.
- `materials/verify_deck.py` and `materials/approved-deck-baseline.txt` — proves a rebuilt deck
  only ever removes copy from the approved slides. `export_pdf.sh` will not run until it passes.
- `materials/DECK-APPROVAL.md` — what may change on the approved slides, and why a checksum was
  the wrong check for it.
- `materials/build_pack.py` and `materials/brand/` — renders the documents through the DTCC
  handbook stylesheet. Three PDFs land in `materials/dist/`: the follow-along guide, the
  facilitator guide, and the take-home pack.
- `materials/session_config.py` — the shared-folder link, date and venue in one place, because
  they are stamped into the deck, the packs and the handouts.
- `materials/activities/sample-pack/rubric-weak.json` — the weak rubric in `mlu-rubric/1` format,
  so the Stress Test can load both sides of the comparison.
- `materials/kiro-grader/` — a workspace for the Kiro segment, seeded by `seed.sh` from the
  sample pack rather than carrying a second copy of it.

### Changed
- **Deck: 28 slides to 29.** A new slide 0 carries the shared-folder QR code at full size, and
  the code is stamped on every slide after it. It is numbered **0** so that every cross-reference
  in the talk track and the handouts still points at the slide it always did.
- Copy was **removed** from slides 2, 7, 13, 15 and 25: the steps that pointed at pre-published
  apps, the paper that is no longer on anyone's table, and the clause on slide 7 that gave away
  the slide 11 reveal twenty minutes early. Nothing was added and nothing was reworded.
- Three unapproved **additions** the deck source had been carrying were reverted to the approved
  copy. They were harmless only while the deck was never rebuilt.
- Talk track reworked throughout — the checklists, and slides 0, 2, 7, 10, 13, 15, 17, 19, 21,
  24, 25 and 26.
- Participants no longer bring their own assignment. One assignment, in the document, ready to
  paste. It saves several minutes and means the room hits the same problems at the same moment,
  which is what makes volunteers effective rather than scattered.
- Nothing is printed. The opening grading exercise happens in the follow-along document.

### Removed
- `APPS_YOU_MUST_BUILD.md`. Its premise — that four apps had to be built before the session could
  run — is exactly what this version replaces.

### Known gaps
- **Expected outcomes in `sample-pack/README.md` are still hand-scored predictions**, not recorded
  results. Replace them after the first rehearsal; model output varies run to run.
- **The materials carry the date, venue and contacts of the first delivery.** They are examples to
  replace, not content. `session_config.py` is where the session facts belong.
- Still `pilot`: the session has not yet been delivered to a room.

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
