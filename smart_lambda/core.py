from typing import Callable, TypeVar

import dis

# Define type-variable for lambda return-type
T = TypeVar('T')


class SmartLambda:
    """
    TODO
    """
    def __init__(self, function: Callable[..., T]):
        """
        Initialize a smart-lambda based on a lambda-function.

        Usage:
        s_lambda = SmartLambda(lambda x: return x ** 2)

        :param function: Lambda-Function
        """
        self.function = function
        self.constants = []

        self.__parse_constants()

    def __parse_constants(self) -> None:
        """
        Parse all constants from underlying lambda-function and store internally.
        """
        [print(instruction) for instruction in dis.get_instructions(self.function)]

        # Iterate over all instructions in lambda-function
        for instruction in dis.get_instructions(self.function):
            # Primitive-Constant (int, str, ...)
            if instruction.opname == 'LOAD_CONST':
                self.constants.append(instruction.argval)       # Append constant

            # List-Constant (`argval` stores entry-count)
            if instruction.opname == 'BUILD_LIST' and instruction.argval > 0:
                list_constants = self.constants[-instruction.argval:]       # Get last `argval` constants
                self.constants = self.constants[0:-instruction.argval]      # Remove last `argval` constants
                self.constants.append(list_constants)                       # Append entries as list

            # List-Constant (>= 3.9, entries loaded as single tuple for long lists)
            if instruction.opname == 'LIST_EXTEND':
                list_constants = self.constants[-1:]            # Get entries [(entries)]
                self.constants = self.constants[0:-1]           # Remove entries
                self.constants.append(list(*list_constants))    # Append entries as list

    def __call__(self, *args, **kwargs) -> T:
        """
        Override call-method to allow the execution of the underlying lambda-function.

        Usage:
        val = s_lambda()

        :param args:   Positional parameter to lambda-function
        :param kwargs: Keyword parameter to lambda-function

        :return: Return-Value of underlying lambda-function
        """
        return self.function(*args, **kwargs)
