from .token_scan import TokenScan
from ..ufu_token import UfuTokenType
from .one_char_ad_hoc_scanner import OneCharAdHocScanner


class SingleCharTokenScanCreator:
    __creators: dict

    def __init__(self):
        self.__creators = {
            UfuTokenType.SEMICOLON: self.__create_semi_colon_scan,
            UfuTokenType.COMMA: self.__create_comma_scan,
            UfuTokenType.OPEN_BRACKETS: self.__create_open_brackets_scan,
            UfuTokenType.CLOSE_BRACKETS: self.__create_close_brackets_scan,
            UfuTokenType.OPEN_PARENTHESES: self.__create_open_parentheses_scan,
            UfuTokenType.CLOSE_PARENTHESES: self.__create_close_parentheses_scan,
            UfuTokenType.ADD: self.__create_add_arithmetic_operation_scan,
            UfuTokenType.SUB: self.__create_subtract_arithmetic_operation_scan,
            UfuTokenType.MUL: self.__create_multiplication_arithmetic_operation_scan,
            UfuTokenType.DIV: self.__create_divide_arithmetic_operation_scan
        }

    def create_token_scan(self, token_type: UfuTokenType) -> TokenScan:
        creator = self.__creators.get(token_type, None)
        if creator is None:
            raise NotImplementedError(f"token type: {token_type}")
        return creator()

    @staticmethod
    def __create_semi_colon_scan():
        return OneCharAdHocScanner(char=';', token_type=UfuTokenType.SEMICOLON)

    @staticmethod
    def __create_comma_scan():
        return OneCharAdHocScanner(char=',', token_type=UfuTokenType.COMMA)

    @staticmethod
    def __create_open_brackets_scan():
        return OneCharAdHocScanner(char='{', token_type=UfuTokenType.OPEN_BRACKETS)

    @staticmethod
    def __create_close_brackets_scan():
        return OneCharAdHocScanner(char='}', token_type=UfuTokenType.CLOSE_BRACKETS)

    @staticmethod
    def __create_open_parentheses_scan():
        return OneCharAdHocScanner(char='(', token_type=UfuTokenType.OPEN_PARENTHESES)

    @staticmethod
    def __create_close_parentheses_scan():
        return OneCharAdHocScanner(char=')', token_type=UfuTokenType.CLOSE_PARENTHESES)

    @staticmethod
    def __create_add_arithmetic_operation_scan():
        return OneCharAdHocScanner(char='+', token_type=UfuTokenType.ADD)

    @staticmethod
    def __create_subtract_arithmetic_operation_scan():
        return OneCharAdHocScanner(char='-', token_type=UfuTokenType.SUB)

    @staticmethod
    def __create_multiplication_arithmetic_operation_scan():
        return OneCharAdHocScanner(char='*', token_type=UfuTokenType.MUL)

    @staticmethod
    def __create_divide_arithmetic_operation_scan():
        return OneCharAdHocScanner(char='/', token_type=UfuTokenType.DIV)
