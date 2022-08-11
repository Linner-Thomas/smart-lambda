from typing import List, Union

from dis import Instruction

from smart_lambda.lexeme import Lexeme, Parameter
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
    def parse(cls, lexemes: List[Lexeme], instruction: Instruction) -> Union[Parameter, None]:
        """
        Parses the given instruction and returns a corresponding parameter.
        Might return None in special cases.

        :param lexemes: List of already parsed lexemes
        :param instruction: Instruction to parse

        :return: Parameter
        """
        return Parameter(instruction.argval)
