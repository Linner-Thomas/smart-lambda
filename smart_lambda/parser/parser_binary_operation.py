from typing import List, Union

from dis import Instruction

from smart_lambda.lexeme import Lexeme, BinaryOperation, BinaryOperations
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
            'BINARY_MODULO': BinaryOperations.MOD
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

        return BinaryOperation(cls.instructions[instruction.opname], lexemes[-2:])
