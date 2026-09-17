# 1-Day Faculty AI Seminar — Plan Summary (v2)

> ## What this contribution ships, and what it does not
>
> **This plan describes a full 9:00–4:00 day. Only the 1:30–3:00 PM afternoon lab is included here.**
> Everything else is either yours to supply or comes from AWS material that is not in this
> repository.
>
> | Block | Time | Included? |
> |---|---|---|
> | Welcome, persona reveal | 9:00–9:15 | Persona table is in this document. **Slides: no.** |
> | Lecture M1 L1 — Intro to Generative AI | 9:15–10:00 | **No.** AWS MLU deck, cherry-picked — see `CONTENT_AUDIT.md` |
> | Lecture M1 L3 — Prompt Engineering | 10:15–11:00 | **No.** AWS MLU deck |
> | Lab 1 — PartyRock | 11:00–12:30 | **No.** AWS "Bootcamp Prep Part 1" PDF |
> | Bridge | 1:15–1:30 | Slide-by-slide spec only — see `BRIDGE_AND_LAB_DECK_SPEC.md` |
> | **Lab 2 — Curriculum Embedding** | **1:30–3:00** | ✅ **Yes — this is the contribution.** Notebooks, data, and a full facilitator track. |
> | Lecture M2 + M3 survey | 3:15–3:45 | **No.** AWS MLU decks |
> | Wrap | 3:45–4:00 | Structure described here; no slides |
>
> **To deliver only the 90-minute lab** — which is what most people will want — you need nothing
> from the rest of this table. Go straight to
> [`INSTRUCTOR_CHEATSHEET.md`](../facilitator-guide/INSTRUCTOR_CHEATSHEET.md), which scripts it
> minute by minute, and [`PREFLIGHT_CHECKLIST.md`](../facilitator-guide/PREFLIGHT_CHECKLIST.md) for
> the morning-of setup.
>
> **To run the whole day**, you must separately obtain the AWS MLU EEP curriculum and the Bootcamp
> Prep PDFs. The links under *Reference* are **not publicly reachable** (HTTP 404 as of 2026-09-17;
> possibly private rather than removed). Budget time to source them, or to substitute your own
> morning content.

