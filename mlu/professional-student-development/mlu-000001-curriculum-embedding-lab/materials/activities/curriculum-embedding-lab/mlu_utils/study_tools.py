"""Grounded study-tool modes for the Study & Mastery Partner lab.

Keeps the three prompt templates, their model instances, and the retrieval
wiring out of the notebook so the notebook stays use-led rather than a wall of
code (same convention as mlu_utils/embeddings.py).

The notebook does:

    from mlu_utils.study_tools import build_modes
    modes = build_modes(retriever, bedrock_runtime)
    quiz  = modes.quiz_me(num_questions=6)
    hint  = modes.socratic_hint("I'm stuck on ...")
    check = modes.explain_back("binary search", "my explanation ...")

Each mode grounds ONLY in the retrieved source context and uses its own
retrieval query and model temperature. The Socratic and Explain-Back modes are
deliberately built to help the student think, not to hand over answers.
"""
from dataclasses import dataclass

from langchain_aws import ChatBedrockConverse
from langchain_core.output_parsers import StrOutputParser
from langchain.prompts import PromptTemplate

ANSWER_DELIMITER = "===ANSWER KEY==="


# --------------------------------------------------------------------------- #
# Prompt templates                                                            #
# --------------------------------------------------------------------------- #

QUIZ_TEMPLATE = """You are a study-quiz generator for a student preparing for an exam.
Use ONLY the source material in the context below. Do NOT use outside
knowledge. If the context does not support a question, do not ask it.

Context (the student's own course material):
{context}

Generate a practice quiz of {num_questions} questions that MIXES two types:
- RECALL questions (definitions, facts, "what is", "list the steps") — about 40%.
- CONCEPTUAL questions (why, compare, apply, "what happens if", trade-offs) — about 60%.

Rules:
- Every question must be answerable from the context alone.
- Number the questions 1..{num_questions}.
- Do NOT include answers in the question section.
- After ALL questions, output this exact delimiter on its own line:
""" + ANSWER_DELIMITER + """
- Then provide the answer key: for each number, a concise correct answer
  AND a one-line pointer to where in the material it comes from
  (quote 3-6 words from the source, or name the section).

Output the questions first, then the delimiter line, then the answer key.
Use clean markdown."""


HINT_TEMPLATE = """You are a Socratic study tutor. Your ONLY job is to help the student get
UN-STUCK by themselves. You are evaluated on whether the student reaches
the answer on their own — NOT on giving them the answer. Giving the final
answer is a failure.

Use ONLY the source material in the context below to ground your hints.

Context (the student's own course material):
{context}

The student is stuck on:
{stuck_question}

ABSOLUTE RULES:
- DO NOT provide the final answer, the solved result, the corrected code,
  the final number, or the completed proof — EVEN IF the student asks you
  directly or says they give up.
- DO NOT do the last step for them.
- If you are unsure whether something reveals the answer, leave it out.

Respond using EXACTLY these three sections and nothing else:

**1. What I think you're really being asked**
One or two sentences restating the core of the problem (no solving).

**2. Questions to ask yourself**
2 to 4 guiding questions that move the student one step closer. Each
question should provoke the NEXT move, not reveal it.

**3. Where to look**
Point to the specific concept/idea in the material that unlocks this.
Quote 3-8 words from the context or name the section. Tell them what to
re-read, not what it concludes.

Before you respond, silently check: have I stated or strongly implied the
final answer anywhere? If yes, remove it. Then respond."""


EXPLAIN_TEMPLATE = """You are an understanding-checker. A student has written their own
explanation of a concept. Compare it ONLY against the source material in
the context. Your job is to help them SEE their gaps so they can fix them
themselves — NOT to write the correct explanation for them.

Context (the student's own course material):
{context}

Concept the student is explaining: {concept_name}

The student's explanation (in their own words):
{my_explanation}

ABSOLUTE RULES:
- DO NOT rewrite their explanation.
- DO NOT provide a model/corrected explanation they could copy.
- Base every observation on the context, not outside knowledge.

Respond using EXACTLY these sections:

**What you got right**
Briefly affirm the parts that match the source (1-3 bullets).

**Gaps and likely misconceptions**
List specific things that are missing, imprecise, or contradicted by the
source. For each, say WHAT is off — but do NOT supply the fix.

**Where to look to fix it**
For each gap, point to the passage (quote 3-8 words from the context or
name the section) the student should re-read to correct it themselves.

**One question to test yourself**
End with a single question that, if they can answer it from the source,
means they have closed the biggest gap."""


