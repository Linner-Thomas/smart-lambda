from dis import Instruction, get_instructions
from typing import Callable, List, TypeVar, Union

from smart_lambda.lexeme import Lexeme
from smart_lambda.parser.parser_lexeme import ParserLexeme
from smart_lambda.parser.parser_parameter import ParserParameter

# Define type-variable for lambda return-type
T = TypeVar('T')


class ParserLambda:
    """
    TODO
    """
    available_parser: List[ParserLexeme] =\
        [
            ParserParameter
        ]

    def __init__(self, function: Callable[..., T]):
        """
        Initialize new lambda-parser based on given lambda-function.

        :param function: Lambda-Function to parse
        """
        self.function = function

    def parse(self) -> List[Lexeme]:
        """
        Parse the internal lambda-function and return list of lexemes.

        :return: List of lexemes
        """
        lexemes = []

        for instruction in get_instructions(self.function):
            parser = self.get_parser(instruction)

            if parser is not None:
                lexemes.append(parser.parse(instruction))

        return lexemes

    def get_parser(self, instruction: Instruction) -> Union[ParserLexeme, None]:
        """
        Returns the responsible lexeme-parser for a given instruction.
        Might return None if no parser was found.

        :param instruction: Instruction to get parser for

        :return: Lexeme-Parser for instruction or None
        """
        for parser in self.available_parser:
            if parser.is_valid_instruction(instruction):
                return parser

        return None
