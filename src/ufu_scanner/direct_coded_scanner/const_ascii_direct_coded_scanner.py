from typing import Optional, Tuple
from enum import Enum, auto

from src.source_program import SourceProgram
from src.ufu_token import UfuToken, UfuTokenType
from src.ufu_scanner.ufu_scanner import ScannerException


class State(Enum):
    initial_state = auto()
    making_ascii = auto()


class ConstAsciiDirectCodedScanner:
    __lexema: str
    __initial_pos: Tuple[int, int]

    def scan(self, source: SourceProgram) -> Optional[UfuToken]:
        self.__initial_pos = source.current_pos()
        self.__lexema = ''
        state = State.initial_state
        while True:
            char = source.current_char()
            # print(f"char:{char} state: {state}")
            if state == State.initial_state:
                if char == '\'':
                    state = State.making_ascii
                else:
                    return None
            elif state == State.making_ascii:
                if char == '\'':
                    return UfuToken(token_type=UfuTokenType.CONST_ASCII, pos=self.__initial_pos, content=self.__lexema)
                elif char.isascii():
                    self.__lexema += char
                else:
                    raise ScannerException(f'Unrecognized symbol at {source.current_pos()}')

            source.next_char()
