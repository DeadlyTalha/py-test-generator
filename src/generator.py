import re

from src.llm import ask_llm
from src.analyzer import analyze_code
from src.prompts import SYSTEM_PROMPT, build_user_prompt


def clean_llm_output(raw: str) -> str:
    """Retire les balises markdown et le bruit autour du code."""
    text = raw.strip()

    # Retirer les blocs markdown ```python ... ```
    text = re.sub(r"^```(?:python)?\s*\n", "", text)
    text = re.sub(r"\n```\s*$", "", text)

    # Retirer d'éventuelles lignes d'intro du type "Voici les tests :"
    lines = text.splitlines()
    while lines and not lines[0].lstrip().startswith(
        ("import ", "from ", "def ", "class ", "#", "@")
    ):
        lines.pop(0)
    text = "\n".join(lines)

    return text.strip()


def generate_tests(source: str) -> dict:
    """Génère les tests pour un code source donné.

    Returns:
        Un dictionnaire avec les clés :
        - 'tests': le code des tests générés
        - 'analysis': la structure extraite du code
        - 'raw_length': la longueur de la réponse brute du LLM
    """
    analysis = analyze_code(source)
    prompt = build_user_prompt(source, analysis)

    raw = ask_llm(prompt, system=SYSTEM_PROMPT)
    tests = clean_llm_output(raw)

    return {
        "tests": tests,
        "analysis": analysis,
        "raw_length": len(raw),
    }