"""Sample rubric for the Paper Autograding Lab.

This is the file the faculty member edits. It is plain Python so you can read it
top to bottom and change it without learning a schema — the only thing that has
to be true is that it defines a dict named RUBRIC with a `criteria` list.

Each criterion has:
  - name        : shown to the student and used to line up the model's scores
  - weight      : relative weight (these are percentages here, but they only
                  have to be relative — the code normalizes them to sum to 100)
  - description : one line on what the criterion measures
  - levels      : the 0-4 descriptors, i.e. what each tier looks like

The sample is written for a short paper in an intro Data Structures course, to
match the bundled course material (persona2_cs_data_structures.pdf). Swap the
whole thing for your own assignment's rubric.
"""

RUBRIC = {
    "max_tier": 4,

    # Percentage cutoffs for the letter grade. Delete this to accept the
    # sensible default in paper_tools.DEFAULT_GRADE_BANDS.
    "grade_bands": [
        [93, "A"], [90, "A-"], [87, "B+"], [83, "B"], [80, "B-"],
        [77, "C+"], [73, "C"], [70, "C-"], [60, "D"], [0, "F"],
    ],

    "criteria": [
        {
            "name": "Thesis & Argument",
            "weight": 25,
            "description": "Is there a clear central claim, and does the paper argue it coherently?",
            "levels": {
                4: "Clear, specific, arguable thesis; every section advances it; no drift.",
                3: "Clear thesis; argument mostly stays on track with minor digression.",
                2: "A thesis is present but vague, or the argument wanders from it.",
                1: "No real thesis, or the paper is a summary with no argument.",
                0: "Off-prompt or missing.",
            },
        },
        {
            "name": "Use of Course Concepts",
            "weight": 35,
            "description": "Does the paper use the data-structures concepts from the course material correctly?",
            "levels": {
                4: "Uses course concepts precisely and correctly; applies them to new cases.",
                3: "Uses the concepts correctly with minor imprecision.",
                2: "References course concepts but with a notable error or shallow use.",
                1: "Mentions terms without understanding, or misuses the concepts.",
                0: "No engagement with course concepts.",
            },
        },
        {
            "name": "Evidence & Support",
            "weight": 25,
            "description": "Are claims backed by examples, complexity analysis, or citations from the material?",
            "levels": {
                4: "Every major claim is supported with a concrete example or correct analysis.",
                3: "Most claims are supported; a few asserted without backing.",
                2: "Some support, but key claims are unsupported assertion.",
                1: "Largely unsupported opinion.",
                0: "No supporting evidence at all.",
            },
        },
        {
            "name": "Clarity & Structure",
            "weight": 15,
            "description": "Is the writing organized and readable — intro, body, conclusion, clean prose?",
            "levels": {
                4: "Tight structure and clean prose; easy to follow throughout.",
                3: "Well organized; occasional awkward passage.",
                2: "Understandable but disorganized or repetitive in places.",
                1: "Hard to follow; little structure.",
                0: "Incoherent.",
            },
        },
    ],
}
