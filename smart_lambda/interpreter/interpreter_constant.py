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
    def interpret(cls, interpreter_base, lexeme: Constant, **kwargs) -> T:
        """
        Interprets the given constant and returns its value.

        :param interpreter_base Reference to base-interpreter (InterpreterLambda)
        :param lexeme: Constant to interpret
        :param kwargs: Dictionary containing arguments for lambda-function

        :return: Value of constant
        """
        super().interpret(interpreter_base, lexeme, **kwargs)

        return lexeme.value
