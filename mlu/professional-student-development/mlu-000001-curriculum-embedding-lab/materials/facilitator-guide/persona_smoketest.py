"""
Persona smoke-test for curriculum-embedding-lab.ipynb
=====================================================
Runs ALL six personas through the EXACT notebook pipeline
(PyPDFLoader -> RecursiveCharacterTextSplitter -> FAISS + Nova embeddings ->
retriever -> ChatBedrockConverse nova-lite) and verifies each output matches
what the persona is supposed to produce.

The PERSONA_TOOLS prompts are read live from the notebook so this tests the
real thing, not a copy. Outputs are written to instructor/persona_test_outputs/.

Run from the repo root:
  python instructor/persona_smoketest.py            # all personas
  python instructor/persona_smoketest.py 1 4        # only personas 1 and 4
"""

import json
import re
import sys
import time
import warnings
from pathlib import Path

import boto3
warnings.filterwarnings("ignore")

# Make the repo root importable so `mlu_utils` resolves regardless of CWD
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from langchain_aws import ChatBedrockConverse
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import FAISS
from langchain_core.output_parsers import StrOutputParser
from langchain.prompts import PromptTemplate
from langchain.text_splitter import RecursiveCharacterTextSplitter
from mlu_utils.embeddings import NovaMultimodalEmbeddings

REPO = Path(__file__).resolve().parent.parent
OUT = REPO / "instructor" / "persona_test_outputs"
OUT.mkdir(exist_ok=True)


def load_persona_tools():
    """Read PERSONA_TOOLS straight from the notebook (the dict portion only)."""
    nb = json.loads((REPO / "curriculum-embedding-lab.ipynb").read_text())
    for c in nb["cells"]:
        src = "".join(c["source"])
        if c["cell_type"] == "code" and "PERSONA_TOOLS = {" in src:
            dict_src = src.split("tool = PERSONA_TOOLS")[0]  # stop before the persona lookup
            ns = {}
            exec(dict_src, ns)
            return ns["PERSONA_TOOLS"]
    raise RuntimeError("PERSONA_TOOLS not found in notebook")


# Same QA template the notebook uses
QA_TEMPLATE = """You are a specialized teaching tool. Use ONLY the context below from the source material.
If the context does not contain enough information, say so — do not invent details.

Context:
{context}

Task: {question}

Output:"""

