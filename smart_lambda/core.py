from typing import Callable, TypeVar

from smart_lambda.parser.parser_lambda import ParserLambda
from smart_lambda.interpreter.interpreter_lambda import InterpreterLambda
from smart_lambda.lexeme import Parameter, Constant, BinaryOperation, UnaryOperation

# Define type-variable for lambda return-type
T = TypeVar('T')


class SmartLambda:
    """
    TODO
    """
    def __init__(self, function: Callable[..., T]):
        """
        Initialize a smart-lambda based on a lambda-function.

        Usage:
        s_lambda = SmartLambda(lambda x: return x ** 2)

        :param function: Lambda-Function
        """
        self.function = function
        self.parser = ParserLambda(function)

        self.lexemes = []
        self.parameter = []
        self.constants = []
        self.binary_operations = []
        self.unary_operations = []

        self.__parse()

    def __parse(self) -> None:
        """
        TODO
        """
        # Parse lambda-function and return lexemes
        self.lexemes = self.parser.parse()

        # Split lexemes into "type" for better accessibility
        for lexeme in self.lexemes:
            if isinstance(lexeme, Parameter):
                self.parameter.append(lexeme)

            if isinstance(lexeme, Constant):
                self.constants.append(lexeme)

            if isinstance(lexeme, BinaryOperation):
                self.binary_operations.append(lexeme)

            if isinstance(lexeme, UnaryOperation):
                self.unary_operations.append(lexeme)

    def __call__(self, *args, **kwargs) -> T:
        """
        Override call-method, this will interpret the internal lexemes and return its return-value.

        Usage:
        val = s_lambda()

        :param args:   Positional-Parameter
        :param kwargs: Keyword-Parameter

        :return: Return-Value of internal lexemes
        """
        # Currently all arguments have to be given as keyword-parameter
        return InterpreterLambda(self.lexemes).interpret(**kwargs)