**Audience:** Multidisciplinary faculty (Computer Science → Dentistry → Humanities → Business → Health Sciences). All have an institutional mandate to incorporate AI into their teaching.
**Format:** Single day, 9:00 AM – 4:00 PM
**Source material:** [aws-mlu-eep-generative-ai](https://github.com/aws-samples/aws-mlu-eep-generative-ai) (MLU EEP curriculum — 14 lessons, 13 labs across 3 modules)

> **What changed from v1:** The afternoon lab is now a **curriculum-embedding lab**, not a technical RAG lab. The original Lab 2 (technical RAG deep-dive) moved to a standalone post-seminar resource. The new lab's goal: faculty leave with a *written curriculum plan*, not just a generated artifact. See `CONTENT_AUDIT.md` for the reasoning.

---

## Goals

By 4 PM, each participant leaves with:
1. A working **PartyRock app** they built themselves (morning lab)
2. A working **AI tool tailored to their persona's vision** (afternoon lab) — case-study coach, primary-source companion, med-calc drill, etc.
3. **A written curriculum plan** specifying course, week, assignment, what AI does, what the instructor still does, and where AI does NOT belong
4. A **dated Monday morning commitment** to one specific action

---

## What we cover

Of the 14 lessons + 13 labs in the source repo, we have ~5.5 hours of teaching time after breaks.

**Covered in depth:**
- Module 1, Lesson 1 — Intro to Generative AI (selectively — see `CONTENT_AUDIT.md`)
- Module 1, Lesson 3 — Prompt Engineering (first half only)
- Hands-on: PartyRock lesson-plan app (Bootcamp Prep Part 1)
- Hands-on: **Curriculum Embedding Lab** (this repo)

**Surveyed only:**
- Module 2 Lesson 3 — Responsible AI dimensions (cherry-picked slides)
- Module 3 — RAG / Agents / Multimodal (concept only)

**Not covered in seminar:**
- Technical RAG implementation deep-dive → **post-seminar repo** at github.com/aws-dsu/mlu-faculty-ai-seminar-lab
- M1 L2/L4/L5, M2 Labs, M3 Lessons 1–2 + 4–5 → upstream MLU GitHub repo for self-study

---

## Agenda

| Time | Block | Content |
|---|---|---|
| 9:00–9:15 | Welcome | Goals, AI mandate framing, persona reveal |
| 9:15–10:00 | **Lecture: M1 L1** | Intro to Generative AI *(use cherry-picked slides — see CONTENT_AUDIT)* |
| 10:00–10:15 | ☕ Break | |
| 10:15–11:00 | **Lecture: M1 L3** | Prompt Engineering *(first 7 slides — skip inference parameters)* |
| 11:00–12:30 | **🛠 Lab 1: PartyRock** | Build your lesson-plan AI app (Bootcamp Prep Part 1) |
| 12:30–1:15 | 🍽 Lunch | |
| 1:15–1:30 | Bridge | "PartyRock got you started. Now where does this fit in your actual course?" |
| 1:30–3:00 | **🛠 Lab 2: Curriculum Embedding** | This lab — persona-matched tool + curriculum plan |
| 3:00–3:15 | ☕ Break | |
| 3:15–3:45 | **Lecture: M2 + M3 survey** | Responsible AI risks + what's next *(cherry-picked slides)* |
| 3:45–4:00 | Wrap | Pod commitment shares, take-home artifact reminder |

---

## Lab 1 — PartyRock (already designed)

Pulled directly from the existing **"EEP Generative AI Faculty Fellows Bootcamp preparation"** PDF. Participants build a lesson-plan-generator AI app, then iteratively extend it with prompt engineering, Theme/Persona widgets, and grounded references.

**Why first:** No-code on-ramp. Builds confidence for non-technical faculty before any notebook appears.

---

## Lab 2 — Curriculum Embedding (this repo)

**Title:** "Embed AI in Your Course"

**What it does:** Each participant runs a persona-matched AI tool against their discipline's sample document, then writes a structured curriculum plan capturing exactly where in their course the tool fits, what they still teach, and where AI does NOT belong.

**Structure (90 min):**

| Part | Time | Type | Purpose |
|---|---|---|---|
| 0 | 5 min | Setup | Pick your persona |
| 1 | 10 min | Watch-along | Bedrock connection + tool definitions load |
| 2 | 30 min | Hands-on | Run YOUR persona's tool against the sample PDF; see your vision come to life |
| 3 | 20 min | Reflection (EDIT ME cells) | Course / week / assignment / what AI does / what YOU still do / concerns |
| 4 | 10 min | Reflection (EDIT ME cells) | Where AI does NOT belong; protected assignment; student AI policy |
| 5 | 5 min | Instructional | Bridge to Canvas / Blackboard / Moodle |
| 6 | 5 min | Reflection + export | Dated Monday commitment; download artifact |
| 7 | 5 min | Pod share | Cross-discipline pairing; ask "what would you NOT do?" |

**Why this design:** Per `CONTENT_AUDIT.md`, the previous Lab 2 produced impressive AI output but did not bridge to "I will use this Monday." The new lab inverts that: less technical depth, more curriculum embedding. 4 of 6 personas previously walked out without an embedding vision; this lab makes vision the deliverable.

### Pre-flight checklist

- [ ] Bedrock model access enabled per AWS account: `amazon.nova-lite-v1:0`, `amazon.nova-2-multimodal-embeddings-v1:0`
- [ ] SageMaker Studio domain pre-provisioned (kernel cold-starts will eat 5–10 min)
- [ ] Kernels pre-warmed before lunch ends (so 1:30 PM start is instant)
- [ ] **6 sample PDFs sourced, license-checked, and staged in `data/`** (one per persona — see `data/README.md`)
- [ ] Persistent Slack channel created for Part 7 share-outs

### Design decisions (locked)

| # | Decision | Why |
|---|---|---|
| 1 | **One notebook with persona selector** (not 6 separate notebooks) | Single artifact for instructor maintenance |
| 2 | **Six tailored prompt templates** (one per persona) | Generic templates fail 4/6 personas — see CONTENT_AUDIT |
| 3 | **Reflection cells use Python variables**, not markdown | Variables export into the take-home artifact header |
| 4 | **Pre-staged PDFs, BYO optional** | Tested — BYO dependency caused 30%+ of attendees to fail in dry-runs |
| 5 | **Embeddings class in helper file** (`mlu_utils/embeddings.py`) | Removes 30-line wall-of-code that scared non-coders in v1 lab |
| 6 | **Watch-along framing for Part 1** | Explicit "instructor runs, you watch" reduces non-coder panic |
| 7 | **Part 4 (where AI does NOT belong) is mandatory** | Skeptic conversion mechanism; missing in v1 lab |
| 8 | **Export artifact bundles AI output + curriculum plan** | Single take-home document; commitment lives at the top |

---

## Faculty Personas

Six personas to print as handouts and project during the 9:15 welcome. Each attendee identifies the closest match at registration so we can pre-stage their sample PDF and group them at lunch.

| # | Persona | Field | AI Comfort | Tool they build in Lab 2 |
|---|---|---|---|---|
| 1 | Dr. Maya Patel | Dentistry — Periodontics | Cautious | Case Study Coach (3-level patient vignettes) |
| 2 | Prof. James Chen | Computer Science — Data Structures | High | Code Critique Generator (Socratic prompt template) |
| 3 | Dr. Sarah Whitman | English — Victorian Lit | Skeptical | Primary Source Companion (no-plot-summary prompts) |
| 4 | Prof. Diane Okafor | Nursing — Pharmacology | Moderate | Med-Calc Drill (dosing problems with safety red-flags) |
| 5 | Dr. Marcus Reyes | Business — Leadership MBA | Enthusiastic | Stakeholder Roleplay (AI plays CFO/CMO from case) |
| 6 | Dr. Lena Hoffmann | Biology — Cell Bio Lab | Low | Pre-Lab Knowledge Gate (quiz students must pass) |

> **Instructor demo lead:** Start with **Persona 1 (Dentistry)** or **Persona 4 (Nursing)**. Clinical use cases create the strongest "if it works for them, it works for me" momentum in a mixed room.

Full persona stories with vision statements and pain points: the table above, plus the persona briefs inside the notebook's Part 1. A separate one-page-per-persona deck was discussed but never produced, and is not required.

---

## Risks & mitigations

| Risk | Mitigation |
|---|---|
| SageMaker kernel cold-start eats lab time | Pre-warm kernels before lunch ends |
| Non-coder panic at first notebook cell | "Watch-along" framing in Part 1; embeddings class hidden in helper file |
| Faculty fill reflection cells with vague platitudes | Instructor walks the room during Part 3; nudges toward specifics with worked examples |
| Skeptics (Persona 3) check out | Part 4 ("where AI does NOT belong") gives skeptics a place to land |
| Bedrock cost overrun | Default to Nova Lite (frugal); PDFs capped at ~50 pages |
| Running over time | Lecture blocks compress, not the lab. Lab 2 reflection cells (Parts 3-4) are the protected core. Cut Part 5 (LMS bridge) first if needed. |
| Faculty don't actually email themselves the commitment | Instructor models it live at 3:00 — opens email, sends to self, projects |

---

## Decisions — settled since this plan was drafted

Recorded so nobody re-opens them.

| Question | Answer |
|---|---|
| Sample-PDF sourcing — personas 3–6 still needed? | **No longer open. All six ship**, licence-checked, in `../activities/curriculum-embedding-lab/data/`, with per-file source and page count in that folder's `README.md`. The note below about "~2 hr each" is obsolete. |
| Standalone Lab 2 framing | **Done.** The technical RAG lab is now [`mlu-000002`](../../../mlu-000002-discipline-assistant-seminar), published separately with its own README and facilitator track. |
| Persona handouts | **Not produced, and not needed.** The persona table below is sufficient to project at 9:15 or print. Treat a separate handout deck as optional polish, not a prerequisite. |

## Still for the hosting institution to decide

These genuinely depend on who is running the session.

1. **Persona selection** — keep all six, or trim to the disciplines actually in the room. Six is the
   default and needs no preparation; trimming only means projecting fewer rows.
2. **Bridge segment (1:15–1:30)** — who delivers it. The framing is specified:
   *"PartyRock got you started; now decide where this actually fits in your course."*
   `BRIDGE_AND_LAB_DECK_SPEC.md` has the slide-by-slide content and speaker notes.
3. **Morning lecture slides** — only if you are running the full day. Per `CONTENT_AUDIT.md`, the
   AWS MLU decks carry roughly 9 useful slides in 23 for a non-CS audience, so someone has to trim
   them. Not needed to deliver the lab alone.
4. **Post-seminar follow-up** — office hours, a curriculum review, a shared channel, or nothing.
5. **Where share-outs happen** — this plan assumes a Slack channel. Any shared channel works, and so
   does a round-the-room verbal share. Nothing in the notebook depends on it.

---

## Reference

- **This lab** (curriculum embedding): this contribution — `mlu-000001-curriculum-embedding-lab`
- **Post-seminar deep-dive** (technical RAG): [`mlu-000002-discipline-assistant-seminar`](../../../mlu-000002-discipline-assistant-seminar) in this repository *(the old standalone `github.com/aws-dsu/...` location is no longer reachable)*
- **Source curriculum**: [aws-samples/aws-mlu-eep-generative-ai](https://github.com/aws-samples/aws-mlu-eep-generative-ai)
- **Bootcamp Prep Part 1 PDF**: PartyRock workshop (used directly as Lab 1)
- **Bootcamp Prep Part 2 PDF**: Research Assistant building (reference material, not delivered)
- **Audit findings**: `instructor/CONTENT_AUDIT.md`
