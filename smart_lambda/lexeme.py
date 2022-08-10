from typing import TypeVar

T = TypeVar('T')


class Constant:
    """
    Wrapper-Class for constant-lexeme
    """
    def __init__(self, value: T):
        """
        Initialize constant based on it's value

        :param value: Value of constant
        """
        self.value: T = value
        self.type: type = type(value)
