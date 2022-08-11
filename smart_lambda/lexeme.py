from __future__ import annotations
from typing import List, TypeVar

from enum import Enum

# Define type-variable for constant type
T = TypeVar('T')


class Lexeme:
    pass


class Constant(Lexeme):
    """
    Wrapper-Class for constant-lexeme.
    """
    def __init__(self, value: T):
        """
        Initialize constant based on its value.

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


class Parameter(Lexeme):
    """
    Class for parameter-lexeme.
    """
    def __init__(self, name: str):
        """
        Initialize parameter based on its name

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


class BinaryOperations(Enum):
    ADD = '+'
    SUB = '-'
    MUL = '*'
    DIV_TRUE = '/'
    DIV_FLOOR = '//'
    MOD = '%'
    AND = '&'
    OR = '|'
    XOR = '^'
    SHIFT_L = '<<'
    SHIFT_R = '>>'


class BinaryOperation(Lexeme):
    """
    Class for binary-operation lexeme (e. g. ADD, MUL, ...).
    """
    def __init__(self, operation: BinaryOperations, operands: List[Lexeme]):
        """
        Initialize binary-operation based on its operation and operands

        :param operation: Operation (e. g. ADD)
        :param operands:  Operands (Constant, Parameter)
        """
        self.operation: BinaryOperations = operation
        self.operands: List[Lexeme] = operands

    def __repr__(self):
        return f"{self.operands[0]} {self.operation.value} {self.operands[1]}"

    def __eq__(self, other: BinaryOperation) -> bool:
        """
        Compare two binary-operations for equality

        :param other: Binary-Operation to compare against

        :return: True / False
        """
        return self.operation == other.operation and self.operands == other.operands
