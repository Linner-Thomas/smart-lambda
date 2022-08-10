from __future__ import annotations
from typing import TypeVar

T = TypeVar('T')


class Constant:
    """
    Wrapper-Class for constant-lexeme.
    """
    def __init__(self, value: T):
        """
        Initialize constant based on it's value.

        :param value: Value of constant
        """
        self.value: T = value
        self.type: type = type(value)

    def __repr__(self) -> str:
        return str(self.value)

    def __eq__(self, other: Constant) -> bool:
        """
        Compare two constants for equality.

        :param other: Constant to compare against

        :return: True / False
        """
        return self.type == other.type and self.value == other.value
