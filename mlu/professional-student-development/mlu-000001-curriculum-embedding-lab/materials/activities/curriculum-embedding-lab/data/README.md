# Sample documents — Curriculum Embedding Lab

Six discipline-specific sample documents, one per persona, used by
`../curriculum-embedding-lab.ipynb` (faculty) and `../study-mastery-lab.ipynb` (students).

## Why these exist

Per the locked design decisions (see `../instructor/SEMINAR_PLAN.md`), the lab does **not** rely on
participants bringing their own PDFs. Every participant gets a pre-staged, licence-clean sample
matched to their persona, so the lab runs out of the box with no prep.

## The six samples

All six are staged, text-extractable, and verified against `pypdf` — the same loader
`PyPDFLoader` uses.

| Persona | Filename | Pages | Source and licence |
|---|---|:---:|---|
| 1. Dentistry | `persona1_dentistry_perio_case.pdf` | 8 | Cureus 2026 case report, **CC-BY 4.0**: "Clinical Management of Localized Aggressive Periodontitis with Esthetic Replacement of Tooth 11 Using a Resin-Bonded Bridge" — Abulfateh et al. |
| 2. Computer Science | `persona2_cs_data_structures.pdf` | 31 | *Open Data Structures* by Pat Morin, **CC-BY**, Ch. 1 extract. The most-tested sample — also the default for the student lab and for the participation and grading labs. |
| 3. English Literature | `persona3_english_victorian_essay.pdf` | 16 | Mary Seacole, *Wonderful Adventures of Mrs. Seacole in Many Lands* (1857), Chapters I–IV. **Public domain**, via Project Gutenberg eBook [#23031](https://www.gutenberg.org/ebooks/23031). Typeset to PDF from the plain-text edition on 2026-08-31; chapters reproduced verbatim, Gutenberg front matter and licence text omitted. |
| 4. Nursing | `persona4_nursing_pharmacology.pdf` | 9 | Original instructional material authored for this seminar (cardiovascular pharmacology). Licence-clean; no rights reserved. |
| 5. Business | `persona5_business_leadership_case.pdf` | 7 | Original fictional teaching case authored for this seminar ("Northwind Logistics"). Licence-clean; all figures and people invented. |
| 6. Biology | `persona6_biology_lab_protocol.pdf` | 8 | Original wet-lab protocol authored for this seminar (agarose gel electrophoresis). Licence-clean; no rights reserved. |

**A note on persona 3.** The Seacole text preserves original nineteenth-century spelling,
punctuation, and racial language. That language is itself an object of scholarly analysis and is
part of why the document works for this persona — but flag it for participants rather than letting
it arrive unannounced.

## Student lab default, and bringing your own

The student lab (`../study-mastery-lab.ipynb`) defaults `SOURCE_PDF` to
`persona2_cs_data_structures.pdf` so it runs immediately. Students swap in their own material by
dropping a text-based PDF into this folder and changing the `SOURCE_PDF` line in Part 2.

## Requirements for any document you add

- **Licence:** public domain, CC-BY, CC-BY-SA, or explicit open access. **No** copyrighted
  textbooks, Harvard Business cases, or paywalled journal articles.
- **Length:** 8–30 pages is the comfortable range. Hard cap **50 pages** — beyond that the
  notebook's embedding-time budget breaks down.
- **Format:** text-based PDF, **not** a scan. `PyPDFLoader` cannot read image-only PDFs. OCR
  scanned material first.
- **Content quality:** realistic to actual teaching workflow — the kind of document a faculty
  member in that discipline would genuinely hand to a student or TA.
- **No student work.** These are teaching materials. Don't stage student submissions here.

## Test a document before you teach with it

1. Drop the file into this folder.
2. Open `../curriculum-embedding-lab.ipynb`.
3. Set `persona = "X"` in the Part 0 cell (or point that persona's `default_pdf` at your file).
4. Run Parts 1 and 2 end to end.
5. Confirm:
   - [ ] Loads without errors, and reports a non-zero page count
   - [ ] Chunks to roughly 15–60 chunks
   - [ ] Embedding completes in under 90 seconds
   - [ ] Quiz / study-guide / rubric outputs are substantive, not generic
   - [ ] The grounded vs. vanilla comparison shows a meaningful difference

`../instructor/persona_smoketest.py` runs all six personas at once and is the faster way to check
the whole set before a delivery.
