from typing import List, Union

from dis import Instruction

from smart_lambda.lexeme import Lexeme, Constant
from smart_lambda.parser.parser_lexeme import ParserLexeme


class ParserConstant(ParserLexeme):
    """
    TODO
    """
    # List of valid instructions for the parameter-parser
    instructions =\
        [
            'LOAD_CONST',
            'BUILD_LIST',
            'LIST_EXTEND',
            'BUILD_SET',
            'BUILD_CONST_KEY_MAP'
        ]

    @classmethod
    def parse(cls, lexemes: List[Lexeme], instruction: Instruction) -> Union[Constant, None]:
        """
        Parses the given instruction and returns a corresponding parameter.
        Might return None in special cases.

        :param lexemes: List of already parsed lexemes
        :param instruction: Instruction to parse

        :return: Constant
        """
        # Primitive-Constant (int, str, ...) and tuple
        if instruction.opname == 'LOAD_CONST':
            if isinstance(instruction.argval, frozenset):
                return Constant(set(instruction.argval))

            return Constant(instruction.argval)

        # List-Constant (`argval` stores entry-count)
        if instruction.opname == 'BUILD_LIST' and instruction.argval > 0:
            # Get last `argval` lexemes, these are constants by definition
            list_constants = [constant.value for constant in lexemes[-instruction.argval:]]
            del lexemes[-instruction.argval:]
            return Constant(list_constants)

        # List-Constant (>= 3.9, entries loaded as single tuple for long lists)
        if instruction.opname == 'LIST_EXTEND':
            list_constants = lexemes[-1].value
            del lexemes[-1]
            return Constant(list(list_constants))

        # Set-Constant (`argval` stores entry-count)
        if instruction.opname == 'BUILD_SET' and instruction.argval > 0:
            # Get last `argval` lexemes, these are constants by definition
            set_constants = [constant.value for constant in lexemes[-instruction.argval:]]
            del lexemes[-instruction.argval:]
            return Constant(set(set_constants))

        # Dict-Constant
        # Values get loaded separate using 'LOAD_CONST'
        # Keys get loaded as tuple using 'LOAD_CONST'
        if instruction.opname == 'BUILD_CONST_KEY_MAP':
            dict_keys = lexemes[-1].value
            dict_vals = [constant.value for constant in lexemes[-instruction.argval - 1:-1]]
            del lexemes[-instruction.argval - 1:]
            return Constant({key: val for key, val in zip(dict_keys, dict_vals)})

        return None
