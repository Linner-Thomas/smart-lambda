from typing import List, TypeVar, Union

from smart_lambda.lexeme import Lexeme
from smart_lambda.interpreter.interpreter_lexeme import InterpreterLexeme

# Define type-variable for lambda return-type
T = TypeVar('T')


class InterpreterLambda:
    """
    TODO
    """
    available_interpreter: List[InterpreterLexeme] =\
        [

        ]

    def __init__(self, lexemes: List[Lexeme]):
        """
        Initialize new lambda-interpreter based on a list of given lexemes.

        :param function: List of lexemes to interpret
        """
        self.lexemes = lexemes

    def interpret(self) -> T:
        """
        Interpret the internal lexemes and return return-value.

        :return: Return-Value of interpreted lexemes
        """
        return None

    def get_interpreter(self, lexeme: Lexeme) -> Union[InterpreterLexeme, None]:
        """
        Returns the responsible lexeme-interpreter for a given lexeme.
        Might return None if no interpreter was found.

        :param lexeme: Lexeme to get interpreter for

        :return: Lexeme-Interpreter for lexeme or None
        """
        for interpreter in self.available_interpreter:
            if interpreter.is_valid_lexeme(lexeme):
                return interpreter

        return None
