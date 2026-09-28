# 🧪 Py Test Generator

Générateur de tests Python propulsé par IA, avec exécution sandboxée.

## Fonctionnalités

- Upload d'un fichier Python
- Analyse automatique (fonctions, classes, signatures)
- Génération de tests pytest par LLM
- Exécution isolée dans Docker
- Rapport de résultats

## Stack

- Streamlit (UI)
- Groq / Gemini / Ollama (LLM)
- Docker (sandbox)
- pytest + coverage

## Installation

    python -m venv .venv
    .venv\Scripts\activate
    pip install -r requirements.txt

## Configuration

Copie `.env.example` en `.env` et renseigne ta clé API.

## Lancer

    streamlit run app.py

## Statut

En développement — phase 1 : architecture