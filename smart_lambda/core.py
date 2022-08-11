from typing import Callable, TypeVar

import dis

from smart_lambda.parser.parser_lambda import ParserLambda
from smart_lambda.lexeme import BinaryOperation, BinaryOperations, Constant, Parameter

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
        self.parser = ParserLambda(function)

        self.lexemes = []
        self.parameter = []
        self.constants = []
        self.binary_operations = []

        self.__parse()

        self.__parse_constants()
        self.__parse_binary_operations()

    def __parse(self) -> None:
        """
        TODO
        """
        # Parse lambda-function and return lexemes
        self.lexemes = self.parser.parse()

        # Split lexemes into "type" for better accessibility
        for lexeme in self.lexemes:
            if isinstance(lexeme, Parameter):
                self.parameter.append(lexeme)

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

    def __parse_binary_operations(self) -> None:
        """
        Parse all binary-operations from underlying lambda-function and store internally.
        """
        [print(instruction) for instruction in dis.get_instructions(self.function)]
        # TODO: Currently only works for parameter!
        # This will probably require a rework of the whole parser system, because we need the last two operands,
        # which can be a mixture of constants and parameter ...

        # Iterate over all instructions in lambda-function
        for instruction in dis.get_instructions(self.function):
            # Addition
            if instruction.opname == 'BINARY_ADD':
                operands = self.parameter[-2:]
                self.binary_operations.append(BinaryOperation(BinaryOperations.ADD, operands))

            # Subtraction
            if instruction.opname == 'BINARY_SUBTRACT':
                operands = self.parameter[-2:]
                self.binary_operations.append(BinaryOperation(BinaryOperations.SUB, operands))

            # Multiplication
            if instruction.opname == 'BINARY_MULTIPLY':
                operands = self.parameter[-2:]
                self.binary_operations.append(BinaryOperation(BinaryOperations.MUL, operands))

            # True-Division
            if instruction.opname == 'BINARY_TRUE_DIVIDE':
                operands = self.parameter[-2:]
                self.binary_operations.append(BinaryOperation(BinaryOperations.DIV_TRUE, operands))

            # Floor-Division
            if instruction.opname == 'BINARY_FLOOR_DIVIDE':
                operands = self.parameter[-2:]
                self.binary_operations.append(BinaryOperation(BinaryOperations.DIV_FLOOR, operands))

            # Modulo
            if instruction.opname == 'BINARY_MODULO':
                operands = self.parameter[-2:]
                self.binary_operations.append(BinaryOperation(BinaryOperations.MOD, operands))

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
