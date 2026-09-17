# Lab 2 (Curriculum Embedding) — Instructor Cheat Sheet

**For:** The instructor running the curriculum-embedding lab (1:30 PM – 3:00 PM).
**Companion docs:** `SEMINAR_PLAN.md` (full agenda), `PREFLIGHT_CHECKLIST.md` (morning-of setup), `CONTENT_AUDIT.md` (why this lab exists), `../curriculum-embedding-lab.ipynb` (the notebook).

---

## TL;DR

- This is **NOT a coding lab.** It's a curriculum design workshop wrapped in a notebook.
- **Parts 3, 4, and 6 are the protected core** — reflection cells where faculty write their plan. Defend these against time pressure.
- **If you run short on time, cut Part 5 (LMS bridge) first**, then trim Part 7 (share-out) to 2 minutes.
- **Skeptics convert in Part 4** ("where AI does NOT belong"). Spend time there if you have a Persona 3 (Sarah) in the room.
- **Demo lead:** Use Persona 1 (Dentistry) or Persona 4 (Nursing). Clinical reasoning has the strongest cross-discipline pull.

---

## Pre-show (1:15 – 1:30, during the bridge segment)

While the bridge instructor talks about *"now where does this fit in your course?"*:

- [ ] Open the notebook in SageMaker Studio
- [ ] Run Parts 1.1, 1.2, 1.3 to pre-warm the kernel and verify Bedrock access
- [ ] Have Persona 1 (Dentistry) loaded as the demo
- [ ] Slack channel open in a second window — you'll model "email to self" at 3:00

If anything errors pre-show, see "Common errors" below.

---

## Section-by-section script

### Part 0 — Pick your persona (1:30 – 1:35, 5 min)

**What you say:**
> "You picked a persona at registration. Today you're going to build the AI tool that persona envisioned — Maya gets her case-study coach, Sarah gets her primary-source companion, Lena gets her pre-lab gate. Generic templates don't honor what you actually need. So we built six of them."

**What you do:**
1. Open the notebook on the projector
2. Read the persona table out loud (slowly)
3. **Pause:** *"Find your number. Change the value in the next cell to match. If you're between two, pick the one you'll teach next semester."*
4. Walk around briefly — anyone confused about their persona is the person who'll be lost all afternoon

**Time check:** Done by 1:35.

---

### Part 1 — Setup (1:35 – 1:45, 10 min) — WATCH-ALONG

**What you say:**
> "Watch me run these. Don't click anything on your screen yet. Three cells: install tools, connect to AWS, load the six tool definitions. While they run, I'll tell you what we're doing."

**What you do:**
1. Run cell 1.1 (install). While it runs (~30 sec), say: *"Borrowing other people's tools — same as you do every day with your textbook."*
2. Run cell 1.2 (imports + Bedrock). Say: *"One handshake with AWS. From now on, calling AI is one line of code."*
3. Run cell 1.3 (persona tools dictionary). Say: *"This is the most important cell of the morning. It contains six different tool prompts — one for each persona's vision. We're going to use yours in a minute."*

**Time check:** Done by 1:45.

**Watch for:** Anyone clicking ahead. Gently: *"Stay with me — your turn starts at Part 2."*

---

### Part 2 — Build your tool (1:45 – 2:15, 30 min) — HANDS-ON

**What you say:**
> "Now your turn. Three cells: load YOUR document, build the search index, run YOUR tool. Press Shift+Enter on each. The output is what your persona envisioned."

**What you do:**

**1:45 – 1:50 (5 min) — Instructor demo with Persona 1**

- With your demo session set to Persona 1, run cells 2.1, 2.2, 2.3
- When 2.3 produces the case vignettes, read the first vignette out loud
- **Land the moment:** *"Maya walked in this morning. She walked out with three teaching cases pulled from a real periodontal article, at three difficulty levels. Tomorrow's Periodontics II class just got a major upgrade."*

**1:50 – 2:10 (20 min) — Everyone runs their own**

