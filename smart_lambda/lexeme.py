from __future__ import annotations
from typing import TypeVar

# Define type-variable for constant type
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


class Parameter:
    """
    Class for parameter-lexeme.
    """
    def __init__(self, name: str):
        """
        Initialize parameter based on it's name

        :param name: Name of parameter
        """
        self.name: str = name

    def __repr__(self):
        return self.name

    def __eq__(self, other: Parameter) -> bool:
        """
        Compare two parameter for equality

        :param other: Parameter to compare against

        :return: True / False
        """
        return self.name == other.name
