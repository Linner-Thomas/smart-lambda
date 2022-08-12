from typing import TypeVar

from smart_lambda.lexeme import UnaryOperation
from smart_lambda.interpreter.interpreter_lexeme import InterpreterLexeme

# Define type-variable for lexeme return-type
T = TypeVar('T')


class InterpreterUnaryOperation(InterpreterLexeme):
    """
    TODO
    """
    # List of valid lexemes for the lexeme-interpreter
    lexemes = \
        [
            UnaryOperation
        ]

    @classmethod
    def interpret(cls, interpreter_base, lexeme: UnaryOperation, **kwargs) -> T:
        """
        Interprets the given unary-operation and returns its result.

        :param interpreter_base Reference to base-interpreter (InterpreterLambda)
        :param lexeme: Unary-Operation to interpret
        :param kwargs: Dictionary containing arguments for lambda-function

        :return: Result of unary-operation
        """
        super().interpret(interpreter_base, lexeme, **kwargs)

        # Interpret operand (e. g. parameter, operation, ...)
        operand = interpreter_base.get_interpreter(lexeme.operand).interpret(interpreter_base, lexeme.operand, **kwargs)

        return lexeme.apply(operand)
