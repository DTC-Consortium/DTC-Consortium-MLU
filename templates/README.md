# Templates

Starting points for a new contribution. Copy the folder for your category, rename it
`<your-id>-<short-slug>`, and fill it in.

> ### These are templates, not published faculty contributions
>
> Nothing in this directory is real teaching material, and nothing here is listed in the catalog or
> any category index. The example text is illustrative — replace all of it.

| Template | For |
|---|---|
| [`course-elements/`](course-elements) | Courses, credentials, modules, lectures, assignments, assessments, instructional materials |
| [`ml-ai-applications/`](ml-ai-applications) | Prompts, applications, codebases, datasets, tool flows, platforms |
| [`professional-student-development/`](professional-student-development) | Bootcamps, workshops, training, presentations, related initiatives |

## Using one

```bash
# 1. A maintainer has assigned you an ID — say mlu-000042.
cp -r templates/course-elements mlu/course-elements/mlu-000042-responsible-ai-module
cd mlu/course-elements/mlu-000042-responsible-ai-module

# 2. Fill in mlu-contribution.yml, then README.md and CHANGELOG.md.
#    LICENSE.md and CITATION.cff are generated — do not write them by hand.

# 3. Put your materials under materials/, and delete the folders you did not use.

# 4. From the repository root:
pip install -r scripts/requirements.txt
python3 scripts/generate_boilerplate.py
python3 scripts/build_catalog.py
python3 scripts/validate_contributions.py
```

The full guide is [`MLU-CONTRIBUTING.md`](../MLU-CONTRIBUTING.md).

## A note on `materials/`

Each template ships the folders that usually suit its category. **Delete the ones you do not use** —
an empty folder tells a reader nothing.

And keep runnable things runnable. If a notebook loads data and helper modules by relative path,
keep them together in one folder rather than scattering them to match the suggested names. A layout
someone has to rearrange before it runs is a worse layout; just explain what you did in your README.
