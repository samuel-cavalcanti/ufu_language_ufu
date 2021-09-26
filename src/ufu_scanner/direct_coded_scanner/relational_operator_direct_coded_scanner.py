from typing import Optional

from src.ufu_token import UfuToken, UfuTokenType
from src.ufu_scanner.token_scan import TokenScan
from src.source_program import SourceProgram

from enum import Enum, auto
from typing import Tuple


class State(Enum):
    initial = auto()
    bigger = auto()
    smaller = auto()
    igual = auto()
    pass


class RelacionalOperators(Enum):
    BIGGER = '>'
    SMALLER = '<'
    IGUAL = '=='
    IGUAL_OR_BIGGER = '>='
    IGUAL_OR_SMALLER = '<='
    DIFFERENT = '<>'


class RelacionalOperatorDirectCodedScanner(TokenScan):
    __initial_pos: Tuple[int, int]
    __state: State
    __source: SourceProgram

    def scan(self, source: SourceProgram) -> Optional[UfuToken]:
        state = State.initial
        self.__initial_pos = source.current_pos()

        self.__source = source
        for _ in range(10):
            char = source.current_char()

            if state == State.initial:
                if char == RelacionalOperators.BIGGER.value:
                    state = State.bigger
                elif char == RelacionalOperators.SMALLER.value:
                    state = State.smaller
                elif char == '=':
                    state = State.igual
                else:
                    return None
            elif state == State.bigger:
                return self.__bigger_state(char)
            elif state == State.smaller:
                return self.__smaller_state(char)
            elif state == State.igual:
                return self.__igual_state(char)

            source.next_char()

    def __bigger_state(self, char: str):
        if char == '=':
            return UfuToken(token_type=UfuTokenType.RELATIONAL_OPERATOR,
                            pos=self.__initial_pos,
                            content=RelacionalOperators.IGUAL_OR_BIGGER.value)
        else:
            self.__source.back(self.__initial_pos)
            return UfuToken(token_type=UfuTokenType.RELATIONAL_OPERATOR,
                            pos=self.__initial_pos,
                            content=RelacionalOperators.BIGGER.value)

    def __smaller_state(self, char: str):
        if char == '=':
            return UfuToken(token_type=UfuTokenType.RELATIONAL_OPERATOR,
                            pos=self.__initial_pos,
                            content=RelacionalOperators.IGUAL_OR_SMALLER.value)
        elif char == '>':
            return UfuToken(token_type=UfuTokenType.RELATIONAL_OPERATOR,
                            pos=self.__initial_pos,
                            content=RelacionalOperators.DIFFERENT.value)
        else:
            self.__source.back(self.__initial_pos)
            return UfuToken(token_type=UfuTokenType.RELATIONAL_OPERATOR,
                            pos=self.__initial_pos,
                            content=RelacionalOperators.SMALLER.value)

    def __igual_state(self, char: str):
        if char == '=':
            return UfuToken(token_type=UfuTokenType.RELATIONAL_OPERATOR,
                            pos=self.__initial_pos,
                            content=RelacionalOperators.IGUAL.value)
        else:
            self.__source.back(self.__initial_pos)
            return None
