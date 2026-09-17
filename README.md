# DTC-Consortium-MLU

**AWS-MLU teaching, learning, and academic innovation resources contributed by the DTCC faculty
community.**

[dtcconsortium.org](https://dtcconsortium.org)

Every contribution here is a self-contained package: documentation, structured metadata, licences,
citation information, and the actual materials. Each has a permanent ID, a version, and its own
download. Anyone can browse and download without signing in.

---

## Browse by category

<!-- BEGIN GENERATED: category-table -->
| Category | What lives there | Published |
|---|---|---|
| **[Course Elements](mlu/course-elements)** | Courses, credentials, modules, lectures, assignments, assessments, instructional materials | _none yet_ |
| **[ML/AI Applications](mlu/ml-ai-applications)** | Prompts, applications, codebases, datasets, tool flows, platforms | **2** |
| **[Professional and Student Development](mlu/professional-student-development)** | Bootcamps, workshops, training, presentations, related initiatives | **3** |
<!-- END GENERATED: category-table -->

**[Browse all materials →](catalog/mlu-contributions.csv)** — the full inventory as a spreadsheet.
The same data is available as [JSON](catalog/mlu-contributions.json) for tooling, and
[collections](collections) group contributions into curated lists such as course kits and cohorts.

**New here?** The [AWS-MLU Faculty AI Sequence](collections#aws-mlu-faculty-ai-sequence) is four
contributions meant to be taught in order, and the best place to start.

---

## Downloading a contribution

Each contribution is released as its own ZIP. There is deliberately **no repository-wide "latest
release"** — you download the one contribution and version you want.

1. Open the contribution, from a category index above.
2. Use the **Download** link in the category table, or the release link in its README.
3. The ZIP contains that contribution's documentation, metadata, licences, and distributable
   materials. Videos and large datasets are not bundled — they appear in an included resource list
   with access instructions.

Where a category table says **_not yet released_**, the materials are browsable in the repository
but no package has been published for them yet. To take a copy in the meantime, clone the
repository and use the contribution's directory:

```bash
git clone https://github.com/DTC-Consortium/DTC-Consortium-MLU.git
```

Each contribution is designed to run straight out of its folder — the notebooks reference their
sample data and helper modules by relative path, so nothing needs rearranging.

---

## Contributing

**→ [`MLU-CONTRIBUTING.md`](MLU-CONTRIBUTING.md)** is the full guide to submitting and updating
materials. Read it before you open anything.

The short version:

1. Open a **[New MLU contribution](../../issues/new?template=new-mlu-contribution.yml)** issue. A
   maintainer assigns you a permanent ID — do not pick one yourself.
2. Copy the [template](templates) for your category and fill it in.
3. Open a pull request. Automated validation checks your metadata; a code owner reviews it.
4. On approval, a maintainer publishes the release.

**Confidential material does not belong in a public issue.** Use the private channel named in
`MLU-CONTRIBUTING.md`.

---

## Reporting problems and requesting updates

| You want to | Do this |
|---|---|
| Report something broken, wrong, or out of date | **[Report a problem](../../issues/new?template=report-problem.yml)** |
| Update materials you contributed | **[Update a contribution](../../issues/new?template=update-mlu-contribution.yml)** |
| Report a licensing or attribution concern | Open a problem report and mark it as licensing. Maintainers treat these as urgent. |
| Report exposed private information | **Do not open a public issue.** Contact the maintainers privately — see `MLU-CONTRIBUTING.md`. |

---

## Attribution and licensing

**Licences differ per contribution and often per file within one.** Always check the
`LICENSE.md` in the contribution you are reusing before you reuse it — do not assume the repository
carries a single blanket licence.

- Most documentation and instructional material is `CC-BY-4.0`: reuse and adapt freely, with credit.
- Most code is `MIT`.
- Bundled sample data keeps the licence of its original source, listed file by file.

Every contribution ships a `CITATION.cff` with the citation its authors ask for. Cite the
contribution, its ID, and the version you used.

**Material owned by AWS, by an institution, or by another third party is not relicensed here.**
Where it is referenced, it is linked rather than redistributed. See
[`LICENSE.md`](LICENSE.md) and [`docs/licensing.md`](docs/licensing.md).

---

## What is not here

This repository is public. By design it holds **no** private drafts, restricted answer keys, student
information, or administrative records. Sample data in every contribution is fabricated or openly
licensed — **no real student record appears anywhere in this repository.**

---

## For maintainers

| | |
|---|---|
| [`ID-REGISTER.md`](ID-REGISTER.md) | The single register of assigned contribution IDs |
| [`docs/handover.md`](docs/handover.md) | **Start here** — setup still outstanding, and how to verify it |
| [`docs/`](docs) | Review, publishing, maintenance, and licensing guidance |
| [`schemas/`](schemas) | Metadata validation rules |
| [`scripts/`](scripts) | Validation, catalog generation, link checking, and packaging |
| [`catalog/taxonomy.yml`](catalog/taxonomy.yml) | Approved categories, disciplines, tools, and audiences |

Category indexes, the catalog, and the collections index are **generated from metadata** — edit
`mlu-contribution.yml`, then run `python3 scripts/build_catalog.py`. Never edit a generated file by
hand.

---

*Maintained by the DTC Consortium MLU maintainers. [dtcconsortium.org](https://dtcconsortium.org)*
