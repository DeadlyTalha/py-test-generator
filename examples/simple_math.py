"""Petites fonctions mathématiques pour tester l'analyseur."""


def add(a: int, b: int) -> int:
    """Additionne deux entiers."""
    return a + b


def divide(a: float, b: float) -> float:
    """Divise a par b. Lève ZeroDivisionError si b vaut 0."""
    if b == 0:
        raise ZeroDivisionError("division par zéro")
    return a / b


class Calculator:
    """Une calculatrice simple."""

    def __init__(self, value: float = 0):
        self.value = value

    def add(self, x: float) -> float:
        self.value += x
        return self.value

    def reset(self) -> None:
        self.value = 0