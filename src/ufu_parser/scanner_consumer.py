from src.ufu_token import UfuToken, UfuTokenType
from src.ufu_scanner import Scanner
from src.ufu_parser.parser import UfuParserException



class ScannerConsumer:
    __scanner: Scanner
    __current_token: UfuToken

    def __init__(self, scanner: Scanner):
        self.__scanner = scanner
        self.__current_token = scanner.get_token()
        print(f"current token {self.__current_token}")


    def eat(self, expected_type: UfuTokenType) -> bool:
        if expected_type == self.__current_token.type:
            self.__current_token = self.__scanner.get_token()
            print(f"current token {self.__current_token}")

            return True

        return False

    def eat_or_exception(self, expected_type: UfuTokenType):
        if self.eat(expected_type):
            return

        row = self.__current_token.file_pos[0] + 1
        col = self.__current_token.file_pos[1] + 1

        message = f'Expected {expected_type.name} ' \
                  f'Token on row {row} and column {col},' \
                  f'find {self.__current_token.content} '

        raise UfuParserException(message)

    def __str__(self) -> str:
        row = self.__current_token.file_pos[0] + 1
        col = self.__current_token.file_pos[1] + 1
        message = f'Token on row {row} and column {col},' \
                  f'find {self.__current_token.content} '

        return message
