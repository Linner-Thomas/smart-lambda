from typing import Callable, TypeVar

import dis

from smart_lambda.lexeme import Constant

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
        self.parameter = []
        self.constants = []

        self.__parse_parameter()
        self.__parse_constants()

    def __parse_parameter(self) -> None:
        """
        Parse all parameter from underlying lambda-function and store internally.
        """
        pass

    def __parse_constants(self) -> None:
        """
        Parse all constants from underlying lambda-function and store internally.
        """
        # Iterate over all instructions in lambda-function
        for instruction in dis.get_instructions(self.function):
            # Primitive-Constant (int, str, ...) and tuple
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

            # Set-Constant (`argval` stores entry-count)
            if instruction.opname == 'BUILD_SET' and instruction.argval > 0:
                set_constants = self.constants[-instruction.argval:]        # Get last `argval` constants
                self.constants = self.constants[0:-instruction.argval]      # Remove last `argval` constants
                self.constants.append(set(set_constants))                   # Append entries as set

            # Set-Constant (>= 3.9, entries loaded as frozenset for long lists)
            if instruction.opname == 'SET_UPDATE':
                set_constants = self.constants[-1:]             # Get entries as frozenset
                self.constants = self.constants[0:-1]           # Remove entries
                self.constants.append(set(*set_constants))      # Append entries as set

            # Dict-Constant
            # Values get loaded separate using 'LOAD_CONST'
            # Keys get loaded as tuple using 'LOAD_CONST'
            if instruction.opname == 'BUILD_CONST_KEY_MAP':
                dict_keys = self.constants[-1:]                                                 # Get keys
                dict_vals = self.constants[-instruction.argval-1:-1]                            # Get vals
                self.constants = self.constants[0:-instruction.argval-1]                        # Remove keys and vals
                self.constants.append({key: val for key, val in zip(*dict_keys, dict_vals)})    # Append dict

        # Convert constants into constant-lexeme
        self.constants = [Constant(constant) for constant in self.constants]

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