- *"Your turn. Run cells 2.1, 2.2, 2.3. Cell 2.1 takes about a minute — it's building the search index."*
- Walk the room. **Cell 2.1 is the most likely failure point** (embedding cost / time). If someone's stuck, swap their persona's PDF to the working dentistry one.
- When most people see output, ask: *"Raise your hand if what came out is recognizably useful for your course."* (Most hands should go up.)

**2:10 – 2:15 (5 min) — Pause and read**

- *"Stop. Read what your AI produced. Don't worry about being right or wrong — just notice. The next sections capture what you noticed."*
- Don't push them past this. The 5-min pause is when the curriculum embedding starts to click.

**Watch for:**
- Someone who's NOT impressed with their output — that's actually fine; Part 2.4 lets them customize the prompt
- Someone visibly skeptical (probably Persona 3, Sarah) — note them; spend extra time with them in Part 4

---

### Part 3 — Curriculum mapping (2:15 – 2:35, 20 min) — PROTECTED REFLECTION

**This is the heart of the lab. Defend the time.**

**What you say:**
> "Generating the cool output was the easy part. The hard part — and the part that determines whether you actually use this Monday — is knowing exactly where in your course it goes. Four cells. Fill them with **specifics**. Not 'someday in my intro class' — specific course, specific week, specific assignment. Vagueness here means you won't do it Monday."

**What you do:**
1. Project your own example. Walk through each variable for Persona 1:
   ```python
   my_course = "DDS 4220 Periodontics II"
   my_week_or_unit = "Week 5 — Diagnosis & Treatment Planning"
   my_assignment = "Pre-class case-study warmup"
   ai_does = "Generates 3 patient vignettes from a primary perio source"
   i_still_do = "Pick which vignette to use; lead the discussion; grade student responses"
   who_sees_output = "Students via Canvas pre-class assignment"
   how_often_regenerate = "Each new topic — about 12 times per semester"
   my_concern = "AI might describe a finding that isn't actually in the source"
   my_mitigation = "Quick review pass before posting; flag uncertain claims for class discussion"
   ```
2. *"Now your turn. 15 minutes. Be specific."*
3. **Walk the room.** Read over shoulders. When you see a `my_course = "[something vague]"`, say quietly: *"What's the actual course code? Catalog number? When does it next meet?"* The specificity is the work.

**Time check:** Done by 2:35.

**Watch for:**
- Faculty leaving placeholders unchanged → call it out individually
- Faculty filling in *aspirational* answers ("I'll figure that out later") → push for current-semester specificity
- The "I still do" cell is the diagnostic. If they can't articulate what they still do, they may have outsourced too much.

---

### Part 4 — Where AI does NOT belong (2:35 – 2:45, 10 min) — SKEPTIC CONVERSION

**What you say:**
> "Equally important. Maybe more important. Where in your course is YOU and only YOU? Where would using AI actually harm what you're trying to teach? Three cells. Be honest — if you have no boundary, you probably haven't thought hard enough."

**What you do:**
1. Project your own example for Persona 1:
   ```python
   where_i_wont_use_ai = "I won't use AI to evaluate student responses in clinical reasoning seminars — that's where they learn to defend their thinking against a real expert"
   ai_protected_assignment = "Mid-semester live case presentation — students must reason aloud in front of peers; no AI in the room"
   student_ai_policy = "Use AI to study; don't use AI to do the thinking I assigned"
   ```
2. *"Your turn. 8 minutes."*
3. **Find your skeptics.** This is their moment. Specifically engage them: *"What part of your teaching does AI threaten? Write that down — that boundary IS your curriculum design."*

**Time check:** Done by 2:45.

**Watch for:** Faculty who fly through this with vague answers. Push them: *"Name a specific assignment."*

---

### Part 5 — LMS bridge (2:45 – 2:50, 5 min) — INSTRUCTIONAL

**What you say:**
> "The output needs to get from this notebook into the place your students see it — Canvas, Blackboard, whatever you use. The notebook has the steps. The short version: copy, paste, fix the formatting where it breaks. Plan for about 5 minutes of cleanup per artifact."

**What you do:**
- Read the relevant section of the notebook out loud (Canvas, Blackboard, Moodle)
- Don't demo Canvas live unless you're sure it'll work — failure here loses momentum
- *"Move on — there's a more important section coming."*

