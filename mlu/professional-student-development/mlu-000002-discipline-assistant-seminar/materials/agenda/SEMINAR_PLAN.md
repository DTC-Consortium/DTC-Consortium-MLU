# 1-Day Faculty AI Seminar — Plan Summary (v1, superseded)

> ## ⚠️ Read this before using this document
>
> **This is the original v1 day-plan, from when this lab was the seminar's 1:30–3:00 PM afternoon
> session. It has been superseded.** In the current plan, the afternoon slot belongs to the
> [Curriculum Embedding Lab](../../../mlu-000001-curriculum-embedding-lab), and *this* lab moved to
> a standalone, post-seminar resource.
>
> **For the current day-plan, use
> [`mlu-000001`'s SEMINAR_PLAN.md](../../../mlu-000001-curriculum-embedding-lab/materials/agenda/SEMINAR_PLAN.md).**
> The two documents describe the same 1:30–3:00 slot differently; that one is authoritative.
>
> This document is kept because its persona table, risk list, and framing are still useful
> background for anyone delivering this lab. **Do not run a day from it.**

## How this lab is actually delivered now

| Mode | Time | What it looks like |
|---|---|---|
| **Self-paced** | ~10–15 min | A participant opens the notebook and runs it alone. This is the figure quoted in the contribution README. |
| **Facilitated lab** | ~90 min | An instructor drives Parts 1–2, participants drive Parts 3–4, everyone shares in Part 5. This is what [`INSTRUCTOR_CHEATSHEET.md`](../facilitator-guide/INSTRUCTOR_CHEATSHEET.md) scripts, on a 1:30–3:00 clock. |

Both are valid. The notebook is the same; only the pacing and the amount of instructor talk differ.
Pick the mode before you read the cheatsheet, because its timings assume the facilitated one.

**Two delivery paths, and they are not interchangeable for setup:**

- **Google Colab + Hugging Face** — no AWS account. The recommended path, because most faculty lose
  cloud access when a seminar ends. See [`PREFLIGHT_CHECKLIST.md`](../facilitator-guide/PREFLIGHT_CHECKLIST.md).
- **SageMaker Studio + Bedrock** — what the v1 plan below assumes throughout.

---

**Audience:** Multidisciplinary faculty (Computer Science → Dentistry → Humanities → Business → Health Sciences). All have an institutional mandate to incorporate AI into their teaching.
**Format:** Single day, 9:00 AM – 4:00 PM
**Source material:** [aws-mlu-eep-generative-ai](https://github.com/aws-samples/aws-mlu-eep-generative-ai) (MLU EEP curriculum — 14 lessons, 13 labs across 3 modules) — **this repository is not public; see the note under Reference.**

---

## Goals

By 4 PM, each participant leaves with:
1. A working **PartyRock app** they built themselves
2. A working **SageMaker Studio notebook** grounded in *their own* discipline's content
3. A persona-based template for how AI fits into their existing course
4. Confidence to explain Responsible AI risks to their department

---

## What we can realistically cover

Of the 14 lessons + 13 labs in the source repo, we have ~5.5 hours of teaching time after breaks. We deliberately **trade breadth for depth + hands-on**.

**Covered in depth:**
- Module 1, Lesson 1 — Intro to Generative AI
- Module 1, Lesson 3 — Prompt Engineering (foundation for both labs)
- Hands-on: PartyRock lesson-plan app (Bootcamp Prep Part 1)
- Hands-on: SageMaker Studio RAG app (adapted from existing M3 Lab 3a)

**Surveyed only (no hands-on):**
- Module 2 — Responsible AI (Evaluating LLMs, key risks)
- Module 3 — What's next (RAG concept, Agents, Multimodal)

**Not covered:** M1 L2/L4/L5, M2 labs, M3 Lessons 1–2 + 4–5, all other labs. We point participants to the GitHub repo for self-study.

---

## Agenda

| Time | Block | Content |
|---|---|---|
| 9:00–9:15 | Welcome | Goals, AI mandate framing, persona reveal |
| 9:15–10:00 | **Lecture: M1 L1** | Intro to Generative AI |
| 10:00–10:15 | ☕ Break | |
| 10:15–11:00 | **Lecture: M1 L3** | Prompt Engineering (with M1 L2 concepts woven in) |
| 11:00–12:30 | **🛠 Lab 1: PartyRock** | Build your lesson-plan AI app (Bootcamp Prep Part 1) |
| 12:30–1:15 | 🍽 Lunch | |
| 1:15–1:30 | Bridge | PartyRock → SageMaker: when do you outgrow the UI? |
| 1:30–3:00 | **🛠 Lab 2: SageMaker Studio** | Discipline-specific RAG tutor (adapted M3 Lab 3a) |
| 3:00–3:15 | ☕ Break | |
| 3:15–3:45 | **Lecture: M2 + M3 survey** | Responsible AI risks + RAG/Agents/Multimodal demo |
| 3:45–4:00 | Wrap | Pod share-outs, self-study roadmap |

---

## Lab 1 — PartyRock (already designed)

Pulled directly from the existing **"EEP Generative AI Faculty Fellows Bootcamp preparation"** PDF. Participants build a lesson-plan-generator AI app, then iteratively extend it with prompt engineering, Theme/Persona widgets, and grounded references.

**Why first:** No-code on-ramp. Builds confidence for non-technical faculty before we touch a notebook.

---

## Lab 2 — SageMaker Studio (new, but ~90% built)

**Title:** "Build a Discipline-Specific AI Teaching Assistant"

**What it does:** Each participant uploads a document from their own discipline (syllabus, case study, lab protocol, primary source, etc.) into a SageMaker Studio notebook. The notebook walks them through:

1. Notebook tour + Bedrock SDK basics *(instructor-led, 15 min)*
2. Direct prompting via code — same as PartyRock but you can see the wires *(hands-on, 15 min)*
3. Upload your document → RAG Q&A grounded in that document *(hands-on, 35 min)*
4. Generate an assessment or study guide from the document *(hands-on, 20 min)*
5. Pod share-out *(5 min)*

**Why second:** Shows the code underneath PartyRock, demonstrates *grounding* (no hallucination) which is the #1 faculty concern, and produces something they can actually adapt for their class.

### Doability check ✓

Every component of Lab 2 already exists in the source repo as a working notebook. We are **composing**, not building from scratch:

| Lab 2 Section | Source Notebook |
|---|---|
| Notebook tour / Bedrock setup | `M1/Lab-2/lab2a-introduction-to-amazon-bedrock.ipynb` |
| Direct prompting, model swap | `M1/Lab-2/lab2b-chat_amazon_bedrock.ipynb` |
| PDF upload + chunking + embeddings + FAISS vector store + RAG Q&A | `M3/Lab-3/lab3a-retrieval_augmented_generation.ipynb` |
| Assessment generation | Repurposes M3 Lab 3a quiz section |

**Work required by instructors:**
- Fork `lab3a-retrieval_augmented_generation.ipynb`
- Swap the demo PDF (`transformers_paper.pdf`) for participant-provided documents
- Replace demo queries with discipline-agnostic prompt templates (quiz / study guide / rubric)
- Stage 4–6 sample PDFs in `data/` as fallback for anyone who didn't bring material
- **Estimated effort: 2–4 hours of notebook editing**

### Pre-flight checklist

- [ ] Bedrock model access enabled per AWS account: `amazon.nova-lite-v1:0`, `amazon.nova-2-multimodal-embeddings-v1:0`, `mistral.mixtral-8x7b-instruct-v0:1` (for Part 2 model swap)
- [ ] SageMaker Studio domain pre-provisioned (kernel cold-starts will eat 5–10 min otherwise)
- [ ] Kernels pre-warmed before lunch ends (so 1:30 PM start is instant)
- [ ] **6 sample PDFs sourced, license-checked, and staged in `data/`** (one per persona — see catalog below)
- [ ] Persistent Slack channel created for Part 5 share-outs (lives beyond seminar)

### Lab 2 — Locked design decisions

| # | Part | Decision |
|---|---|---|
| 1 | Part 1 (Notebook Tour) | **Watch only** — instructor screen-shares; non-coders don't click along |
| 2 | Part 2 (Direct Prompting) | Model swap: **Nova Lite vs Mistral Mixtral** *(Anthropic Claude not enabled in MLU training accounts)* |
| 3 | Part 2 (Direct Prompting) | **Pre-fill** the prompt cell with a fun seed (haiku about your field) |
| 4 | Part 3 (Upload + RAG) | **Provide 6 sample PDFs** (one per persona). BYO is optional only. |
| 5 | Part 3 (Upload + RAG) | PDF size cap: **~50 pages** |
| 6 | Part 4 (Take It Home) | Show **all 3 prompt templates** (quiz, study guide, rubric) |
| 7 | Part 4 (Take It Home) | Include a **final cell that exports AI output to PDF/markdown** |
| 8 | Part 5 (Share-out) | Share-outs land in a **persistent Slack channel** |

### Sample PDF catalog (to source)

Public-domain or CC-licensed only. Don't use Harvard Business cases or copyrighted textbooks — sets a bad example for faculty.

| Persona | Sample document | Length | Suggested source |
|---|---|---|---|
| 1. Dentistry | Clinical periodontal case study | 15–25 pp | PubMed Central open access, LibreTexts Dental |
| 2. Computer Science | Data structures chapter | 20–30 pp | "Open Data Structures" (Pat Morin, CC-BY), MIT OCW |
| 3. English Literature | Victorian primary source essay/short story | 10–20 pp | Project Gutenberg (Seacole, Dickens, Wilde) |
| 4. Nursing | Pharmacology chapter / drug class | 15–25 pp | OpenStax "Pharmacology for Nurses," LibreTexts Medicine |
| 5. Business | Open-access leadership case | 10–20 pp | MIT OCW Sloan, IIMA/Ivey free cases |
| 6. Biology | Real lab protocol | 8–15 pp | OpenStax Bio lab manual, JoVE open protocols |

**Naming convention:** `data/persona1_dentistry_perio_case.pdf` (self-documenting).
**Instructor demo PDF:** Lead with Persona 1 (Dentistry) — clinical reasoning creates the strongest "wow, this could work for me too" moment in a mixed room.

---

## Faculty Personas

Six personas to print as handouts and project during the 9:15 welcome. Each attendee identifies the closest match at registration so we can pre-stage their sample PDF and group them at lunch.

| # | Persona | Field | AI Comfort | Key PartyRock Use | Key SageMaker Use |
|---|---|---|---|---|---|
| 1 | Dr. Maya Patel | Dentistry — Periodontics | Cautious | Case-study coach | RAG-grounded clinical reasoning Q&A |
| 2 | Prof. James Chen | Computer Science — Data Structures | High | "Code Critique" (no answers) | Textbook-grounded TA bot |
| 3 | Dr. Sarah Whitman | English — Victorian Lit | Skeptical | Primary-source discussion prompts | Citation-grounded close-reading tool |
| 4 | Prof. Diane Okafor | Nursing — Pharmacology | Moderate | Med-calc drill app | Formulary-grounded practice tool |
| 5 | Dr. Marcus Reyes | Business — Leadership MBA | Enthusiastic | Case-prep companion | Stakeholder roleplay simulator |
| 6 | Dr. Lena Hoffmann | Biology — Cell Bio Lab | Low | Pre-lab knowledge gate | Protocol-grounded Q&A |

> **Instructor tip:** Lead the SageMaker demo with **Persona 1 (Dentistry)** or **Persona 4 (Nursing)**. Clinical examples create stronger "if it works for them, it works for me" momentum in a mixed room than CS demos.

Full persona stories with vision statements and pain points are in the table above. A separate one-page-per-persona handout deck was discussed but never produced; the table is sufficient to project or print.

---

## Risks & mitigations

| Risk | Mitigation |
|---|---|
| SageMaker kernel cold-start eats lab time | Pre-warm kernels before lunch ends |
| Non-coder panic at first notebook cell | Frame sections 1–2 as "watch, don't touch"; everyone touches the RAG step |
| Participant forgets to bring their document | 4–6 sample PDFs pre-staged in `data/` |
| Skeptics (Persona 3) check out | Lead with grounding/citation demos; RAG-vs-vanilla comparison widget is the killer feature |
| Bedrock cost overrun | Default to Nova Lite (frugal); cap embedding doc size; tip from M3 L3a built in |
| Running over time | Lecture blocks compress, not labs. Cut the M2/M3 survey before cutting hands-on. |

---

## Decisions — settled since v1

These were open questions when this plan was written. They are answered now; the answers are
recorded here so nobody re-opens them.

| Question | Answer |
|---|---|
| Who sources and licence-checks the 6 sample PDFs? | **Done.** All six ship in `materials/activities/discipline-assistant/data/`, with per-file source, licence, and page count in that folder's `README.md`. No sourcing work remains. |
| Do we write a SageMaker pre-flight doc? | **Done.** [`PREFLIGHT_CHECKLIST.md`](../facilitator-guide/PREFLIGHT_CHECKLIST.md) covers both the SageMaker and Colab paths. |
| Take-home artifact bundle? | **Yes, and it is automatic.** The whole contribution is published as a single versioned ZIP. Point participants at the release rather than assembling anything by hand. |
| Bridge segment framing | Superseded. The afternoon slot belongs to `mlu-000001`; see its plan. |

## Still for the hosting institution to decide

These genuinely depend on who is running the session and cannot be answered here.

1. **Persona selection** — keep all six, or trim to the disciplines actually in the room. Six is the
   default and needs no preparation; trimming only means projecting fewer rows.
2. **Post-seminar follow-up** — office hours, a curriculum review, a shared channel, or nothing.
3. **Where share-outs happen** — the v1 plan assumes a Slack channel. Any shared channel works, and
   so does a round-the-room verbal share. Nothing in the notebook depends on it.

---

## Reference

> **The upstream AWS curriculum links below are not publicly reachable** (they return HTTP 404 as of
> 2026-09-17 — they may be private rather than removed). None of them is needed to deliver *this*
> lab, which is fully self-contained. They are listed because the v1 day-plan above drew its lecture
> blocks from them; if you intend to run that full day, you will need to source those separately.

- Source curriculum index: [aws-mlu-eep-generative-ai/LESSONS.md](https://github.com/aws-samples/aws-mlu-eep-generative-ai/blob/main/LESSONS.md) — *not reachable*
- Bootcamp Prep Part 1 PDF: PartyRock workshop (used directly as Lab 1) — *not included in this repository*
- Bootcamp Prep Part 2 PDF: Research Assistant building (reference material, not delivered) — *not included in this repository*
