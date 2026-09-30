import json


SYSTEM_PROMPT = """Tu es un expert en tests Python avec pytest.

Tu génères des tests clairs, lisibles et robustes qui couvrent :
- les cas nominaux (fonctionnement normal),
- les cas limites (0, None, listes vides, chaînes vides, valeurs extrêmes),
- les exceptions attendues (avec pytest.raises),
- les effets de bord si pertinent.

Règles STRICTES :
- Utilise UNIQUEMENT pytest et la bibliothèque standard Python.
- N'utilise JAMAIS de réseau, de fichiers réels, ni de time.sleep.
- N'invente JAMAIS de fonctions : teste uniquement ce qui existe dans le code fourni.
- Chaque test doit avoir un nom explicite qui décrit ce qu'il vérifie.
- Retourne UNIQUEMENT le code Python des tests.
- Ne mets PAS de balises markdown (```python).
- Ne mets AUCUNE explication avant ou après le code.
"""


def build_user_prompt(source: str, analysis: dict) -> str:
    """Construit le prompt utilisateur à partir du code et de son analyse."""
    analysis_str = json.dumps(analysis, indent=2, ensure_ascii=False)

    return f"""Voici un module Python :

```python
{source}
Structure extraite automatiquement :
{analysis_str}

Génère une suite complète de tests pytest pour ce module.

Contraintes techniques :

Le fichier de tests s'appellera test_generated.py.

Importe le module testé avec import module_under_test.

N'écris AUCUN import du module lui-même dans le fichier (on s'en occupe).

Utilise import pytest si tu as besoin de pytest.raises.

Chaque fonction publique doit avoir au moins 2 tests (cas normal + cas limite).

Chaque méthode publique de classe doit avoir au moins 1 test.

Retourne uniquement le code Python des tests, sans texte autour.
"""