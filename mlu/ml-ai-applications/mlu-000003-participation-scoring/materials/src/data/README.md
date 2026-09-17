# Sample data for the Participation Scoring Lab

This folder ships everything the lab needs to run out of the box, plus the slots where you
drop in your own class material.

## What's here

| File | What it is | Source |
|---|---|---|
| `persona2_cs_data_structures.pdf` | The **day's lesson material** — Ch. 1 of *Open Data Structures* (interfaces, ArrayStack, running time, amortized analysis). This is what defines "on topic" for the sample class. | Open Data Structures by Pat Morin (CC-BY), Ch. 1 extract. Reused from the curriculum lab. |
| `sample_class_transcript.vtt` | A **fabricated Zoom transcript** of a CS Data Structures class discussing that chapter. Six speakers spanning every participation tier. | Original, authored for this lab. All students are invented. |
| `sample_roster.csv` | A **fabricated class roster** of seven enrolled students. | Original, authored for this lab. |

The sample is built so the output is legible: it demonstrates a strong on-topic contributor, a
solid contributor, a brief-but-substantive contributor, a chatty-but-off-topic student, a
filler-only student, and two students who never spoke (one "silent," one effectively absent).

## Bring your own

Swap in real material by changing two lines in the notebook (Parts 2 and 3):

- **`LESSON_PDF`** → any text-based PDF of the day's material (lecture notes, reading, slides
  exported to PDF, the chapter you covered). Same requirements as the curriculum lab:
  text-based (not a scan), roughly 8–50 pages.
- **`TRANSCRIPT_PATH`** → your Zoom transcript. Zoom exports these as `.vtt` (Recording →
  Audio Transcript) or as a `.txt`. Both work. The parser reads the common
  `Speaker Name: text` format and the WebVTT `<v Speaker Name>` voice-tag format.
- **`ROSTER_PATH`** (optional) → a CSV with a `student_name` column (other columns are ignored).
  Without a roster, the notebook can only score students who actually spoke — a fully silent
  student won't appear with a 0.

## ⚠️ Privacy first

Class recordings and transcripts are student records. Before you run this on a real class:

- Make sure recording + transcription is covered by your institution's policy and that students
  were notified (FERPA in the US; your local equivalent elsewhere).
- Keep transcripts on approved storage. Don't paste real student names into anything outside
  your approved environment.
- The score this lab produces is a **draft you review** — never a grade the tool assigns on its
  own. See Part 0 and Part 7 of the notebook.
