# Curriculum Embedding Lab (`mlu-000001`) — Cell-by-Cell Podium Script

**For:** The instructor narrating the notebook live, cell by cell, at the front of the room.

**How this differs from the cheat sheet:** `INSTRUCTOR_CHEATSHEET.md` is the **run-of-show** — clock times, energy checks, demo-persona strategy, the error table. *This* doc is the **podium narration** — what to say as you click through each numbered cell, and the click-level gotchas. Keep the cheat sheet open for timing; use this to drive the notebook. They do not contradict each other.

> **Cell numbers** below match the notebook's execution order (Part 1.1 = the `pip install` cell, etc.). "🟢" marks an EDIT ME cell faculty fill in themselves.

> **A note on numbering.** "Lab 2" here means *the seminar's second lab* — the afternoon slot, after
> the morning PartyRock session. It is **not** the same as "lab 2 of 4" in the published teaching
> sequence, where this contribution is **lab 1 of 4 — the entry point**. Two different schemes, unfortunately colliding on
> the same number. When in doubt, go by the contribution ID.

---

## Opening (before Part 0) — ~2 min

- "This is a lab, but it's **not a coding lab**. You'll run about five cells of Python and you won't need to understand any of them. The cells that matter are the ones where *you* write."
- "By 3:00 you walk out with four things: a working AI tool tuned to your discipline, a written plan for exactly where it goes in your course, a line you will *not* cross with AI, and one dated commitment for Monday."
- "Two kinds of cells: **watch-along** ones I run, and **🟢 EDIT ME** ones where you type. A blank EDIT ME cell at the end means you left without a plan."
- "Run top to bottom. Don't jump ahead — the later cells depend on values set earlier."

---

## Part 0 — Pick Your Persona (~5 min)

**🟢 Cell: `persona = "1"`**

- "You picked a persona at registration — the one closest to your discipline. Find your number in the table."
- "You are not building a generic quiz generator. Persona 1 builds a *case-study coach*, Persona 3 a *primary-source companion*, Persona 4 a *med-calc drill*. The tool is shaped to how your field actually teaches."
- **Do now:** everyone changes `persona = "1"` to their own number and runs that one cell.

> **Gotcha — persona number is the #1 silent failure.** If someone's output later looks wrong for their field, they left it on `"1"`. Say preemptively: *"If you're not Persona 1 — and most of you aren't — change that string now."* You get a second chance to catch this at cell 1.3, which prints their persona name.

---

## Part 1 — Setup (watch-along, ~10 min)

You drive; they just press run.

**Cell 1.1 — `pip install`:** "Installs the tools we're borrowing — about 30 seconds. The `%%capture` just hides the noisy output."

**Cell 1.2 — imports + Bedrock connect:** "This is one handshake. We connect to Amazon Bedrock once, then call AI all afternoon. Two models behind the scenes — Nova Lite does the writing, a Nova embeddings model does the document search. You don't need to remember that."

**Cell 1.3 — load tool definition:** "This holds the instructions for all six tools. Run it and it prints *yours* — your name, what you're building, your sample document. Confirm it matches your discipline." ← **second persona-number checkpoint.**

> **Gotcha:** `AccessDeniedException` here = Bedrock model access, which is on the AWS setup, not the participant. Don't let anyone troubleshoot AWS during the lab — see the cheat sheet's error table.

---

## Part 2 — Build Your Tool (hands-on, ~30 min)

The payoff. The room goes quiet and engaged here.

**Cell 2.1 — load + index the PDF:** "Reads your sample PDF, chops it into chunks, and builds a searchable index so the AI looks things up instead of making them up. 30–90 seconds — let it run." *(Cheat sheet flags this as the most likely failure point; swap a stuck participant to the dentistry PDF.)*

**Cell 2.2 — grounded chain:** "The anti-hallucination step. We tell the AI: answer *only* from this document; if it's not there, say so. That's the difference between a tool you'd trust and a chatbot."

**Cell 2.3 — ▶ run your tool (the big moment):** "This is it. The AI applies *your* persona's prompt to *your* document. About 30 seconds."

