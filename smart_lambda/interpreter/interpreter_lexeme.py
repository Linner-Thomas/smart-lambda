from typing import TypeVar

from smart_lambda.lexeme import Lexeme

# Define type-variable for lexeme return-type
T = TypeVar('T')


class InterpreterLexeme:
    """
    TODO
    """
    # List of valid lexemes for the lexeme-interpreter
    lexemes = []

    @classmethod
    def interpret(cls, interpreter_base, lexeme: Lexeme, **kwargs) -> T:
        """
        Interprets the given lexeme and returns its return value.

        This method has to be overridden by each lexeme-interpreter.

        :param interpreter_base Reference to base-interpreter (InterpreterLambda)
        :param lexeme: Lexeme to interpret
        :param kwargs: Dictionary containing arguments for lambda-function

        :return: Return-Value of lexeme
        """
        pass

    @classmethod
    def is_valid_lexeme(cls, lexeme: Lexeme) -> bool:
        """
        Check whether the given lexeme is valid for the lexeme-interpreter.

        :param lexeme: Lexeme to check

        :return: True / False
        """
        return type(lexeme) in cls.lexemes
