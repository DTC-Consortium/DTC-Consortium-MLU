# Licensing and rights clearance

For contributors deciding what they can share, and reviewers deciding what can be published.

The root [`LICENSE.md`](../LICENSE.md) describes how licensing is structured. This document is about
the judgment calls.

## The rule

**Confirm reuse rights before publishing. Do not apply a blanket licence to material owned by AWS,
by an institution, or by any other third party without authorization.**

When redistribution is not permitted, **link to the original**. A link that works is worth more than
a copy that has to be taken down.

## One contribution, several licences

This is normal. A typical contribution has:

- Instructional prose under `CC-BY-4.0`
- Code under `MIT`
- Sample data under whatever each file's source carries

`LICENSE.md` records this as a table, generated from `mlu-contribution.yml`. Anyone reusing one file
should be able to find that file's row without reading anything else.

## Sample data

Sample data causes more licensing problems than anything else, because it is easy to grab and easy
to forget.

**Where good sample data comes from:**

| Source | Watch for |
|---|---|
| Material you authored yourself | Nothing — say so, and licence it |
| Openly licensed work (`CC-BY`, `CC0`) | Record the source, the licence, and the extent used |
| Public domain | Confirm it really is, in the jurisdictions that matter |
| Fabricated — invented people, papers, transcripts | Say plainly that it is fabricated |

**Where it must not come from:**

- Real student work, even anonymized. Anonymization is not reliable at this scale, and consent for
  one use is not consent for publication.
- Publisher material, question banks, or textbook figures.
- Scraped content whose licence you have not checked.

Every bundled file needs a row in `licenses.data` with its path, licence, and source. If you cannot
fill that row, do not bundle the file.

### Content notes

Some legitimately licensed material needs a warning rather than removal. A public-domain
nineteenth-century text may preserve period racial language; a clinical case may carry graphic
detail. Where that is part of why the material works, keep it and put a note in `licenses.data` and
in the contribution README, so it reaches a facilitator before it reaches a room.

## AWS material specifically

This repository holds materials developed *through* AWS-MLU programs. That is not the same as
holding *AWS's* materials.

**Yours to share:** what you wrote — your lab, your notebook, your rubric, your slides — even when
it was developed during an AWS-supported program and uses AWS services.

**Not yours to relicense:** AWS course content, AWS branding and logos, AWS documentation text,
workshop materials authored by AWS.

Referring to AWS services, naming models, and including code that calls AWS APIs is all fine. Copying
AWS's own instructional text into your contribution is not.

## Derived and adapted work

Adapting someone else's openly licensed material is encouraged, and has requirements:

- Credit the original author and link the source.
- Name the original licence and comply with it. `CC-BY-SA` means your adaptation must be `CC-BY-SA`
  too; `CC-BY-NC` blocks commercial reuse downstream, which limits who can use your contribution.
- State what you changed.

Record all of this in `licenses.data` with a `notes` entry.

## Things that can never be published here

Regardless of licence, this repository is public. It never holds:

- Real student records, in any form.
- Restricted answer keys and unreleased assessments.
- Credentials, API keys, tokens, or account identifiers.
- Administrative or personnel records.
- Private drafts not intended for publication.

These belong in whatever private system your institution already uses. If material like this needs
to reach maintainers, use the approved private channel described in
[`MLU-CONTRIBUTING.md`](../MLU-CONTRIBUTING.md).

## If something was published that should not have been

Act first. Remove the content and any release asset containing it, then work out how it happened.
Report it privately, not in a public issue — see [`maintenance.md`](maintenance.md).

## When you are unsure

Ask before publishing, not after. An unanswered licensing question is a reason to hold a
contribution back, and no reviewer will think less of a contributor for raising one.
