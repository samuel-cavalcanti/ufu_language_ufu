from enum import auto, Enum
from typing import Optional

from src.source_program import SourceProgram
from src.ufu_token import UfuToken


class State(Enum):
    space = auto()
    commentary = auto()


class CommentariesAndSpaces:
    __state: State

    def scan(self, source: SourceProgram) -> Optional[UfuToken]:
        self.__state = State.space

        while True:
            char = source.current_char()

            if self.__state == State.space:

                if char == '[':
                    self.__state = State.commentary
                elif not char.isspace():
                    return None

            elif self.__state == State.commentary:
                if char == ']':
                    self.__state = State.space

            source.next_char()
