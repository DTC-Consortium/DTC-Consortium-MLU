# The four apps — what you must build before you can deliver this session

> ## Read this first
>
> **This session demonstrates four AI apps. None of them ships with this contribution.**
>
> `TALK_TRACK.md`'s morning-of checklist says *"Apps published and shared with every attendee
> account"* as though they already exist. For the original delivery they did. For you they do not,
> and **you cannot run this session until you build them.**
>
> This document collects every requirement the talk track and the deck actually depend on, so you
> are rebuilding against a spec rather than guessing. Where the original is genuinely
> under-specified, it says so rather than inventing a detail.

## What you are building, and where

| # | App | Platform | Room does | Session time |
|---|---|---|---|---|
| 1 | **Rubric Builder** | Amazon Quick | Hands-on | 0:18–0:36 |
| 2 | **AI-Proofing Assistant** | Amazon Quick | Hands-on | 0:36–0:46 |
| 3 | **Grading Assistant** | **Kiro** | Watches | 0:46–0:59 |
| 4 | **Pre-Assessment Triage** | Amazon Quick — an *extension* of app 3's Quick equivalent | Hands-on | 0:59–1:22 |

Everything they operate on is in [`../activities/sample-pack/`](../activities/sample-pack). The
rubric interchange format is [`../activities/rubric-format.md`](../activities/rubric-format.md)
(`mlu-rubric/1`) — build to it and a rubric moves between all four apps, and loads unchanged into
[`mlu-000004`](../../../../ml-ai-applications/mlu-000004-paper-autograder).

---

## 1. Rubric Builder

**Input:** an assignment prompt plus its learning objectives, as text.
**Output:** a rubric in `mlu-rubric/1` format — both `.json` and `.md`.

**Required behaviour**

- Produces weighted criteria, each with **distinguishing descriptors per tier** — not point ranges.
  The weak rubric fails precisely because it has ranges without descriptors.
- Includes a **correctness criterion tied to the course reading**, not to the model's general sense
  of the topic. Slide 10 has you point at this in the output.
- Emits a **`present when` line per criterion**. Tool 4 reads these and nothing else, so they must
  be self-contained.
- Criteria map to the stated learning objectives.
- Has a **Stress Test tab**: run one paper against two rubrics and show the grades side by side.

**The demo that must work (slide 11).** Marcus Lee against `rubric-weak.md` → roughly **B+**.
Marcus Lee against `rubric-golden.json` → **F**. If your build does not reproduce that gap, the
session has no spine. Test it before anything else.

**Reference output:** `../activities/sample-pack/rubric-golden.json` is what good looks like.

---

## 2. AI-Proofing Assistant

**Input:** an assignment prompt and a rubric.
**Output:** flags identifying requirements a general chatbot could satisfy with no knowledge of the
course.

**Required behaviour**

- Flags per requirement, with a reason.
- Suggests changes that make the assignment **need the course** — its reading, its discussion, the
  student's own process.
- Framing to preserve: the goal is *not* to make cheating impossible.

> **⚠️ This app is the least specified of the four.** `TALK_TRACK.md` slide 15 carries the original
> author's own note: *"Update these steps to match the final AI-Proofing app before rehearsal."*
> That means the app was still changing when the talk track was written. Build it, then **rewrite
> slide 15's steps to match what you built.**

---

## 3. Grading Assistant — built in Kiro

Built in **Kiro**, not Quick, and the room **watches**. That is the point: the contrast between
Quick's describe-then-fix loop and Kiro's approve-requirements-then-design-then-tasks loop *is* the
teaching content of this segment.

**You must have a `requirements.md` to project** (slide 17). It needs at least two requirements,
one testable and one deliberately not — the original uses "grades fairly," and the room's job is to
spot that "fairly" has no pass or fail. Keep a deliberately untestable requirement in yours.

**Three design decisions the talk track names (slide 18) — build all three:**

1. **The math is in code.** The model picks a 0–4 tier per criterion; the weighted grade is
   *calculated*, never generated. Grades must be exactly reproducible.
2. **Correct means correct per the course reading.** This is why Marcus fails.
3. **Everyone is accounted for.** Diego Alvarez, who submitted nothing, is flagged **missing** —
   never given a silent zero.

The line to land: *"The model judges. The code counts. The instructor decides."*

**Expected output on the sample (slide 19):** Marcus **F**, with his wrong claims quoted back as
evidence. Diego **missing**. Leila roughly **50%**. Every result framed as a draft for review.

> `mlu-000004` already implements all three decisions against the same sample data, including the
> weighted-grade-in-code rule. Read its `mlu_utils/paper_tools.py` before you build this — not to
> copy it, but because the behaviour you need is already worked out there.

---

## 4. Pre-Assessment Triage

Not a separate app: an **extension of the grading app**, applied live in the Quick builder view by
pasting one line (slide 21). Build it as an extension so the room sees that happen.

**Required behaviour**

- Returns **Present / Partial / Missing** per criterion, each with the quote it is based on.
- **Never a score. Never a rewrite.** Those limits are the design, not a shortfall (slide 23).
- Reads **only the `present when` lines** — never the weights — so it structurally lacks the
  information to compute a grade. Say this out loud.

**Expected outputs**

| Student | Result | Why it is in the session |
|---|---|---|
| Priya Chandra | Missing ×3, Partial ×1 | Surfaces a failing draft a week early |
| Leila Haddad | Present / Partial / Partial / Missing / Partial | What *Partial* looks like |
| Marcus Lee | Mostly **Present** | **The honest limit.** Triage passes him — *present is not correct* |

Marcus passing triage is a feature. Slide 23 depends on it.

**You must prepare two copies:** the one you extend live, and a **pre-extended fallback**. The talk
track is explicit — if the live build has not finished after two minutes, switch. Do not wait on
stage.

---

## Before you rehearse

- [ ] All four built, published, and shared with every attendee account
- [ ] Marcus: ≈B+ on the weak rubric, **F** on the golden rubric
- [ ] Marcus: **F** in the grading app, wrong claims quoted as evidence
- [ ] Marcus: mostly **Present** in triage
- [ ] Diego: **missing**, not zero
- [ ] Priya: **Missing ×3** in triage
- [ ] Pre-extended triage fallback published and reachable
- [ ] Kiro `requirements.md` ready to project, with one untestable requirement in it
- [ ] Kiro grader already run once with results saved, in case the live run is slow
- [ ] Slide 15's steps rewritten to match the AI-Proofing app you actually built
- [ ] **Recorded outcomes replace the predictions** in `../activities/sample-pack/README.md` — they
      are hand-scored estimates, not results

## A note on scope

Rebuilding four apps is not a small job, and it is the reason this contribution is published at
**pilot** maturity rather than classroom-tested. Budget for it honestly. The deck, talk track,
handout, and sample pack are complete and rehearsable; the apps are the gap.
