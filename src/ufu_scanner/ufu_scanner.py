from src.source_program import SourceProgram
from src.ufu_scanner.token_scan import TokenScan
from src.ufu_token import UfuToken


from typing import List


class ScannerException(Exception):
    pass


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

        token = None
        for scanner in self.__token_scanners:
            token = scanner.scan(self.__source)
            if token is not None:
                break

        if token is None:
            row, col = self.__source.current_pos()
            raise ScannerException(
                f'unrecognized token, in row: {row}, column:{col} ')

        return token
