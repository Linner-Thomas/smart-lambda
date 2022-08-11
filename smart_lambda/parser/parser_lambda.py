from typing import Callable, List, TypeVar

from smart_lambda.lexeme import Lexeme

# Define type-variable for lambda return-type
T = TypeVar('T')


class ParserLambda:
    """
    TODO
    """
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
        return []
