from typing import TypeVar

from smart_lambda.lexeme import BinaryOperation
from smart_lambda.interpreter.interpreter_lexeme import InterpreterLexeme

# Define type-variable for lexeme return-type
T = TypeVar('T')


class InterpreterBinaryOperation(InterpreterLexeme):
    """
    TODO
    """
    # List of valid lexemes for the lexeme-interpreter
    lexemes = \
        [
            BinaryOperation
        ]

    @classmethod
    def interpret(cls, interpreter_base, lexeme: BinaryOperation, **kwargs) -> T:
        """
        Interprets the given binary-operation and returns its result.

        :param interpreter_base Reference to base-interpreter (InterpreterLambda)
        :param lexeme: Binary-Operation to interpret
        :param kwargs: Dictionary containing arguments for lambda-function

        :return: Result of binary-operation
        """
        super().interpret(interpreter_base, lexeme, **kwargs)

        # Interpret operands (e. g. parameter, operation, ...)
        operand_1 = interpreter_base.get_interpreter(lexeme.operands[0])\
            .interpret(interpreter_base, lexeme.operands[0], **kwargs)
        operand_2 = interpreter_base.get_interpreter(lexeme.operands[1])\
            .interpret(interpreter_base, lexeme.operands[1], **kwargs)

        return lexeme.apply(operand_1, operand_2)