**Cell 2.3 follow-up — the pause prompt.** Read these four questions out loud, then give 60–90 seconds of silence:
1. Would I actually *use* this? In what form?
2. What would I edit before handing it to students?
3. What's missing that I'd add?
4. What's there that I'd cut?

**🟢 Cell 2.4 — customize the prompt (optional):** "This is the real skill of the day — prompting. If the output wasn't quite right, edit the prompt string and re-run. **To run it, delete the `#` on the last two lines to uncomment them.** If yours was already good, skip it — don't over-polish; we have a plan to write."

> **Gotcha:** The smaller model sometimes drifts off-spec (e.g. a Socratic tool that leaks the answer). Frame it as the lab's point: *"Notice when it goes off-spec — that's exactly the judgment you bring that the AI doesn't."*

---

## Part 3 — Where Does This Go? (~20 min) — the heart of the lab

**Say up front:** "Generating cool output is easy. Knowing *where in your course it belongs* is the hard part — and the only thing that determines whether you use this Monday. Specifics only. Not 'someday in my intro class' — specific course, specific week, specific assignment."

- **🟢 3.1 — `my_course` / `my_week_or_unit` / `my_assignment`:** "Real course number, real week."
- **🟢 3.2 — `ai_does` / `i_still_do`:** "The most clarifying question in the lab. If you can't say what *you* still do, you may have outsourced too much of the teaching. Your side should never be empty."
- **🟢 3.3 — `who_sees_output` / `how_often_regenerate`:** "Straight to students or just to you? What cadence — and *why* that cadence?"
- **🟢 3.4 — `my_concern` / `my_mitigation`:** "Be honest. Zero concerns means you haven't thought hard enough. Write the worry *and* how you'll handle it."

**Do:** quiet writing time — circulate, push vague answers toward specifics. (Cheat sheet has a fully filled-in Persona 1 example to project.)

---

## Part 4 — Where AI Does NOT Belong (~10 min)

**Say:** "Equally important — maybe more. What part of your course is *you and only you*? Faculty who can name this are far more credible than people who say AI is good for everything."

- **🟢 4.1 — `where_i_wont_use_ai`:** "Where would AI actually *harm* what you're teaching?"
- **🟢 4.2 — `ai_protected_assignment`:** "One assignment where you *want* students to struggle without AI. Can't name one? Say so out loud — that's worth noticing."
- **🟢 4.3 — `student_ai_policy`:** "One sentence. A student asks Monday, 'Can we use ChatGPT for this?' — what do you say?"

**Tone:** this section earns the room's trust and signals the seminar isn't an AI sales pitch. This is where skeptics convert — lean in.

---

## Part 5 — Bridge to Your LMS (~5 min)

**Say:** "You made something useful — now it has to reach where students see it. The notebook has steps for Canvas, Blackboard, Moodle, and others. Same pattern everywhere: copy the output, paste into your platform's rich-text editor, fix what breaks — usually tables and headers. No platform has a clean markdown-to-quiz pipeline yet; budget ~5 minutes of cleanup per artifact. Still a fraction of writing it from scratch."

**Do:** point at it and move on — it's reference material. **First thing to cut if you're running long.** Don't demo Canvas live unless you're certain it'll work.

---

## Part 6 — Your Monday Commitment (~5 min)

**🟢 Cell 6.1 — `commitment_date` / `commitment_action`:** "One sentence. Specific date, specific class, specific action. Writing it down makes it ~3x more likely to happen." Real date next week, concrete action.

**Cell 6.2 — save the artifact:** "Run this last cell. It bundles everything — your AI output *and* your whole plan — into one markdown file." Then walk them through: "Right-click the file on the left → Download."

Then the two highest-leverage instructions of the day:
- "Email it to yourself, subject **'Monday morning AI commitment.'** Calendar reminders get ignored; emails to yourself don't." *(Model this live on the projector.)*
- "Block 30 minutes on your commitment date to actually do it."

