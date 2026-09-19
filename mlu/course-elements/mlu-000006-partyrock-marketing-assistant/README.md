# Build and Evaluate an AI Marketing Assistant in PartyRock

**`mlu-000006`** · Course Elements · v1.0.0 · **classroom-tested**

Students build a working marketing-content app in Amazon PartyRock without writing a line of code —
then do the part that actually teaches something. One identical scenario, a campus coffee shop, goes
through three prompt strategies: a bare instruction, a role-and-context prompt, and a fully
structured prompt with an output format and a no-unsupported-claims constraint. Students score all
three against the same five criteria and argue for a winner using their own outputs as evidence.

The app is the hook. **The comparison table is the assignment.**

Built for an 8-week, no-code AI course taken across majors — business to the arts — where the
missing piece was never explanation, it was contact with a working model.

## At a glance

| | |
|---|---|
| **Audience** | Undergraduates in any major; no programming background assumed |
| **Duration** | 1–2 hours of student work (45–60 min build, 30 min comparison) |
| **Delivery** | In person, online asynchronous, or hybrid |
| **Runs on** | Amazon PartyRock in a browser. Nothing to install. |
| **Prerequisites** | A free PartyRock sign-in via Apple, Google, or Amazon. No AWS account, no credit card. |
| **Expected cost** | None |
| **Sample data** | A worked scenario — campus coffee shop, students 18–24 — used throughout, so nobody has to invent a product first |
| **You end with** | A published PartyRock app, three recorded outputs, a completed scoring table, and a 150–250 word reflection |

## Learning outcomes

By the end, a student can:

1. Build a functioning generative-AI application without writing code.
2. Reference app inputs inside a prompt so that outputs change with user input.
3. Compare a bare prompt, a role-and-context prompt, and a structured prompt on one identical
   scenario.
4. Score generative-AI output against relevance, specificity, tone, completeness, and usability
   rather than accepting it at face value.
5. Explain which prompt elements — role, context, tone, constraints, output format — most changed
   the result, citing their own outputs.

## Contents

| Path | What it is |
|---|---|
| [`materials/assignments/marketing-assistant-assignment.md`](materials/assignments/marketing-assistant-assignment.md) | The full assignment: build guide, the three comparison prompts, the scoring table, what to submit, troubleshooting, and a glossary |
| [`materials/assignments/marketing-assistant-assignment.docx`](materials/assignments/marketing-assistant-assignment.docx) | The author's original Word version, for instructors who want to edit and redistribute |
| [`materials/faculty-guide/teaching-notes.md`](materials/faculty-guide/teaching-notes.md) | Why it exists, what changed in the course, the guardrail to say out loud, and how to move the pattern to your discipline |

### The three prompts

| | Strategy | What it is |
|---|---|---|
| **A** | Basic | `Write a marketing advertisement for a coffee shop.` |
| **B** | Role + context | Adds a role, the audience, and the product's actual benefits |
| **C** | Structured | Labeled Task / Audience / Tone / Key benefits / Length, a numbered output format, and *"Do not make claims that are not supported by the information provided."* |

That last clause in Prompt C is the one worth stopping on. Comparing what A invents against what C
refuses to invent is the clearest demonstration of a guardrail most students have never seen written
down.

## How to use it

1. **Download** this contribution — see [Downloading a contribution](../../../README.md#downloading-a-contribution).
2. **Test `partyrock.aws` from a lab machine.** Some campus networks block AWS domains. This is the
   most common day-of failure and the easiest to prevent.
3. **Read [`teaching-notes.md`](materials/faculty-guide/teaching-notes.md)** for the course context
   and the responsible-use point the assignment is built around.
4. **Assign it.** Students work solo or in pairs; pairs tend to produce better comparisons because
   they argue about the scoring.
5. **If time is short, cut Part 2 polish — never Part 3.** The build is not the learning.

## Related

Week 7 of the same course is [`mlu-000007`](../mlu-000007-partyrock-phishing-detector), which takes
the same build-then-evaluate loop into cybersecurity and adds an adversarial round where students
try to fool the tool they just built. Run this one first: it establishes prompt structure before
that one asks students to attack it.

## Reuse and attribution

Documentation is `CC-BY-4.0`. See [`LICENSE.md`](LICENSE.md) and [`CITATION.cff`](CITATION.cff).
No student work or student records appear anywhere in this contribution — the worked scenario is
invented.

Structured metadata for this contribution lives in [`mlu-contribution.yml`](mlu-contribution.yml).
