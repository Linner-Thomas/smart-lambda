from dis import Instruction

from smart_lambda.lexeme import Lexeme


class ParserLexeme:
    """
    TODO
    """
    # List of valid instructions for the lexeme-parser
    instructions = []

    @classmethod
    def parse(cls, instruction: Instruction) -> Lexeme:
        """
        Parses the given instruction and returns a corresponding lexeme.
        This method has to be overridden by each lexeme-parser.

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
