# The shared folder — what goes in it, and how

Everything the room needs arrives through one Google Drive folder, reached by the QR code on
slide 0 and in the corner of every slide after it.

**Current folder:**
<https://drive.google.com/drive/folders/10aipzDJD_Hpn8lVpa8eorBTFFeYjVn3D>

The link lives in one place in this project — `DRIVE_URL` in
[`../session_config.py`](../session_config.py). It is stamped into the deck's QR codes from
there. Change it there and rebuild; do not paste a URL into a slide by hand.

```sh
python3 build_deck.py && ./export_pdf.sh && python3 build_pack.py
```

---

## Required layout

**One document.** Faculty open one thing and never leave it. Everything they read, grade, copy or
paste is inside it: the paper, the rubric, the assignment, the objectives, all three prompts.

```
2026_AWS_MLU_AI_Symposium/                       ← the folder the QR code points at
│
├── ★ THE ASSIGNMENT LIFECYCLE — follow along here    Doc  ← MASTER-FOLLOW-ALONG.md
│
├── Sample pack/
│   ├── The course reading                    PDF   uploaded into the Rubric Builder
│   ├── Class roster                          Sheet
│   ├── Student papers/                             pasted INTO the tools, so kept separate
│   │   ├── Marcus Lee — the paper you graded       Doc
│   │   ├── Aisha Rahman — a strong paper           Doc
│   │   ├── Priya Chandra — a reflection, not an analysis   Doc
│   │   └── Leila Haddad — an unfinished draft      Doc
│   └── For the tools (advanced)/
│       └── The rubric format (mlu-rubric/1)  Doc
│
└── Take home/
    ├── Follow-along guide                    PDF   the same document, branded and paginated
    ├── The session deck                      PDF
    └── Take-home pack                        PDF
```

The **Follow-along guide** is the master document rendered through the DTCC handbook stylesheet
by `build_pack.py --edition followalong`: same source, so the two cannot drift, but with the
branding and with every prompt in a bordered callout. Useful for anyone who wants to print it or
read it away from Drive. The Google Doc stays the one people work from live, because it is the
one they can copy out of.

### Why one document

The folder used to hold seven: a start-here page, a steps page per tool, and a prompt page per
tool. It was coherent on paper and wrong in a room. Ninety minutes does not have room for forty
people navigating between documents, and every hop is somewhere to get lost while the clock runs.

Two consequences follow, and both are improvements:

- **Nothing is printed.** The paper and the weak rubric are in the document, so the opening
  grading exercise happens on the laptop that is already open. No table cards, no handout, no
  stack of paper to carry.
- **Nobody brings their own assignment.** One assignment, in the document, ready to paste. It
  saves four or five minutes of reading and typing, and it means forty people hit the same
  problems at the same time — which is what makes volunteers effective rather than scattered.

**The student papers stay outside.** They get pasted *into* the tools rather than read, so they
are better as separate documents that can be opened and copied whole.

### The prompt blocks

The prompts sit between marker lines — `━━━ START OF PROMPT 1 ━━━` / `━━━ END OF PROMPT 1 ━━━` —
and the document explains once, at the top, how to select between them: click before the first
word, shift-click after the last.

Two rules when editing them:

1. **Do not let the prompt lines become Markdown lists.** Google Docs turns `- ` and `1. ` into
   real lists, which renumber and re-bullet when pasted. Inside a prompt block, lines start with
   an em dash or `RULE n.` for exactly that reason.
2. **The marker lines are load-bearing.** They are how forty people find the boundaries of a
   block they have to select by hand.

Google Docs' Markdown import does not keep fenced code blocks, which is why the markers exist at
all: there is no grey box to point at.

**Emphasis inside a table cell is escaped, not applied** — `**Content**` arrives as literal
asterisks. The weak-rubric table in the master document has no bold in it for that reason.

---

## What does NOT go in the folder

| Not shared | Why |
|---|---|
| `facilitator/PROMPT-F1-grading-app.md` | The grading app is a demo the room watches. Handing out its prompt invites people to build it during the Kiro segment instead of listening. |
| `facilitator/PROMPT-F2-kiro-grader.md` | Same, and Kiro is not on their machines. |
| `TALK_TRACK.md` | Stage directions. It says what to do when a CS faculty member spots Marcus's errors early. |
| The facilitator guide PDF | Contains the talk track and the answer to slide 17's poll. |
| *The reference rubric* **before** the session | See below. |

> ### One timing decision to make deliberately
>
> *The reference rubric* **is the answer to the first hands-on**. If it is in the folder from the
> start, some attendees will find it during the 12 minutes of slide 13 and compare their
> generated rubric against it instead of reading their own.
>
> Two defensible choices:
>
> - **Leave it in.** Simpler, one folder, nothing to do live. Most people will not go looking.
> - **Add it at 0:36**, after the rubric segment. One drag into the folder, and the reference
>   rubric lands exactly when it is useful — as a comparison, which is what it is for.
>
> Pick one before the day. Do not leave it to the moment.

---

## Sharing settings

- **"Anyone with the link" → Viewer.** No Google sign-in. Attendees are already signing into
  Amazon Quick during the first twelve minutes; a second sign-in wall costs the session its
  opening, and the people it blocks are exactly the ones already struggling.
- **Viewer, not Editor.** Editor means one person can delete the sample pack mid-session.
- **Check it from outside your account.** An incognito window, signed out, on a phone. A folder
  that opens for you because you own it will not open for them.

## Before every delivery

- [ ] Folder opens in an incognito window, signed out, on a phone
- [ ] Every file opens — not just the folder — **tapped on a phone, not clicked on a laptop**
- [ ] Nothing in the folder shows a file extension except the two in *For the tools (advanced)*
- [ ] `DRIVE_URL` in `session_config.py` matches the folder, and the deck was rebuilt after any change
- [ ] `python3 verify_deck.py` reports the QR present on every slide and decoding to that URL
- [ ] Scan slide 0 from the back of the actual room, off the actual projector
- [ ] The three prompts are **Google Docs**, and you can select and copy a whole prompt block
- [ ] **No curly quotes in any prompt block** — search each prompt doc for `"` and `"`
- [ ] Paste one prompt straight from its Doc into Quick and build the app from it. This is the
      only check that tests what attendees actually do; do it on every delivery, not once.
- [ ] Decide the `rubric-golden` timing, above
- [ ] No facilitator material in the folder
- [ ] `DRIVE_SHORTLINK` filled in, if you want a typable link on slide 0 for the back row

> **Scan it off the projector, not off your laptop.** A code that scans from two feet away on a
> retina display can be unreadable at forty feet through a washed-out projector — and that is
> the only place it has to work.