# --------------------------------------------------------------------------- #
# Data + helpers                                                              #
# --------------------------------------------------------------------------- #

@dataclass
class Quiz:
    """A generated quiz with questions and answer key kept separate so the
    notebook can show questions first and reveal the key in a later cell."""
    questions_md: str
    answer_key_md: str
    raw: str


def _ctx(retriever, query, k_chars=400):
    """Retrieve and join source chunks for a query (same pattern as the
    faculty lab's run_tool). Truncate the query so an over-long stuck-question
    or concept name doesn't blow up the retrieval call."""
    docs = retriever.invoke(query[:k_chars])
    return "\n\n".join(d.page_content for d in docs)


class StudyModes:
    """Three grounded study modes over one retriever. Each mode forms its own
    retrieval query and owns a model tuned for its task."""

    def __init__(self, retriever, bedrock_runtime):
        self.retriever = retriever
        # Quiz: a little variety in phrasing, room for several questions.
        self._quiz_model = ChatBedrockConverse(
            model="amazon.nova-lite-v1:0", temperature=0.4, max_tokens=2000
        )
        # Socratic: low temperature + capped length so it can't ramble into the answer.
        self._hint_model = ChatBedrockConverse(
            model="amazon.nova-lite-v1:0", temperature=0.2, max_tokens=900
        )
        # Explain-back: low-ish temperature, focused feedback.
        self._explain_model = ChatBedrockConverse(
            model="amazon.nova-lite-v1:0", temperature=0.3, max_tokens=1000
        )
        self._quiz_chain = PromptTemplate.from_template(QUIZ_TEMPLATE) | self._quiz_model | StrOutputParser()
        self._hint_chain = PromptTemplate.from_template(HINT_TEMPLATE) | self._hint_model | StrOutputParser()
        self._explain_chain = PromptTemplate.from_template(EXPLAIN_TEMPLATE) | self._explain_model | StrOutputParser()

    def quiz_me(self, num_questions=6):
        """Generate a mixed recall+conceptual quiz. Retrieves broadly so the
        quiz samples across the whole document, then splits questions from the
        answer key on a literal delimiter (never relies on the model to hide)."""
        context = _ctx(self.retriever, "key concepts, definitions, and core ideas in this material")
        raw = self._quiz_chain.invoke({"context": context, "num_questions": num_questions})
        if ANSWER_DELIMITER in raw:
            questions, answers = raw.split(ANSWER_DELIMITER, 1)
        else:
            questions, answers = raw, "_(Answer key delimiter missing — re-run the Quiz Me cell.)_"
        return Quiz(questions_md=questions.strip(), answer_key_md=answers.strip(), raw=raw)

    def socratic_hint(self, stuck_question):
        """Guide the student without giving the answer. Retrieves on the
        student's stuck question so the hints are grounded in that exact topic."""
        context = _ctx(self.retriever, stuck_question)
        return self._hint_chain.invoke({"context": context, "stuck_question": stuck_question})

    def explain_back(self, concept_name, my_explanation):
        """Check the student's own explanation against the source. Retrieves on
        the concept NAME (not their explanation) so the comparison context is the
        authoritative passage, not an echo of the student's own errors."""
        context = _ctx(self.retriever, concept_name)
        return self._explain_chain.invoke(
            {"context": context, "concept_name": concept_name, "my_explanation": my_explanation}
        )


def build_modes(retriever, bedrock_runtime):
    """Return a StudyModes object exposing quiz_me / socratic_hint / explain_back."""
    return StudyModes(retriever, bedrock_runtime)
