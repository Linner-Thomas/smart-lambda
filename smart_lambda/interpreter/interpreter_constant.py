from typing import TypeVar

from smart_lambda.lexeme import Constant
from smart_lambda.interpreter.interpreter_lexeme import InterpreterLexeme

# Define type-variable for lexeme return-type
T = TypeVar('T')


class InterpreterConstant(InterpreterLexeme):
    """
    TODO
    """
    # List of valid lexemes for the lexeme-interpreter
    lexemes = \
        [
            Constant
        ]

    @classmethod
    def interpret(cls, lexeme: Constant) -> T:
        """
        Interprets the given constant and returns its value.

        :param lexeme: Constant to interpret

        :return: Value of constant
        """
        super().interpret(lexeme)

        return lexeme.value
