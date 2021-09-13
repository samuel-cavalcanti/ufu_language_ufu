from typing import Optional

from src.ufu_scanner.token_scan import TokenScan
from src.ufu_token import UfuToken,UfuTokenType
from src.source_program import SourceProgram

class OneCharScannerException(Exception):
    pass


class OneCharAdHocScanner(TokenScan):
    """
        OneCharScanner é um scan que utiliza a ideia Ad hoc,
        mas sem verificar o próximo char para confirmar o token.
        Eles só pode ser utilizado para reconhecer tokens de um único caractere
    """
    __char: str
    __token_type: UfuTokenType

    def __init__(self, char: str, token_type: UfuTokenType):
        if len(char) != 1:
            raise OneCharScannerException("this Scanner works only with one char")
        self.__char = char
        self.__token_type = token_type

    def scan(self, source: SourceProgram) -> Optional[UfuToken]:
        char = source.current_char()

        if char == self.__char:
            return UfuToken(token_type=self.__token_type, pos=source.current_pos())

        return None
