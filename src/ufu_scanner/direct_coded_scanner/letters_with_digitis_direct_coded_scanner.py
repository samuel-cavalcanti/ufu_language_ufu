from typing import Optional, Tuple

from src.ufu_token import UfuToken
from src.ufu_scanner.token_scan import TokenScan, UfuTokenType
from src.source_program import SourceProgram
from enum import Enum, auto


class State(Enum):
    initial_state = auto()
    creating_lexema = auto()
    final_state = auto()


class LettersWithDigitsDirectCodedScanner(TokenScan):
    __lexema: str
    __initial_pos: Tuple[int, int]

    def scan(self, source: SourceProgram) -> Optional[UfuToken]:
        self.__initial_pos = source.current_pos()
        self.__lexema = ''
        state = State.initial_state
        back_pos = self.__initial_pos

        while True:
            char = source.current_char()
            if state == State.initial_state:
                if char.isalpha():
                    self.__lexema += char
                    state = State.creating_lexema
                else:
                    return None

            elif state == State.creating_lexema:
                if char.isalpha() or char.isdigit():
                    self.__lexema += char
                else:
                    source.back(back_pos)
                    return self.__create_token()

            back_pos = source.current_pos()
            source.next_char()

    def __create_token(self):
        lower_lexema = self.__lexema.lower()
        if lower_lexema == 'programa':
            return UfuToken(token_type=UfuTokenType.SOFTWARE, pos=self.__initial_pos)
        elif lower_lexema == 'if':
            return UfuToken(token_type=UfuTokenType.IF, pos=self.__initial_pos)
        elif lower_lexema == 'then':
            return UfuToken(token_type=UfuTokenType.THEN, pos=self.__initial_pos)
        elif lower_lexema == 'else':
            return UfuToken(token_type=UfuTokenType.ELSE, pos=self.__initial_pos)
        elif lower_lexema == 'while':
            return UfuToken(token_type=UfuTokenType.WHILE, pos=self.__initial_pos)
        elif lower_lexema == 'do':
            return UfuToken(token_type=UfuTokenType.DO, pos=self.__initial_pos)
        elif lower_lexema == 'until':
            return UfuToken(token_type=UfuTokenType.UNTIL, pos=self.__initial_pos)
        elif lower_lexema == 'ascii':
            return UfuToken(token_type=UfuTokenType.TYPE_VARIABLE, pos=self.__initial_pos, content='ascii')
        elif lower_lexema == 'int':
            return UfuToken(token_type=UfuTokenType.TYPE_VARIABLE, pos=self.__initial_pos, content='int')
        elif lower_lexema == 'real':
            return UfuToken(token_type=UfuTokenType.TYPE_VARIABLE, pos=self.__initial_pos, content='real')
        else:
            return UfuToken(token_type=UfuTokenType.VARIABLE_ID, pos=self.__initial_pos, content=self.__lexema)
