import os
from dotenv import load_dotenv
from openai import OpenAI
from groq import Groq

load_dotenv() #charge le fichier .env

PROVIDER = os.getenv("LLM_PROVIDER", "groq").lower() #lit la variable LLM_PROVIDER dans .env. Si elle n'existe pas, elle utilise "groq" par défaut.

DEFAULT_SYSTEM = "You are a Python testing expert."


def ask_llm(prompt: str, system: str = DEFAULT_SYSTEM) -> str:
    """Envoie un prompt au LLM configuré et retourne la réponse texte."""
    if PROVIDER == "groq":
        return _ask_groq(prompt, system)
    # if PROVIDER == "gemini":
        # return _ask_gemini(prompt, system)
    if PROVIDER == "ollama":
        return _ask_ollama(prompt, system)
    raise ValueError(f"Provider inconnu : {PROVIDER}")


def _ask_groq(prompt: str, system: str) -> str:
    
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        raise RuntimeError("GROQ_API_KEY manquante dans .env")
    client = Groq(api_key=api_key)
    resp = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[
            {"role": "system", "content": system},
            {"role": "user", "content": prompt},
        ],
        temperature=0.2,
    )
    return resp.choices[0].message.content

# def _ask_gemini(prompt: str, system: str) -> str:
    
#     api_key = os.getenv("GEMINI_API_KEY")
#     if not api_key:
#         raise RuntimeError("GEMINI_API_KEY manquante dans .env")
#     genai.configure(api_key=api_key)
#     model = genai.GenerativeModel("gemini-1.5-flash")
#     resp = model.generate_content(f"{system}\n\n{prompt}")
#     return resp.text


def _ask_ollama(prompt: str, system: str) -> str:
    
    client = OpenAI(base_url="http://localhost:11434/v1", api_key="EMPTY")
    resp = client.chat.completions.create(
        model="qwen2.5-coder:7b",
        messages=[
            {"role": "system", "content": system},
            {"role": "user", "content": prompt},
        ],
    )
    return resp.choices[0].message.content