**Time check:** Done by 2:50.

**If running short:** **Cut this section.** Tell them to read it later. Hand the 5 minutes to Part 4 or Part 6.

---

### Part 6 — Monday commitment (2:50 – 2:55, 5 min) — PROTECTED

**What you say:**
> "One sentence. Specific date, specific class, specific action. Writing it down makes it 3x more likely to happen."

**What you do:**
1. Project your own commitment for Persona 1:
   ```python
   commitment_date = "2026-06-08"
   commitment_action = "Generate 3 perio case vignettes for the Week 5 warmup and post to Canvas before Monday's class"
   ```
2. *"Your turn. 2 minutes."*
3. Run cell 6.2 yourself live — show the artifact file appearing in the file browser
4. **The critical move:** *"Now everyone — open your email. Send the file to yourself. Subject: 'Monday morning AI commitment.' I'm doing it right now, on the projector."* Do it visibly.
5. *"You just made it 3x more likely you'll actually do this."*

**Time check:** Done by 2:55.

**Watch for:** Anyone who didn't email themselves. Walk over. The email is the commitment device.

---

### Part 7 — Pod share-out (2:55 – 3:00, 5 min)

**What you say:**
> "Find someone from a different discipline than yours. Show them your tool's output, your Monday commitment, and your protected assignment. Then ask them: 'What's one thing about how I'm using AI that you would NOT do in your discipline — and why?'"

**What you do:**
- Manage the cross-discipline pairing (people gravitate to same-discipline; intervene)
- 3 min for the exchange
- 2 min: ask 1 volunteer to share what they heard from their partner (NOT what they said themselves — what they heard)
- Push to break at 3:00

---

## Common errors and fixes

| Error | Likely cause | Fix |
|---|---|---|
| `botocore.exceptions.NoCredentialsError` | AWS session expired | Refresh credentials |
| `AccessDeniedException` on model invoke | Bedrock model not enabled | Verify per `PREFLIGHT_CHECKLIST.md` |
| `Could not load PDF` | Wrong persona variable, or PDF placeholder not yet replaced | Confirm `persona = "1"`-`"6"` is set; check `data/` for actual PDF |
| Embedding cell hangs > 90 sec | PDF too large (> 50 pages) | Swap to Persona 1 sample |
| Kernel disconnected | Studio session timeout | Restart kernel; re-run Part 1 |
| Reflection cells full of placeholders | Faculty rushed past them | Stop, walk room, push for specificity |
| Skeptic checks out in Part 3 | Generic engagement not landing | Pull them into Part 4 personally |

---

## Energy check moments

| When | What to listen for | If wrong |
|---|---|---|
| 1:50 | Quiet typing + occasional "oh wow" during Part 2 | Worried silence → check projector visibility, run a demo yourself |
| 2:20 | Steady typing during Part 3 reflection cells | Empty cells → walk the room, push for specifics |
| 2:40 | Pauses + visible reflection during Part 4 | Fly-through → spend time with skeptics personally |
| 2:55 | Visible commitment to emailing the artifact | Skipping → call it out, do it yourself on the projector |

---

## If you have extra time

In priority order, add:
1. **More Part 3 specificity** — ask 2-3 faculty to read their `i_still_do` out loud; collect patterns on the whiteboard
2. **Cross-discipline pairings in Part 7** — make it 8 minutes instead of 5
3. **One "what scares you?" round** — open mic, 2 minutes, no fixing
4. **Preview the standalone post-seminar lab** — open the RAG repo URL briefly as "what's next if you want to keep going"

---

## If you run out of time

In priority order, cut from the bottom:
1. **Part 5 (LMS bridge)** — fully cuttable; tell them to read it later
2. **Part 2.4 (custom prompt iteration)** — most faculty won't customize anyway
3. **Part 2 demo time** — cut to 3 min instead of 5
4. **Part 7 share-out** — trim to 2 min, share 1 example not 2

**Do NOT cut:** Parts 3, 4, and 6 (the reflection and commitment cells). These are the lab. Without them, this becomes the v1 Lab 2 — output without embedding.
