from typing import TypeVar

from smart_lambda.lexeme import Parameter
from smart_lambda.interpreter.interpreter_lexeme import InterpreterLexeme

# Define type-variable for lexeme return-type
T = TypeVar('T')


class InterpreterParameter(InterpreterLexeme):
    """
    TODO
    """
    # List of valid lexemes for the lexeme-interpreter
    lexemes = \
        [
            Parameter
        ]

    @classmethod
    def interpret(cls, lexeme: Parameter, **kwargs) -> T:
        """
        Interprets the given parameter and returns its value.

        :param lexeme: Parameter to interpret
        :param kwargs: Dictionary containing arguments for lambda-function

        :return: Value of parameter
        """
        super().interpret(lexeme)

        # Invalid argument
        if lexeme.name not in kwargs:
            return None

        return kwargs[lexeme.name]
