from src.source_program import SourceProgram
from src.ufu_scanner.token_scan import TokenScan
from src.ufu_scanner.scanner import ScannerException
from src.ufu_token import UfuToken
from src.ufu_scanner.direct_coded_scanner import CommentariesAndSpaces
from typing import List


class UfuScanner:
    __token_scanners: List[TokenScan]
    __source: SourceProgram
    __first_iteration: bool

    def __init__(self, token_scanners: List[TokenScan], source: SourceProgram):
        self.__token_scanners = token_scanners
        self.__source = source
        self.__first_iteration = True

    def get_token(self) -> UfuToken:

        if self.__first_iteration is False:
            self.__source.next_char()
        else:
            self.__first_iteration = False

        self.__token_scanners: List[TokenScan] = [CommentariesAndSpaces()] + self.__token_scanners

        for scanner in self.__token_scanners:
            token = scanner.scan(self.__source)
            if token is not None:
                return token

        row, col = self.__source.current_pos()
        raise ScannerException(
            f'unrecognized token, in row: {row + 1}, column: {col + 1} char: {self.__source.current_char().encode()} ')
