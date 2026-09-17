# MLU Contribution ID Register

Every contribution gets one permanent ID in the form `mlu-000001`. **IDs are assigned by a
repository maintainer, never self-assigned**, so two contributions can never collide. An ID is
never reused, never renumbered, and never recycled after a withdrawal — it is the stable handle that
citations, collections, and release tags depend on.

## How to get one

1. Open a **New MLU contribution** issue. Do not pick an ID.
2. A maintainer adds the next unused ID to the table below in a pull request, and replies on the
   issue with it.
3. Use that ID for the directory name (`<id>-<short-slug>`), the `id:` field in
   `mlu-contribution.yml`, and the release tag.

`scripts/validate_contributions.py` fails any contribution whose ID is missing from this table, or
whose ID does not match its directory name.

## When something needs its own ID

A course module gets its own ID when it is **independently reusable and downloadable**. Otherwise it
stays inside its parent package and is described in that package's README. If it does get its own
ID, set `parent_id` to the package it came from.

## Assigned

| ID | Title | Category | Assigned | Status |
|---|---|---|---|---|
| `mlu-000001` | Curriculum Embedding Lab — Embed AI in Your Course | professional-student-development | 2026-09-17 | Published |
| `mlu-000002` | Discipline-Specific AI Teaching Assistant — Seminar Lab | professional-student-development | 2026-09-17 | Published |
| `mlu-000003` | Class Participation Scoring — Transcript to Draft Score | ml-ai-applications | 2026-09-17 | Published |
| `mlu-000004` | Paper Autograder — Rubric-Based Draft Grading | ml-ai-applications | 2026-09-17 | Published |
| `mlu-000005` | The Assignment Lifecycle — Quick Assessment Demo Session | professional-student-development | 2026-09-17 | Published (pilot) |

**Next available ID: `mlu-000006`.**

### Status values

| Status | Means |
|---|---|
| Reserved | Assigned to an accepted submission that has not been published yet. |
| Published | Live in the repository and listed in the catalog. |
| Withdrawn | Removed from publication. The ID stays listed and is never reissued. |
