from typing import List, Union

from dis import Instruction

from smart_lambda.lexeme import Lexeme, UnaryOperation, UnaryOperations
from smart_lambda.parser.parser_lexeme import ParserLexeme


class ParserUnaryOperation(ParserLexeme):
    """
    TODO
    """
    # List of valid instructions for the unary-parameter-parser
    instructions = \
        {

        }

    @classmethod
    def parse(cls, lexemes: List[Lexeme], instruction: Instruction) -> Union[UnaryOperation, None]:
        """
        Parses the given instruction and returns a corresponding unary-operation.
        Might return None in special cases.

        :param lexemes: List of already parsed lexemes
        :param instruction: Instruction to parse

        :return: Unary-Operation
        """
        super().parse(lexemes, instruction)

        return UnaryOperation(cls.instructions[instruction.opname], lexemes[-1])
