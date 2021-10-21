from src.source_program import SourceProgram, SourceProgramException
from src.ufu_scanner.token_scan import TokenScan
from src.ufu_scanner.scanner import ScannerException
from src.ufu_token import UfuToken, UfuTokenType
from src.ufu_scanner.direct_coded_scanner import CommentariesAndSpaces
from typing import List, Optional


class UfuScanner:
    __token_scanners: List[TokenScan]
    __source: SourceProgram
    __first_iteration: bool

    def __init__(self, token_scanners: List[TokenScan], source: SourceProgram):
        self.__token_scanners = [CommentariesAndSpaces()] + token_scanners
        self.__source = source
        self.__first_iteration = True

    def get_token(self) -> UfuToken:

        if self.__first_iteration:
            self.__first_iteration = False
        else:
            self.__source.next_char()

        try:
            token = self.__run()
        except SourceProgramException:
            token = UfuToken(UfuTokenType.END_FILE, pos=(-1, -1))

        return token

    def __run(self) -> UfuToken:
        for scanner in self.__token_scanners:
            token = scanner.scan(self.__source)
            if token:
                return token

        row, col = self.__source.current_pos()
        raise ScannerException(
            f'unrecognized token, in row: {row + 1}, column: {col + 1} char: {self.__source.current_char().encode()} ')
