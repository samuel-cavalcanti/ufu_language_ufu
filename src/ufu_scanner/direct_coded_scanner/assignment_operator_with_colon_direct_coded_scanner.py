from typing import Optional

from src.ufu_token import UfuToken, UfuTokenType
from src.source_program import SourceProgram
from enum import Enum, auto


class State(Enum):
    initial_state = auto()
    colon = auto()


class AssignmentOperatorWithColonInDirectCodedScanner:

    def scan(self, source: SourceProgram) -> Optional[UfuToken]:
        state = State.initial_state
        initial_pos = source.current_pos()
        back_pos = source.current_pos()
        for _ in range(5):
            char = source.current_char()
            if state == State.initial_state:
                if char == ':':
                    state = State.colon
                else:
                    return None
            elif state == State.colon:
                if char == '=':
                    return UfuToken(token_type=UfuTokenType.ASSIGNMENT_OPERATOR, pos=initial_pos)
                else:
                    source.back(back_pos)
                    return UfuToken(token_type=UfuTokenType.COLON, pos=initial_pos)
            back_pos = source.current_pos()
            source.next_char()
