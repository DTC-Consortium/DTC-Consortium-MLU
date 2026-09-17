# Lab 2 — Instructor Cheat Sheet

**For:** The instructor running Lab 2 (1:30 PM – 3:00 PM) during the 1-day Faculty AI Seminar.
**Companion docs:** `SEMINAR_PLAN.md` (full agenda), `PREFLIGHT_CHECKLIST.md` (morning-of setup), `seminar-lab2-discipline-assistant.ipynb` (the notebook itself).

---

## TL;DR

- **You drive Part 1 + 2.** Participants drive Part 3 + 4. You facilitate Part 5.
- **Lead the demo with Persona 1 (Dentistry)** — clinical reasoning is the most persuasive demo for a mixed room.
- **The killer moment is 3.7** — grounded vs. vanilla side-by-side. Don't rush it.
- **If you run short on time, cut Template C (Rubric) in Part 4.** Quiz and Study Guide are the keepers.

---

## Pre-show (1:15 – 1:30 PM, during the bridge segment)

While the bridge instructor talks about *PartyRock → SageMaker*:

- [ ] Open the notebook in SageMaker Studio
- [ ] Run cells 1.1, 1.2, 1.3 to pre-warm everything
- [ ] Run Part 2.1 (model setup) — verifies both Nova Lite and Mistral are accessible
- [ ] Have the dentistry sample PDF loaded path ready for your demo
- [ ] Slack channel open in a second window

If anything errors in pre-show, see "Common errors" at the bottom.

---

## Section-by-section script

### Part 1 — Setup (1:30 – 1:45, 15 min) — INSTRUCTOR-LED

**What you say (after participants open the notebook):**
> "This is a Jupyter notebook. Think of it as a recipe card. Gray boxes are notes, white boxes are buttons. We're going to press them in order. For this first part, **just watch me** — don't touch your own notebook yet. I'll tell you when it's your turn."

**What you do:**
1. **Open the notebook.** Project it large.
2. **Read the "What you'll build today" cell out loud.** Anchors expectations.
3. **Run cell 1.1 (install).** While it runs (~30 sec), explain that real production code would have these pre-installed — this is just because we're sharing infrastructure.
4. **Run cell 1.2 (imports).** Frame: *"Setting tools out on a workbench."* Don't go line by line.
5. **Run cell 1.3 (Bedrock client).** Frame: *"One handshake with AWS. From now on, every model call is one line of code."*

**Time check:** You should be done by 1:45. If you're behind, skip the workbench metaphor and just run.

**Watch for:** Anyone looking lost. They should be following along visually but not clicking. If someone has their hands hovering over the keyboard, gently say *"this part is just watching — your turn is coming."*

---

### Part 2 — Direct prompting (1:45 – 2:00, 15 min) — FIRST HANDS-ON

**What you say:**
> "PartyRock hid the code from you. Here it is. Three lines: define a prompt, pick a model, get a response. Now it's your turn."

**What you do:**
1. **Run cells 2.1 (model setup).** Quick.
2. **Stop at cell 2.2 (🟢 EDIT ME).** Walk over to a participant's screen if you can. *"Change this prompt to something from your field. Hit Shift+Enter."*
3. **Give them 2 minutes** to write their own prompt and run it.
4. **Run cell 2.3 yourself** (Mistral, same prompt). Project the comparison.
5. **Land the takeaway:** *"Same prompt. Different model. Different voice. This is the first thing you outgrow PartyRock for — choosing the right model for the job."*

**Time check:** Done by 2:00.

**Watch for:** Someone whose prompt errored. Most likely cause: they replaced the whole string with something that broke quoting. Fix: paste a working prompt into theirs.

---

### Part 3 — RAG (2:00 – 2:35, 35 min) — THE CORE

This is the most important section. Don't rush.

**What you say:**
> "Now we're going to ground the AI in YOUR discipline's content. This pattern is called RAG — Retrieval-Augmented Generation. Fancy name for 'give the model the textbook before you ask it the question.' What it gets you is no hallucinations. Every answer traceable. This is the part that changes the AI mandate from scary to useful."

**What you do:**

**2:00 – 2:10 (10 min) — Instructor demo with Persona 1 (Dentistry)**

- Set `pdf_path = "data/persona1_dentistry_perio_case.pdf"`.
- Run 3.2 (load), 3.3 (chunk), 3.4 (embed).
- **While 3.4 runs (~60 sec), narrate:** *"It's calling Bedrock once per chunk to turn each piece of text into a numeric fingerprint. We'll use those fingerprints to find relevant content when you ask a question."*
- Run 3.5 (build chain).
- Run 3.6 with the default question. Show the source citations at the bottom.
- **Run 3.7 — the grounded vs. vanilla comparison.** *This is the moment.*
  - Read both answers out loud.
  - Point at the differences. *"See how the grounded version cites the specific clinical findings? See how the vanilla version makes up details? That's the difference grounding makes."*
- Pause. Let it land.

**2:10 – 2:30 (20 min) — Participants run their own**

