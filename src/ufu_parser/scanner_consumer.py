from typing import Optional

from src.ufu_token import UfuToken, UfuTokenType
from src.ufu_scanner import Scanner
from src.ufu_parser.parser import UfuParserException
from .syntax_tree import SyntaxNode
from src.ufu_parser.parser_observer import Subject


class ScannerConsumer:
    __scanner: Scanner
    __current_token: UfuToken
    parent: SyntaxNode
    parser_subject: Subject

    def __init__(self, scanner: Scanner, subject: Subject):
        self.__scanner = scanner
        self.__current_token = scanner.get_token()
        self.parser_subject = subject

    def eat(self, expected_type: UfuTokenType) -> Optional[UfuToken]:
        if expected_type == self.__current_token.type:
            token = self.__current_token
            self.__current_token = self.__scanner.get_token()

            return token

        return None

    def eat_or_exception(self, expected_type: UfuTokenType) -> UfuToken:
        token = self.eat(expected_type)
        if token:
            return token

        row = self.__current_token.file_pos[0] + 1
        col = self.__current_token.file_pos[1] + 1

        message = f'Expected {expected_type.name} ' \
                  f'Token on row {row} and column {col},' \
                  f'find {self.__current_token} '

        raise UfuParserException(message)

    def __str__(self) -> str:
        row = self.__current_token.file_pos[0] + 1
        col = self.__current_token.file_pos[1] + 1
        message = f'Token on row {row} and column {col},' \
                  f'find {self.__current_token.content} '

        return message
