# Project O.R.A.C.L.E. — A GenAI-Enhanced International Relations Lab

**`mlu-000009`** · Course Elements · v1.0.0 · **classroom-tested**

*Organized Reports and Analysis for Contact with Life Elsewhere.*

International Relations students have a STEM gap that has nothing to do with math: they have no
laboratory. Unlike their peers in the sciences, they get no interactive, experiential space to test
a theoretical framework against evidence and find out where it breaks. This 1-credit lab module
builds one.

The vehicle is a fictional 2025 alien-contact scenario — a benign fleet that bypasses secretive
governments to ask classrooms how humans make sense of things. Students are cast as **"non-expert
but educated analysts,"** a role that is doing real work: it makes the student's own reasoning the
object of study rather than an inferior substitute for an expert's.

**What it is built against is fluent-but-shallow AI output** — writing that is grammatically
impeccable, perfectly formatted, and carries no new evidence or genuine depth. Lab 1 makes students
find where the LLM fails. Lab 2 has them build a PartyRock app that works around those limits. The
module ends where AI cannot follow: a one-on-one oral defense where a student explains their
research design and their own AI use to a person who will ask follow-up questions.

## At a glance

| | |
|---|---|
| **Audience** | Undergraduate IR students at community-college level; designed for non-STEM majors |
| **Duration** | A 6-week lab intensive series inside a 1-credit-hour laboratory course |
| **Delivery** | In person, instructor-led |
| **Runs on** | PartyRock plus any major LLM, in a browser. Nothing to install. |
| **Prerequisites** | Concurrent or prior IR coursework; free PartyRock and LLM accounts; your institution's academic-integrity policy |
| **Expected cost** | None beyond tuition and fees |
| **Sample data** | The alien-contact scenario and mission brief are the fabricated case; students supply their own research questions |
| **You end with** | A 1,200–1,600 word research design, a documented AI usage trail, and a 20–30 minute oral defense |

> ## ⚠️ This is a scaffolding template, not a turnkey lab
>
> The author is explicit about this, and it is the honest frame for adopting it. Two things follow:
>
> **1. It was designed against spring-2025 LLMs.** Specific prompts, model capabilities, and costs
> have moved since. Re-test everything before you deliver it; treat the *structure* as the
> contribution, not the prompts.
>
> **2. The design notes are working notes.** Several fields in the per-practical grid read "Not
> specified," and the Lab Intensive 2 session outlines were never written. The capstone project, the
> rubrics, and the delivered slide decks are complete; the surrounding lab-by-lab plan is a design
> rationale to adapt from.

## Learning outcomes

By the end, a student can:

1. Apply IR theories and approaches to a focused question concerning an extraterrestrial encounter.
2. Develop and communicate a research design reflecting academic reasoning, data–method fit, and
   awareness of bias.
3. Describe the basic functions of general LLMs and express their limitations for academic work.
4. Use GenAI tools ethically to support idea generation, literature identification, and clarity —
   and document that use.
5. Evaluate the strengths and limitations of GenAI's role in social-science research.
6. Reflect on the utility of GenAI in their academic, professional, or personal futures.

## Contents

| Path | What it is |
|---|---|
| [`materials/assignments/lab-project.md`](materials/assignments/lab-project.md) | **The capstone.** Five required research-design sections, two submission tracks, the oral-defense format, both rubrics, and the five defense prompts |
| [`materials/lectures/`](materials/lectures) | Slide decks for Lab Intensive 1 (both sessions) and Lab Practical 1 |
| [`materials/references/pre-lecture-international-society.pdf`](materials/references/pre-lecture-international-society.pdf) | Pre-lecture reading on Hedley Bull's three traditions — the theory Lab Practical 1 runs on |
| [`materials/references/partyrock-apps.md`](materials/references/partyrock-apps.md) | The instructor-built PartyRock apps the labs use, with a caution about hosted-app drift |
| [`materials/references/oacc-workforce-readiness-non-stem-genai.pdf`](materials/references/oacc-workforce-readiness-non-stem-genai.pdf) | The author's conference presentation on the problem this module addresses |
| [`materials/faculty-guide/course-design-notes.md`](materials/faculty-guide/course-design-notes.md) | The 16-week schedule and per-practical design grid. Working notes — read its preamble first |

### The design move worth stealing

**Two tracks, one deliverable.** Every student writes the same research design paper. What differs
is how they got there, and what they must therefore disclose:

| | **Bot-Build track** | **Human track** |
|---|---|---|
| How the design is produced | In PartyRock, by building and refining an app | Written in the student's own words, with GenAI support |
| Transparency artifact | **App Snapshot** — the app's visible workflow *is* the usage log | **AI Usage Log** — a table of tool, task, prompt, and revision rationale |
| Also required | Prompts appendix, references | Prompts appendix, references |

This sidesteps the unenforceable question — *did you use AI?* — and replaces it with an answerable
one: *show me how.* Both tracks then meet the same oral defense, where the rubric scores ethical
reasoning and verification alongside the design itself, and where the prompts appendix is graded on
**usefulness, not quantity**.

## How to use it

1. **Download** this contribution — see [Downloading a contribution](../../../README.md#downloading-a-contribution).
2. **Read [`lab-project.md`](materials/assignments/lab-project.md) first.** It is the most complete
   artifact here and the clearest picture of what the module produces.
3. **Open each [PartyRock app](materials/references/partyrock-apps.md) and run it** against your own
   scenario. Hosted apps drift; assume nothing works until you have seen it work.
4. **Swap in your own institution's integrity policy.** The labs reference OCCC policies 4016 and
   5076 directly, and that reference is load-bearing — the ethics sessions are built on a document
   students can be held to.
5. **Adapt the scenario if you need to.** The alien-contact framing is doing a specific job — it
   puts every student at the same starting distance from the evidence, where no one can lean on
   prior expertise. Any scenario with that property will work.
6. **Budget the defense time.** 20–30 minutes per student is the real scheduling constraint, and it
   is also the part that makes the rest of it assessable.

## Related

[`mlu-000010`](../../ml-ai-applications/mlu-000010-assignment-defender) is the same author's
faculty-facing tool for the inverse problem: rather than teaching students to use AI honestly, it
analyses how easily AI could satisfy an assignment and suggests redesigns.

## Reuse and attribution

Documentation is `CC-BY-4.0`; PartyRock app logic is `MIT`. See [`LICENSE.md`](LICENSE.md) and
[`CITATION.cff`](CITATION.cff).

No real student records, papers, or transcripts appear anywhere in this contribution. The alien
encounter narrative and all associated data are fabricated educational prompts.

Structured metadata for this contribution lives in [`mlu-contribution.yml`](mlu-contribution.yml).
