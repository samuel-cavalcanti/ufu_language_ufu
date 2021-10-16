from typing import Protocol, Tuple


class SourceProgramException(Exception):
    pass


class SourceProgram(Protocol):

    def current_char(self) -> str:
        """get current char of source Object"""

    def next_char(self) -> None:
        """go to next char maybe raise SourceProgramException if is end of file"""

    def current_pos(self) -> Tuple[int, int]:
        """get current row,column of file,maybe raise SourceProgramException if is end of file"""

    def back(self, pos: Tuple[int, int]) -> None:
        """return source Object to desired pos"""