> **Gotcha:** Cell 6.2 reads variables from Parts 3, 4, and 6. If someone skipped an EDIT ME cell, their saved file shows the literal `[bracket placeholder]`. Tell them: *"If your file has brackets in it, you skipped a cell — scroll up, fill it in, re-run this one."*

---

## Part 7 — Share With Someone Different (~5 min)

**Say:** "Find someone from a *different* discipline. Show them three things: your tool's output, your Monday commitment, your protected assignment. Then ask the one question that matters: **'What's one thing about how I'm using AI that you would NOT do in your discipline — and why?'** The disagreement is the point."

**Do:** force cross-discipline pairing (people drift to same-discipline). For the share-back, ask a volunteer what they *heard*, not what they said. Post one insight per persona thread in Slack. Break at 3:00.

---

## Closing — ~1 min

Run the final checklist (working tool, written plan, the AI-doesn't-belong boundary, student policy, dated commitment, downloaded artifact, a colleague's insight) and end on the three next steps: **email yourself, tell one colleague, block the 30 minutes.**

---

## Timing reality

Parts 0–2 eat ~45 min and that's fine — the build is the hook. Parts 3–4 are the substance; protect the full 30 min even if you rush Part 5. Running long? Cut in this order: Part 5 → Part 2.4 → trim Part 2 demo → trim Part 7. **Never cut Parts 3, 4, or 6** — they are the lab. (Full cut/add priority lists are in the cheat sheet.)

---

## Appendix — Per-Persona Demo Pack

Use this if you want to demo a persona other than 1, or switch personas live to show the room how the same notebook produces six genuinely different tools. **To switch:** change `persona = "N"` in the Part 0 cell, then re-run from cell 1.3 down (the persona feeds 1.3, 2.1, and 2.3). Each entry below gives what to say at cell 2.3, what the output looks like, the output quirk to watch for, and a fully filled-in Part 3/4/6 you can project.

> The cheat sheet recommends **Persona 1 (Dentistry)** or **Persona 4 (Nursing)** as the lead demo — clinical reasoning has the strongest cross-discipline pull. The others are here for variety and for when you have that discipline in the room.

---

### Persona 1 — Dr. Maya Patel · Dentistry (Case Study Coach)

- **PDF:** `data/persona1_dentistry_perio_case.pdf` · **Builds:** 3 patient vignettes at 3 difficulty levels from a real perio case.
- **Output:** Vignette 1 (foundational, 1 finding, 2 questions) → Vignette 2 (typical, diagnostic ambiguity, 3 questions) → Vignette 3 (complex, comorbidities, ethics, 4 questions).
- **Land the moment:** *"Maya walked in this morning; she walks out with three teaching cases pulled from a real periodontal article, at three difficulty levels. Tomorrow's Periodontics II just got an upgrade."*
- **Quirk to watch:** the prompt forbids inventing findings — point out it stays inside the source case rather than fabricating lab values.
- **Project for Parts 3/4/6:**
  ```python
  my_course = "DDS 4220 Periodontics II"
  my_week_or_unit = "Week 5 — Diagnosis & Treatment Planning"
  my_assignment = "Pre-class case-study warmup"
  ai_does = "Generates 3 patient vignettes from a primary perio source"
  i_still_do = "Pick which vignette to use; lead the discussion; grade responses"
  where_i_wont_use_ai = "Live clinical-reasoning seminars — students must defend thinking to a real expert"
  ai_protected_assignment = "Mid-semester live case presentation — reason aloud, no AI in the room"
  student_ai_policy = "Use AI to study; don't use AI to do the thinking I assigned"
  commitment_date = "2026-06-08"
  commitment_action = "Generate 3 perio vignettes for the Week 5 warmup and post to Canvas before Monday"
  ```

---

### Persona 2 — Prof. James Chen · Computer Science (Code Critique Generator)

