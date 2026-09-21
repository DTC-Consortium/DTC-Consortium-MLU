# The prompt pack

**Nothing in this session is pre-built.** Attendees build three of the four tools themselves, in
the room, by pasting a prompt into Amazon Quick. The facilitator builds the fourth in advance and
the room watches.

That is a deliberate change from the original delivery, which assumed four apps already existed
and were shared with every attendee's account. Prewritten prompts plus the assets, handed over on
a QR code, is how these workshops have always worked — and it is what attendees can actually take
home. An app shared to an account they lose access to is not something they keep. A prompt is.

---

## What's here

| # | Prompt | Who builds it | Session slot | Slide |
|---|---|---|---|---|
| 1 | [Rubric Builder](PROMPT-1-rubric-builder.md) | **Attendees** | 0:24–0:36 | 13 |
| 2 | [AI-Proofing Assistant](PROMPT-2-ai-proofing.md) | **Attendees** | 0:36–0:46 | 15 |
| 3 | [Pre-Assessment Triage](PROMPT-3-triage.md) | **Attendees** | 1:07–1:22 | 24, 25 |
| F1 | [Grading Assistant — Quick](facilitator/PROMPT-F1-grading-app.md) | Facilitator, in advance | 0:59–1:05 | 21, 22 |
| F2 | [Grading Assistant — Kiro](facilitator/PROMPT-F2-kiro-grader.md) | Facilitator, in advance | 0:46–0:59 | 17, 18, 19 |

**What attendees actually see is one document**, not these five files.
[`MASTER-FOLLOW-ALONG.md`](MASTER-FOLLOW-ALONG.md) is the source for it: the paper, the rubric,
the assignment, the objectives and prompts 1–3, in the order the session runs, so nobody
navigates between documents while the clock is running. The files here stay as the per-tool
reference — what each prompt is for, and what it must produce before you rehearse.

**F1 and F2 are facilitator-only** and never go in the folder — see
[DRIVE-FOLDER.md](DRIVE-FOLDER.md).

## How each prompt is laid out

The same three parts every time, because the middle one gets read aloud while people work:

1. **What to do** — the numbered steps. These used to be on slides 13, 15 and 25; they were
   removed from the deck so they can be revised without going back to legal.
2. **The prompt** — one fenced block, copied whole and pasted into Quick's *describe your app*
   box. Nothing outside the block gets pasted.
3. **Before you deliver: prove it works** — the outputs the build must produce on the sample
   pack. Not optional. The session's argument is three specific numbers, and a build that misses
   them looks fine and teaches nothing.

## The three results the session cannot lose

Everything else can compress. These cannot:

| # | Result | Where it lands |
|---|---|---|
| 1 | Marcus scores **≈88 (B+)** on the weak rubric and **F** on the generated one | Slide 11 |
| 2 | The grader marks Diego **missing**, not zero | Slide 18 |
| 3 | Triage returns **Present** for Marcus's running-time section | Slide 23 |

Number 3 is the one that looks like a bug. It is the session's closing argument: *present is not
the same as correct.* A build that "fixes" it has broken the session.

## The rubric is the thread

The rubric prompt 1 writes is the rubric prompts 2 and 3 read, in the
[`mlu-rubric/1`](../activities/rubric-format.md) format. That is the thing to protect when you
revise a prompt: change the format in one and the other two stop working, quietly, in the room.

Triage reads **only** each criterion's `present_when` line — never `weight`, never `levels`. That
is not a simplification, it is the guarantee: it cannot produce a grade because it is never given
the parts a grade is made from.

## If you change a prompt

The steps live here, not in the deck, precisely so you can. Change the prompt, change the steps
above it, reprint the card, re-run the "prove it works" table. Nothing in the deck moves and
nothing goes back to legal.

The one thing to keep is what the tools **refuse** to do. Triage's refusals are most of its
prompt, and they are what makes it something you can put in front of students.
