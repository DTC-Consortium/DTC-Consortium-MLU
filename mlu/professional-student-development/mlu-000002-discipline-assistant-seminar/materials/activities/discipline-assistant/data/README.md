# Sample documents — Discipline-Specific AI Teaching Assistant

Six discipline-specific sample documents, one per persona, used by
`../discipline-assistant.ipynb` (SageMaker + Bedrock).

The Colab notebook (`../discipline-assistant-colab.ipynb`) does **not** read this folder — it
downloads a sample document at runtime in Part 2, so it works from a single file with nothing
else cloned.

## Why these exist

The lab does **not** rely on participants bringing their own PDFs. Every participant gets a
pre-staged, licence-clean sample matched to their persona, so the lab runs out of the box.

These are the same six documents as the
[Curriculum Embedding Lab](../../../../../mlu-000001-curriculum-embedding-lab/materials/activities/curriculum-embedding-lab/data), deliberately — a participant
who runs both labs sees familiar material and can focus on what changed.

## The six samples

All six are staged, text-extractable, and verified against `pypdf` — the same loader
`PyPDFLoader` uses.

| Persona | Filename | Pages | Source and licence |
|---|---|:---:|---|
| 1. Dentistry | `persona1_dentistry_perio_case.pdf` | 8 | Cureus 2026 case report, **CC-BY 4.0**: "Clinical Management of Localized Aggressive Periodontitis with Esthetic Replacement of Tooth 11 Using a Resin-Bonded Bridge" — Abulfateh et al. |
| 2. Computer Science | `persona2_cs_data_structures.pdf` | 31 | *Open Data Structures* by Pat Morin, **CC-BY**, Ch. 1 extract. The most-tested sample. |
| 3. English Literature | `persona3_english_victorian_essay.pdf` | 16 | Mary Seacole, *Wonderful Adventures of Mrs. Seacole in Many Lands* (1857), Chapters I–IV. **Public domain**, via Project Gutenberg eBook [#23031](https://www.gutenberg.org/ebooks/23031). Typeset to PDF from the plain-text edition on 2026-08-31; chapters reproduced verbatim, Gutenberg front matter and licence text omitted. |
| 4. Nursing | `persona4_nursing_pharmacology.pdf` | 9 | Original instructional material authored for this seminar (cardiovascular pharmacology). Licence-clean; no rights reserved. |
| 5. Business | `persona5_business_leadership_case.pdf` | 7 | Original fictional teaching case authored for this seminar ("Northwind Logistics"). Licence-clean; all figures and people invented. |
| 6. Biology | `persona6_biology_lab_protocol.pdf` | 8 | Original wet-lab protocol authored for this seminar (agarose gel electrophoresis). Licence-clean; no rights reserved. |

**Persona 3 is the one to demo to a skeptical audience.** That persona represents the faculty
member who believes AI erodes critical thinking, so the demo has to show that grounding
*preserves* close reading rather than replacing it — answers that cite specific passages, and
discussion prompts that push toward analysis rather than plot recap.

Note that the Seacole text preserves original nineteenth-century spelling, punctuation, and racial
language. That language is itself an object of scholarly analysis and is part of why the document
suits this persona — but flag it for participants rather than letting it arrive unannounced.

## Requirements for any document you add

- **Licence:** public domain, CC-BY, CC-BY-SA, or explicit open access. **No** copyrighted
  textbooks, Harvard Business cases, or paywalled journal articles.
- **Length:** 8–30 pages is the comfortable range. Hard cap **50 pages**.
- **Format:** text-based PDF, **not** a scan. `PyPDFLoader` cannot read image-only PDFs.
- **Content quality:** realistic to actual teaching workflow.
- **No student work.** These are teaching materials, not student submissions. On the Colab path,
  remember the document is sent to Hugging Face's Inference API — use published or openly licensed
  material only.

## Test a document before you teach with it

1. Drop the file into this folder.
2. Open `../discipline-assistant.ipynb`.
3. Point the PDF path variable at `data/personaX_...`.
4. Run Parts 3 and 4 end to end.
5. Confirm:
   - [ ] Loads without errors, and reports a non-zero page count
   - [ ] Chunks to roughly 15–60 chunks
   - [ ] Embedding completes in under 90 seconds
   - [ ] Quiz / study-guide / rubric outputs are substantive, not generic
   - [ ] The grounded vs. vanilla comparison shows a meaningful difference
