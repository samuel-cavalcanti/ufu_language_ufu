from typing import Optional, Tuple
from enum import Enum, auto

from src.source_program import SourceProgram
from src.ufu_token import UfuToken, UfuTokenType
from src.ufu_scanner.ufu_scanner import TokenScan, ScannerException


class State(Enum):
    initial_state = auto()
    making_int = auto()
    making_real = auto()
    making_real_with_scientific_notation = auto()
    making_exponent_value = auto()


class ConstNumberDirectCodedScanner(TokenScan):
    __initial_pos = Tuple[int, int]
    _lexema: str

    def scan(self, source: SourceProgram) -> Optional[UfuToken]:
        self.__initial_pos = source.current_pos()
        old_pos = self.__initial_pos
        state = State.initial_state
        self._lexema = ''
        while True:
            char = source.current_char()
            if state == State.initial_state:
                if char.isdigit() or char == '-' or char == '+':
                    state = State.making_int
                    self._lexema += char
                else:
                    return None
            elif state == State.making_int:
                if char.isdigit():
                    self._lexema += char
                elif char == '.':
                    state = State.making_real
                    self._lexema += char
                elif char == 'e' or char == 'E':
                    self._lexema += char
                    state = State.making_real_with_scientific_notation
                else:
                    source.back(old_pos)
                    return UfuToken(token_type=UfuTokenType.CONST_INT, pos=self.__initial_pos, content=self._lexema)

            elif state == State.making_real:
                if char.isdigit():
                    self._lexema += char
                elif char == 'e' or char == 'E':
                    self._lexema += char
                    state = State.making_real_with_scientific_notation
                else:
                    source.back(old_pos)
                    return UfuToken(token_type=UfuTokenType.CONST_REAL, pos=self.__initial_pos, content=self._lexema)

            elif state == State.making_real_with_scientific_notation:
                if char == '+' or char == '-':
                    self._lexema += char
                    state = State.making_exponent_value
                elif char.isdigit():
                    self._lexema += char
                    state = State.making_exponent_value
                else:
                    raise ScannerException(f'unrecognize symbol at {source.current_pos()}')

            elif state == State.making_exponent_value:
                if char.isdigit():
                    self._lexema += char
                elif self._lexema[-1].isdigit():
                    source.back(old_pos)
                    return UfuToken(token_type=UfuTokenType.CONST_REAL, pos=self.__initial_pos, content=self._lexema)
                else:
                    raise ScannerException(f'unrecognize symbol at {source.current_pos()}')

            old_pos = source.current_pos()
            source.next_char()
