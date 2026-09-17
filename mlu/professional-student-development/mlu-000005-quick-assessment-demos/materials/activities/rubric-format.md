# Rubric Format — `mlu-rubric/1`

One rubric format shared by all four tools in the session. The Rubric Builder writes it; the
AI-Proofing Assistant, the Grading Assistant, and Pre-Assessment Triage read it. A rubric in this
format also loads unchanged into `mlu-paper-autograder` (`paper_tools.load_rubric` accepts `.json`
and ignores the extra fields).

Every rubric ships as two files with the same content:

- **`.json`** — for tools. The source of truth.
- **`.md`** — for people, and for pasting into a Quick app or a chat window.

The worked example is `sample-pack/rubric-golden.json` / `.md`.

---

## Shape

```json
{
  "format": "mlu-rubric/1",
  "title": "Choose the Right Structure — short paper",
  "assignment": "assignment.md",
  "course_material": "persona2_cs_data_structures.pdf",
  "max_tier": 4,
  "grade_bands": [[93, "A"], [90, "A-"], [87, "B+"], "…", [0, "F"]],
  "criteria": [
    {
      "id": "running-time",
      "name": "Correctness of Running-Time Analysis",
      "weight": 35,
      "objective": "LO2",
      "description": "One line on what the criterion measures.",
      "present_when": "What must be on the page for this criterion to count as attempted.",
      "levels": { "4": "…", "3": "…", "2": "…", "1": "…", "0": "…" }
    }
  ]
}
```

## Fields

| Field | Required | Meaning |
|---|:---:|---|
| `format` | ✓ | Always `"mlu-rubric/1"`. Lets a tool reject a file it can't read. |
| `title` | ✓ | Shown to students. |
| `assignment` | | The assignment the rubric belongs to — a filename or a short description. |
| `course_material` | | The reading "correct" is judged against. Correctness criteria mean nothing without it. |
| `max_tier` | ✓ | Top of the scale. Always `4` in this session: levels run 0–4. |
| `grade_bands` | | `[percent_floor, letter]` pairs, highest first. Omit to use the grader's default. |
| `criteria[].id` | ✓ | Stable slug. Tools line up scores by `id`, so renaming a criterion doesn't break anything. |
| `criteria[].name` | ✓ | Shown to students. |
| `criteria[].weight` | ✓ | Relative weight. Doesn't have to sum to 100 — tools normalize. |
| `criteria[].objective` | | The learning objective this criterion evidences (`LO1`…). A rubric with no criterion for an objective isn't assessing it. |
| `criteria[].description` | ✓ | One line: what the criterion measures. |
| `criteria[].present_when` | ✓ | What has to be on the page for the criterion to count as **attempted** — not done well, just there. Written as observable features, never as quality judgments. |
| `criteria[].levels` | ✓ | One descriptor per tier, `"0"` through `"max_tier"`. Keys are strings (JSON requires it). |

## Which tool reads what

| Field | Rubric Builder | AI-Proofing | Grading Assistant | Triage |
|---|:---:|:---:|:---:|:---:|
| `name`, `description` | writes | reads | reads | reads |
| `objective` | writes | reads | — | — |
| `present_when` | writes | reads | — | **reads** |
| `weight`, `levels`, `grade_bands` | writes | reads | **reads** | **never reads** |

**Triage never reads `weight`, `levels`, or `grade_bands`.** That's deliberate, and it's the
strongest guarantee it can't produce a score: it doesn't have the information to calculate one.

## Triage statuses

Triage compares each criterion's `present_when` with the draft:

| Status | Meaning |
|---|---|
| **Present** | Everything `present_when` asks for is on the page. |
| **Partial** | Some of it is on the page. |
| **Missing** | None of it is on the page. |

Each status comes with the quoted passage it rests on, or "no passage found" for Missing. A
**Present** status says nothing about whether the content is correct — Marcus's running times are
present and wrong.

## Rules for writing `present_when`

- **Observable, not evaluative.** "Gives a big-O running time for the operation in two structures"
  — not "analyzes running time well."
- **Countable where possible.** "At least one," "in the recommended structure and one alternative."
- **One job.** If it contains "and also," split the criterion.