- **PDF:** `data/persona2_cs_data_structures.pdf` · **Builds:** a copy-paste *prompt template* students paste into a chatbot with their broken code — it diagnoses, **refuses to write corrected code**, and asks 1–2 Socratic questions.
- **Output:** a `PROMPT TEMPLATE:` block (with a `[STUDENT CODE HERE]` placeholder) + an `INSTRUCTOR NOTE:` paragraph. This persona builds a *tool students use later*, not content for class — name that distinction out loud.
- **Land the moment:** *"James didn't get a worksheet — he got a reusable tutor his students can paste their code into all semester, that's wired to never hand them the answer."*
- **Quirk to watch:** smaller models sometimes leak a fix anyway. Show the room where the template says "refuse to output corrected code" — that's the guardrail, and catching when it slips is the skill.
- **Project for Parts 3/4/6:**
  ```python
  my_course = "CS 2110 Data Structures"
  my_week_or_unit = "Week 9 — Hash Tables & Big-O"
  my_assignment = "Debugging clinic before Project 3"
  ai_does = "Acts as a Socratic code-review tutor that won't write the fix"
  i_still_do = "Set the no-answer policy; review the template; grade the project myself"
  where_i_wont_use_ai = "Exam design and final-project evaluation — that's my read on what they learned"
  ai_protected_assignment = "The from-scratch hash-table implementation — struggling with collisions is the point"
  student_ai_policy = "Use AI to ask better questions about your code, not to receive code"
  commitment_date = "2026-06-08"
  commitment_action = "Post the code-critique template to Canvas and require it for Project 3 debugging help"
  ```

---

### Persona 3 — Dr. Sarah Whitman · English Literature (Primary Source Companion)

