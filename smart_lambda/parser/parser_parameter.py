from dis import Instruction

from smart_lambda.lexeme import Parameter
from smart_lambda.parser.parser_lexeme import ParserLexeme


class ParserParameter(ParserLexeme):
    """
    TODO
    """
    # List of valid instructions for the parameter-parser
    instructions =\
        [
            'LOAD_FAST'
        ]

    @classmethod
    def parse(cls, instruction: Instruction) -> Parameter:
        """
        Parses the given instruction and returns a corresponding parameter.

        :param instruction: Instruction to parse

        :return: Parameter
        """
        return Parameter(instruction.argval)
