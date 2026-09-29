import ast
from typing import Any


def analyze_code(source: str) -> dict[str, Any]:
    """Analyse un code Python et retourne sa structure.

    Args:
        source: le code Python sous forme de chaîne.

    Returns:
        Un dictionnaire avec les fonctions et les classes trouvées.

    Raises:
        SyntaxError: si le code n'est pas du Python valide.
    """
    tree = ast.parse(source)
    functions: list[dict] = []
    classes: list[dict] = []
    imports: list[str] = []

    for node in tree.body:
        if isinstance(node, ast.FunctionDef):
            functions.append(_extract_function(node))
        elif isinstance(node, ast.ClassDef):
            classes.append(_extract_class(node))
        elif isinstance(node, (ast.Import, ast.ImportFrom)):
            imports.append(ast.unparse(node))

    return {
        "functions": functions,
        "classes": classes,
        "imports": imports,
    }


def _extract_function(node: ast.FunctionDef) -> dict:
    """Extrait les infos d'une fonction."""
    return {
        "name": node.name,
        "args": [a.arg for a in node.args.args],
        "returns": ast.unparse(node.returns) if node.returns else None,
        "docstring": ast.get_docstring(node),
        "lineno": node.lineno,
    }


def _extract_class(node: ast.ClassDef) -> dict:
    """Extrait les infos d'une classe et de ses méthodes."""
    methods = []
    for item in node.body:
        if isinstance(item, ast.FunctionDef):
            methods.append(_extract_function(item))

    return {
        "name": node.name,
        "methods": methods,
        "docstring": ast.get_docstring(node),
        "lineno": node.lineno,
    }