- **PDF:** `data/persona3_english_victorian_essay.pdf` · **Builds:** 5 discussion prompts that push past plot summary into interpretation (authorial choice, context, the text's silences), each citing a specific passage.
- **Output:** 5 open-ended prompts, no yes/no framings, no comprehension checks.
- **Land the moment:** *"Sarah's worry is that AI flattens literature into plot summary. This does the opposite — every prompt forbids recap and forces interpretation."*
- **Quirk to watch:** **this is your most likely skeptic** (the cheat sheet flags her). If a Persona 3 is in the room, slow down — the no-plot-summary constraint is the proof that AI can respect humanities pedagogy. Lean into Part 4 with them.
- **Project for Parts 3/4/6:**
  ```python
  my_course = "ENGL 3340 Victorian Literature"
  my_week_or_unit = "Week 6 — Industrial-era novel"
  my_assignment = "Weekly seminar discussion board"
  ai_does = "Drafts 5 interpretation-level prompts tied to specific passages"
  i_still_do = "Choose which prompts fit the seminar; facilitate; assess the close reading"
  where_i_wont_use_ai = "Grading interpretive essays — the judgment about an argument is mine"
  ai_protected_assignment = "The close-reading essay — wrestling with the text unaided is the skill"
  student_ai_policy = "Use AI to surface questions; the interpretation must be your own"
  commitment_date = "2026-06-08"
  commitment_action = "Seed next week's discussion board with 3 AI-drafted interpretation prompts I've vetted"
  ```

---

### Persona 4 — Prof. Diane Okafor · Nursing (Med-Calc Drill)

- **PDF:** `data/persona4_nursing_pharmacology.pdf` · **Builds:** 5 NCLEX-style dosing problems, **drugs and dose ranges drawn only from the source**, each with a worked solution and a ⚠️ safety red-flag.
- **Output:** numbered problems with patient setup, the calculation, worked math, and one safety element students must catch.
- **Land the moment:** *"Diane gets five dosing problems grounded in the actual formulary — and every one hides a safety red-flag students have to catch. That's the clinical judgment, not just the arithmetic."* Strong second-choice lead demo.
- **Quirk to watch:** the prompt says *say so rather than invent* when the source lacks safe dosing detail. Point out a "not enough info" response is the tool working correctly, not failing.
- **Project for Parts 3/4/6:**
  ```python
  my_course = "NUR 320 Acute Care Pharmacology"
  my_week_or_unit = "Week 7 — Cardiac Drugs"
  my_assignment = "Pre-lecture practice quiz"
  ai_does = "Generates 5 dosing problems with answer keys and safety flags"
  i_still_do = "Review every problem for clinical accuracy; set the passing threshold; lead the walk-through"
  where_i_wont_use_ai = "Final med-administration checkoff — patient safety judgment is assessed by me"
  ai_protected_assignment = "The live dosage-calculation exam — no AI, no calculator crutch"
  student_ai_policy = "Use AI to drill problems; never to compute a dose you'll give a patient"
  commitment_date = "2026-06-08"
  commitment_action = "Generate 5 cardiac-drug dosing problems, verify them, and post as the Week 7 pre-lecture quiz"
  ```

---

### Persona 5 — Dr. Marcus Reyes · Business (Stakeholder Roleplay)

- **PDF:** `data/persona5_business_leadership_case.pdf` · **Builds:** an interactive roleplay — the AI plays the case's most pivotal stakeholder (CFO/CMO/etc.), stays in character, only references case facts, and pushes back on thin reasoning.
- **Output:** an *opening turn* — the stakeholder introduces themselves, states the decision/tension, and invites the student to respond. **This one is conversational**, so demo it differently: after the opening, type a student reply into the prompt and re-run to show it staying in character.
- **Land the moment:** *"Marcus's students can now rehearse a board-room conversation against a CFO who won't break character and won't hand them the answer — before they ever face a real one."*
- **Quirk to watch:** it should say *"I'm not aware of that"* when asked something outside the case. If it invents financials, that's the failure mode to name — and exactly why faculty review matters.
- **Project for Parts 3/4/6:**
  ```python
  my_course = "MBA 610 Leadership & Organizational Change"
  my_week_or_unit = "Week 4 — Stakeholder Negotiation"
  my_assignment = "Pre-case roleplay rehearsal"
  ai_does = "Plays a case stakeholder in character for students to practice against"
  i_still_do = "Run the live in-class case; debrief; grade the negotiation analysis"
  where_i_wont_use_ai = "The graded live negotiation — reading a real human in the room is the competency"
  ai_protected_assignment = "The in-person stakeholder debate — improvising against peers is the point"
  student_ai_policy = "Use AI to rehearse; the graded conversation is human-to-human"
  commitment_date = "2026-06-08"
  commitment_action = "Open the stakeholder roleplay for the Week 4 case and have students log one rehearsal before class"
  ```

---

### Persona 6 — Dr. Lena Hoffmann · Biology (Pre-Lab Knowledge Gate)

- **PDF:** `data/persona6_biology_lab_protocol.pdf` · **Builds:** a pre-lab quiz — **exactly 3 multiple-choice + 2 short-answer** — with at least one safety question and one "why this reagent/step," plus an answer key. Calibrated so a reader passes 4/5 and a skimmer fails.
- **Output:** numbered questions 1–5 then an `ANSWER KEY` with explanations.
- **Land the moment:** *"Lena's lab is dangerous if students show up unprepared. This is a gate — pass means you read the protocol, fail means re-read before you touch a reagent."*
- **Quirk to watch:** verify it produced **exactly 3 MC + 2 short-answer** — the strict structure is the easiest spec for a small model to miss. Use it to show how precise prompts buy reliable structure.
- **Project for Parts 3/4/6:**
  ```python
  my_course = "BIOL 2410 Cell Biology Lab"
  my_week_or_unit = "Lab 4 — Gel Electrophoresis"
  my_assignment = "Mandatory pre-lab gate quiz"
  ai_does = "Generates a 5-question pre-lab check with answer key from the protocol"
  i_still_do = "Verify safety items; set the pass threshold; bar unprepared students from lab"
  where_i_wont_use_ai = "Bench technique assessment — I watch them pipette, AI can't"
  ai_protected_assignment = "The lab notebook write-up — interpreting their own messy data unaided"
  student_ai_policy = "Use AI to prep for lab; your data analysis is your own"
  commitment_date = "2026-06-08"
  commitment_action = "Generate the Lab 4 pre-lab gate quiz, verify the safety question, and require a pass before Monday's lab"
  ```