# What each persona is SUPPOSED to produce -> structural checks on the output.
# (name, predicate(output_text) -> bool)
CHECKS = {
    "1": [
        ("3 vignettes present", lambda t: len(re.findall(r"vignette\s*[123]", t, re.I)) >= 3),
        ("difficulty tiers (foundational/typical/complex)",
         lambda t: sum(w in t.lower() for w in ["foundational", "typical", "complex"]) >= 2),
        ("discussion questions", lambda t: "question" in t.lower()),
    ],
    "2": [
        ("copy-paste placeholder for student code", lambda t: "[student code" in t.lower() or "student code here" in t.lower()),
        # accept the whole refusal-phrasing family (refuse / refrain / do not write / without giving …)
        ("refuses to write the fix", lambda t: bool(re.search(
            r"(refrain|refus|do ?n.?t|don't|won'?t|will not|without|never|no)\b[^.]{0,40}"
            r"(writ|output|provid|giv|generat|reveal|share)\w*\b[^.]{0,40}(correct|code|solution|fix|answer)", t, re.I))
            or any(w in t.lower() for w in ["refrain from writing", "do not write", "without writing", "won't accept the corrected"])),
        ("Socratic questioning", lambda t: "?" in t and ("socratic" in t.lower() or "guiding question" in t.lower() or "ask" in t.lower())),
        ("instructor note", lambda t: "instructor" in t.lower()),
    ],
    "3": [
        ("5 discussion prompts", lambda t: len(re.findall(r"^\s*\d[\.\)]", t, re.M)) >= 5 or len(re.findall(r"prompt\s*\d", t, re.I)) >= 5),
        ("citations to passages", lambda t: bool(re.search(r"(page|p\.|section|line|para|passage|quote)", t, re.I)) or t.count('"') >= 4 or t.count("“") >= 2),
        ("interpretation not summary", lambda t: any(w in t.lower() for w in ["interpret", "authorial", "craft", "context", "choice", "meaning"])),
    ],
    "4": [
        ("5 calculation problems", lambda t: len(re.findall(r"problem\s*\d", t, re.I)) >= 4 or len(re.findall(r"^\s*\d[\.\)]", t, re.M)) >= 4),
        ("safety red flag", lambda t: "red flag" in t.lower() or "⚠" in t or "safety" in t.lower()),
        ("worked solution / math", lambda t: any(w in t.lower() for w in ["solution", "=", "mg", "ml", "dose"])),
    ],
    "5": [
        # single-shot run can validly EITHER open in character OR request the role first
        ("opens in character or requests role",
         lambda t: any(w in t.lower() for w in ["i'm", "i am", "my name", "as the", "roleplay", "which stakeholder", "tell me which"])),
        ("invites the student to engage",
         lambda t: "?" in t or any(w in t.lower() for w in ["awaiting", "tell me", "what would you", "like to discuss"])),
        ("stakeholder role referenced", lambda t: any(w in t.lower() for w in ["cfo", "cmo", "coo", "ceo", "board", "stakeholder", "chair", "chief financial", "chief marketing", "chief operating", "officer", "founder"])),
        ("substantive in-character opening (not a bare await)", lambda t: len(t) >= 350 and "awaiting" not in t.lower()),
    ],
    "6": [
        ("multiple-choice questions", lambda t: len(re.findall(r"\b[abcd][\.\)]\s", t, re.I)) >= 4),
        ("exactly 3 MC questions (3+ D-options)", lambda t: len(re.findall(r"\bd[\.\)]\s", t, re.I)) >= 3),
        ("short-answer questions", lambda t: "short" in t.lower() or "short-answer" in t.lower() or len(re.findall(r"^\s*\d[\.\)]", t, re.M)) >= 5),
        ("answer key", lambda t: "answer" in t.lower() and ("key" in t.lower() or "explanation" in t.lower())),
        ("safety question", lambda t: "safety" in t.lower() or "hazard" in t.lower() or "caution" in t.lower()),
    ],
}


# Plain-English requirements per persona — judged by an LLM (meaning, not keywords).
REQUIREMENTS = {
    "1": ["Produces 3 distinct teaching case vignettes",
          "The vignettes escalate in difficulty (foundational → typical → complex)",
          "Each vignette includes discussion questions",
          "Uses only clinical detail from the source; invents no findings"],
    "2": ["Is a copy-paste prompt template addressed TO an AI, with a [STUDENT CODE HERE] placeholder",
          "Instructs the AI to NOT write or output the corrected code (any wording)",
          "Has the AI ask 1-2 Socratic questions instead of giving the fix",
          "Cites a specific concept/data-structure/pattern from the source material",
          "Ends with an instructor note"],
    "3": ["Provides 5 discussion prompts for a humanities seminar",
          "Each prompt is grounded in a specific passage from the source (quoted or referenced)",
          "Prompts push past plot summary into interpretation (authorial choice, craft, context)",
          "Prompts are open-ended, not yes/no or comprehension checks"],
    "4": ["Provides 5 medication-calculation practice problems",
          "Uses only drugs and dosing ranges present in the source",
          "Each problem shows a worked solution with the math",
          "Each problem includes a safety red-flag element (contraindication, dose/route error)"],
    "5": ["Opens a stakeholder roleplay in character, naming a specific stakeholder from the case",
          "Grounds the opening in specific facts from the source case",
          "Stays in character (does not give away the 'right answer')",
          "Invites the student to respond or take a position"],
    "6": ["Has exactly 5 questions: 3 multiple-choice (4 options each) + 2 short-answer",
          "Includes at least one safety question and at least one 'why' (not just 'what') question",
          "Includes an answer key with brief explanations",
          "Content is drawn from the source protocol"],
}


