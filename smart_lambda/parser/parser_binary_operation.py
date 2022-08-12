from typing import List, Union

from dis import Instruction

from smart_lambda.lexeme import Lexeme, BinaryOperation, BinaryOperations, UnaryOperation
from smart_lambda.parser.parser_lexeme import ParserLexeme


class ParserBinaryOperation(ParserLexeme):
    """
    TODO
    """
    # List of valid instructions for the parameter-parser
    instructions = \
        {
            'BINARY_ADD': BinaryOperations.ADD,
            'BINARY_SUBTRACT': BinaryOperations.SUB,
            'BINARY_MULTIPLY': BinaryOperations.MUL,
            'BINARY_TRUE_DIVIDE': BinaryOperations.DIV_TRUE,
            'BINARY_FLOOR_DIVIDE': BinaryOperations.DIV_FLOOR,
            'BINARY_MODULO': BinaryOperations.MOD,
            'BINARY_AND': BinaryOperations.AND,
            'BINARY_OR': BinaryOperations.OR,
            'BINARY_XOR': BinaryOperations.XOR,
            'BINARY_LSHIFT': BinaryOperations.SHIFT_L,
            'BINARY_RSHIFT': BinaryOperations.SHIFT_R
        }

    @classmethod
    def parse(cls, lexemes: List[Lexeme], instruction: Instruction) -> Union[BinaryOperation, None]:
        """
        Parses the given instruction and returns a corresponding binary-operation.
        Might return None in special cases.

        :param lexemes: List of already parsed lexemes
        :param instruction: Instruction to parse

        :return: Binary-Operation
        """
        super().parse(lexemes, instruction)

        return BinaryOperation(cls.instructions[instruction.opname], cls.get_operands(lexemes))

    @classmethod
    def get_operands(cls, lexemes: List[Lexeme]) -> List[Lexeme]:
        """
        Get the two operands for the binary-operation based on the already parsed lexemes

        :param lexemes: List of already parsed lexemes

        :return: List of operands
        """
        operands = []

        # Iterate lexemes in reversed order
        lexemes_iter = iter(lexemes[::-1])
        for lexeme in lexemes_iter:
            operands.append(lexeme)

            # If lexeme was binary operation, skip next two lexemes (operands of operation)
            if isinstance(lexeme, BinaryOperation):
                next(lexemes_iter)
                next(lexemes_iter)

            # If lexeme was unary operation, skip next lexeme (operand of operation)
            if isinstance(lexeme, UnaryOperation):
                next(lexemes_iter)

            # Break when 2 operands where found
            if len(operands) == 2:
                break

        # Fix order of operands and return
        return operands[::-1]