- *"Now your turn. Change the `pdf_path` to your persona — table is right above the cell. Then run cells 3.2 through 3.7."*
- Walk the room. **The embedding cell (3.4) is the most likely failure point** — that's where you provide white-glove help.
- Encourage them to ask their document something they actually wonder about.

**2:30 – 2:35 (5 min) — Buffer / Q&A**

- Anyone behind catches up.
- Take questions. Common ones in "FAQ" below.

**Watch for:**
- **Embedding takes too long:** PDF was bigger than spec. Suggest swapping to a sample. Don't troubleshoot Bedrock costs live.
- **Vanilla answer happens to be correct:** Acknowledge it. *"Sometimes the model gets lucky. But in clinical work, would you want to bet on lucky?"* Pivots to safety framing.
- **Skeptic engaged:** This is your conversion. Spend extra time with them in Part 4.

---

### Part 4 — Templates (2:35 – 2:55, 20 min) — TAKE-HOME

**What you say:**
> "Three templates. Pick whichever is most useful for what you teach. Run it. You're going to walk out of here with a real artifact — quiz questions, study guide, or rubric — grounded in your discipline's content."

**What you do:**
1. **Quickly walk through what each template does** (30 sec each — don't run them yet).
2. **Tell participants to run at least one.** Fast finishers run all three.
3. **Walk the room.** Look for outputs that are share-worthy in Part 5.
4. **At 2:50, run cell 4.4 (save artifact) yourself** and project it. Show them where to right-click to download.
5. *"Take this file home. Show it to a colleague Monday morning. That's the proof you built something real."*

**If running short on time:** Cut Template C (Rubric). Have everyone do at least one of A or B.

**Watch for:** Quality of generated outputs. Pre-identify 2–3 attendees whose results you want to spotlight in Part 5.

---

### Part 5 — Share-out (2:55 – 3:00, 5 min) — FACILITATE

**What you say:**
> "Pick one output. Paste it into Slack in your persona's thread. Include your discipline, which template you used, and one thing that surprised you. We'll spotlight 2–3 in the wrap at 3:45."

**What you do:**
- Don't wait for everyone to post — push to break at 3:00 sharp.
- Make sure the Slack channel is visible on screen so latecomers can find it.

---

## Common errors and fixes

| Error | Likely cause | Fix |
|---|---|---|
| `botocore.exceptions.NoCredentialsError` | AWS session expired | Refresh credentials from the seminar console |
| `AccessDeniedException` on model invoke | Bedrock model not enabled | Run pre-flight check; have backup model IDs ready |
| `Could not load PDF` | Scanned PDF (not text-extractable) | Swap to sample; do NOT troubleshoot live |
| Embedding cell hangs > 90 sec | PDF too large OR throttling | Cancel cell, swap to smaller sample |
| Notebook kernel disconnected | Studio session timeout | Restart kernel, re-run from Part 1.2 (imports cached) |
| Quiz output is generic / bland | Prompt not specific enough | Suggest adding course-level detail to the template |

---

## FAQ to expect from participants

**"Can I use this with confidential exam material?"**
> Yes — your documents only exist in your SageMaker session, not shared. But check your institution's data policy before uploading sensitive material.

**"What does this cost?"**
> Today's lab costs ~$0.10–0.50 per participant. In production you'd budget based on usage — Nova Lite is the frugal choice we used. We can talk pricing strategies after the seminar.

**"Can I run this on my laptop?"**
> Not directly — you need AWS access. But everything here works in any Python environment with Bedrock credentials. Talk to your IT department about getting access.

**"How is this different from ChatGPT?"**
> Three things: (1) grounded in YOUR documents, (2) you choose the model and control the prompt, (3) your data stays in your AWS account. ChatGPT-the-product is the consumer version; this is the building-block version.

**"What if I'm not technical?"**
> You don't need to be. Today you ran cells without writing code. To customize on Monday, you'd change three things: the PDF path, the question, and the prompt template. All three are clearly marked.

---

## If you run out of time

In priority order, cut from the bottom:
1. **Template C (Rubric)** — keep Quiz and Study Guide
2. **Buffer at 2:30 – 2:35** — push forward
3. **Multi-template demo** — have everyone do one template, not three
4. **Detail in the comparison cell 3.7** — show but don't analyze line by line

**Do NOT cut:** Part 3 (the RAG section) or the grounded-vs-vanilla comparison. Those are the seminar.

---

## If you have extra time

In priority order, add:
1. **More questions in 3.6** — let participants ask their document 3-4 things
2. **Cross-discipline pairing** — have a CS prof and a humanities prof share screens
3. **Template variations** — change "undergraduate" to "graduate" and re-run a template
4. **Preview Lab 4 (Agents)** — open the M3 Lab 4 notebook briefly as a "what's next"

---

## Energy check

At ~2:15, you should hear typing and quiet "oh wow" reactions during the comparison cell. If the room is silent and worried-looking, **pause and check in**: *"What's hardest right now?"* Then troubleshoot collectively. Don't push forward through panic.