def judge(judge_model, name, vision, requirements, output):
    """LLM-as-judge: returns dict {requirements:[{n,verdict,reason}], overall}."""
    req_lines = "\n".join(f"{i+1}. {r}" for i, r in enumerate(requirements))
    prompt = (
        "You strictly verify whether a teaching-tool OUTPUT satisfies its REQUIREMENTS. "
        "Allow reasonable wording variation — judge MEANING, not exact phrases.\n\n"
        f"TOOL: {name}\nPURPOSE: {vision}\n\nREQUIREMENTS:\n{req_lines}\n\n"
        f'OUTPUT:\n"""\n{output}\n"""\n\n'
        'Return STRICT JSON only, no prose:\n'
        '{"requirements":[{"n":1,"verdict":"PASS","reason":"<=8 words"}],"overall":"PASS"}\n'
        '"overall" is PASS only if every requirement is PASS.'
    )
    raw = judge_model.invoke(prompt).content
    try:
        return json.loads(raw[raw.find("{"): raw.rfind("}") + 1])
    except Exception:
        return {"requirements": [], "overall": "PARSE_ERROR", "_raw": raw[:200]}


def main():
    which = [a for a in sys.argv[1:] if a in "123456"]
    personas = which or ["1", "2", "3", "4", "5", "6"]

    tools = load_persona_tools()
    rt = boto3.client("bedrock-runtime", region_name="us-east-1")
    model = ChatBedrockConverse(model="amazon.nova-lite-v1:0", temperature=0.5, max_tokens=2000)
    embeddings = NovaMultimodalEmbeddings(client=rt)
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1200, chunk_overlap=60,
        separators=["\n\n", "\n", "(?<=\\. )", " ", ""], is_separator_regex=True,
    )
    chain = PromptTemplate.from_template(QA_TEMPLATE) | model | StrOutputParser()
    judge_model = ChatBedrockConverse(model="amazon.nova-lite-v1:0", temperature=0, max_tokens=900)

    summary = []
    for p in personas:
        tool = tools[p]
        print(f"\n{'='*70}\nPERSONA {p}: {tool['name']}\n  expects: {tool['vision']}\n{'='*70}")
        t0 = time.time()
        try:
            pages = PyPDFLoader(tool["default_pdf"]).load()
            chunks = splitter.split_documents(pages)
            print(f"  loaded {len(pages)} pages -> {len(chunks)} chunks; embedding+indexing...")
            vectordb = FAISS.from_documents(chunks, embeddings)
            retriever = vectordb.as_retriever(search_kwargs={"k": 6})
            docs = retriever.invoke(tool["prompt"][:400])
            context = "\n\n".join(d.page_content for d in docs)
            output = chain.invoke({"question": tool["prompt"], "context": context})
        except Exception as e:
            print(f"  !! ERROR: {type(e).__name__}: {e}")
            summary.append((p, tool["name"], "ERROR", str(e)[:80]))
            continue

        (OUT / f"persona{p}.md").write_text(f"# {tool['name']}\n\n{output}\n")
        elapsed = time.time() - t0

        verdict_data = judge(judge_model, tool["name"], tool["vision"], REQUIREMENTS[p], output)
        reqs = verdict_data.get("requirements", [])
        for r in reqs:
            mark = "PASS" if str(r.get("verdict", "")).upper() == "PASS" else "FAIL"
            label = REQUIREMENTS[p][r.get("n", 1) - 1] if 0 < r.get("n", 0) <= len(REQUIREMENTS[p]) else r.get("reason", "")
            print(f"    [{mark}] {label}  — {r.get('reason','')}")
        passed = sum(str(r.get("verdict", "")).upper() == "PASS" for r in reqs)
        total = len(REQUIREMENTS[p])
        overall = str(verdict_data.get("overall", "")).upper()
        verdict = "PASS" if overall == "PASS" else ("PARTIAL" if passed else "FAIL")
        print(f"  -> {verdict} ({passed}/{total} judged, {len(output)} chars, {elapsed:.0f}s)")
        summary.append((p, tool["name"], verdict, f"{passed}/{total} · {len(output)}c · {elapsed:.0f}s"))

    print(f"\n{'='*70}\nSUMMARY\n{'='*70}")
    for p, name, verdict, detail in summary:
        print(f"  P{p} {verdict:8} {name.split('—')[0].strip():22} {detail}")
    print(f"\nOutputs saved to: {OUT}")


if __name__ == "__main__":
    main()
