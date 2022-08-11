from typing import List, Union

from dis import Instruction

from smart_lambda.lexeme import Lexeme


class ParserLexeme:
    """
    TODO
    """
    # List of valid instructions for the lexeme-parser
    instructions = []

    @classmethod
    def parse(cls, lexemes: List[Lexeme], instruction: Instruction) -> Union[Lexeme, None]:
        """
        Parses the given instruction and returns a corresponding lexeme.
        Might return None in special cases.

        This method has to be overridden by each lexeme-parser.

        :param lexemes: List of already parsed lexemes
        :param instruction: Instruction to parse

        :return: Lexeme
        """
        pass

    @classmethod
    def is_valid_instruction(cls, instruction: Instruction) -> bool:
        """
        Check whether the given instruction is valid for the lexeme-parser.

        :param instruction: Instruction to check

        :return: True / False
        """
        return instruction.opname in cls.instructions
