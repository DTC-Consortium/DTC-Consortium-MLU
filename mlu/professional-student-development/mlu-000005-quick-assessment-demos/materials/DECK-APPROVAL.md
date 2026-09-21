# Deck approval status — read before touching the deck

**The words on the 28 approved slides may be removed. They may never be added to or reworded.**

Every string on those slides was reviewed and signed off. The standing permission is subtractive:
deleting approved copy is cleared, because nothing unreviewed reaches the screen. Writing new
copy onto an approved slide — or rewording existing copy, which is the same thing — is not.

New **slides** are different. They are new material, they go to legal on their own, and they do
not touch what was approved. The deck currently has one: slide 0.

| | |
|---|---|
| Approval baseline | `approved-deck-baseline.txt` — the slide text as approved |
| Baseline captured from | `assessment-lifecycle-deck.pdf` at md5 `9fcad6b71fe23cd4c994a2527d76d277` |
| Source of record | `aws-mlu-faculty-fellows-inventory/raw-assets/decks/Tariq_Hook_assessment-lifecycle-deck.pdf` |
| Current deck | 29 slides — slide 0, then the approved 28 |

---

## The check

`verify_deck.py` diffs every build against the baseline and **fails on any addition**. It is not
advisory: `export_pdf.sh` will not overwrite the PDF until it passes.

```sh
python3 verify_deck.py            # the .pptx
python3 verify_deck.py --show     # ...and print every deletion
python3 verify_deck.py --pdf assessment-lifecycle-deck.pdf
```

This replaced a frozen-md5 contract. An md5 answers *"is this file unchanged?"*, which stopped
being the right question the moment subtractive edits were permitted — it forbids the edits that
are allowed and says nothing about the ones that aren't. The diff answers the real question:
*does this deck contain only approved strings, and fewer of them?*

`approved-deck-baseline.txt` is the approval record. **Never regenerate it from a rebuilt deck** —
that rebases the check onto whatever the deck currently says and silently blesses it. It is
regenerated only from the source-of-record PDF, by hand, if legal approves new copy.

`verify_deck.py` also checks a second, unrelated thing: that the shared-folder QR code is on every
slide and decodes to `DRIVE_URL`. That one is about delivery, not about legal.

---

## What has been removed, and why

| Slide | Removed | Why |
|---|---|---|
| 2 | "Find **Apps** in the left menu. Today's tools live there." | Nothing is pre-published any more. Attendees build each tool from a prompt; there are no apps waiting in that menu. |
| 7 | "— and wrong about running times" | Marcus's card gave away the slide-11 reveal about twenty minutes early. This was the deck's worst known problem and the talk track used to spend a paragraph working around it. |
| 13 | The four `Open / Paste / Generate / Edit` steps | They pointed at a pre-published app and a table card that no longer exist. |
| 15 | The four steps | Same — and the original author's note said these had to be rewritten to match the finished app, which subtractive-only editing does not allow. Deleting them settles it. |
| 25 | `Open` / `Paste` / `Upload` | Same. The fourth step, the check, stays. |

Slides 13, 15 and 25 keep their title, their check card and their `HANDS-ON · N MIN` pill. Each is
now the marker and the clock; the steps live on the prompt cards in the shared folder, where they
can be revised without going back to legal. That is the point of moving them.

## Three unapproved *additions* that were reverted

`build_deck.py` had been sitting one revision **ahead** of approval, carrying copy legal never
saw. It was harmless only while the PDF was never rebuilt. The first rebuild would have shipped
all of it silently.

| Slide | Was in the `.pptx` | Restored to |
|---|---|---|
| 4 | a subtitle: "The paper on your table, graded with only the rubric on the handout." | *(no subtitle)* |
| 4 | five cards, `A B C D F`, and "Hands up **for your letter**." | four cards, `A B C F`, "Hands up." |
| 9 | "**60 of 100 points** go to what you can see without expertise" | "**Half the points** go to what you can see without expertise" |

A fourth difference — slide 7's "The paper you graded. Fluent and confident." — was a rewording,
so it could not ship either. Deleting the spoiler clause reaches nearly the same place
subtractively, and that is what the deck now does.

**Slide 4 has no `D` card.** The weak rubric does have a D band. Poll A/B/C/F only and never call
for a D; the talk track says how.

## Slide 0, and why it is numbered 0

The shared-folder slide sits ahead of the cover and is numbered **0**, so the cover is still
slide 1 and the approved 28 keep the numbers everything refers to.

The talk track, the handout and the take-home pack are full of references like "slide 13",
"slide 21", "slide 27". Inserting a new slide 1 would shift all 28 and quietly falsify every one
of them — the kind of error that is invisible in review and obvious on stage. `firstSlideNum=0`
in `build_deck.py` avoids it entirely.

The QR code is stamped on the other 28 slides **with no caption**. That is what keeps it
compatible with the permission: a graphic adds no words, so the approved copy is provably intact
and the check still passes. Slide 0 carries all the explanation.

If you add another slide ahead of the approved 28, raise `LEADING_EXTRA` in `verify_deck.py`.
That line exempts a slide from the check, so it is the one worth reviewing carefully — moving
approved copy onto a "new" slide to dodge the check would defeat the point of having one.

---

## Releasing a rebuild

```sh
python3 build_deck.py                    # regenerates the .pptx and the QR asset
python3 verify_deck.py --show            # read the deletions; confirm 0 additions
./export_pdf.sh                          # gated on the check; syncs the attendee copy
python3 build_pack.py                    # rebuilds both PDFs around the new deck
```

`export_pdf.sh` verifies the `.pptx` before exporting and the PDF afterwards, then copies the
result to `participant-resources/`. Both copies must stay identical — the exported deck ships to
attendees as the appendix of the take-home pack, and `build_pack.py` copies its pages in at
native size with nothing overlaid on them.

```sh
md5 -q assessment-lifecycle-deck.pdf participant-resources/assessment-lifecycle-deck.pdf
```

The md5 is no longer a fixed value to check against — it changes with every legitimate rebuild.
It is only there to confirm the two copies match each other. `verify_deck.py` is what says
whether the content is allowed.

## Known issues in the approved copy, and where they are handled

| Slide | Issue | Handled in |
|---|---|---|
| 4 | No `D` card, though the weak rubric has a D band | Talk track — poll A/B/C/F only, never call for a D |
| 9 | "Half the points" understates it; 60 of 100 is the real figure | Talk track — say "half," then give the number; don't correct the slide on stage |
| 11 | Shows `B+` for 88/100 | Fixed at the source: the weak rubric carries plus/minus bands, so 88 **is** a B+ |

Slide 7's spoiler used to be the fourth row here. It is gone.
