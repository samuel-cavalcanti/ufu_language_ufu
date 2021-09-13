from typing import Protocol, Tuple
from abc import abstractmethod


class SourceProgramException(Exception):
    pass


class SourceProgram(Protocol):

    @abstractmethod
    def current_char(self) -> str:
        """get current char of source Object"""
        raise NotImplementedError

    @abstractmethod
    def next_char(self) -> None:
        """go to next char maybe raise SourceProgramException if is end of file"""
        raise NotImplementedError

    @abstractmethod
    def current_pos(self) -> Tuple[int, int]:
        """get current row,column of file,maybe raise SourceProgramException if is end of file"""
        raise NotImplementedError

    @abstractmethod
    def back(self, pos: Tuple[int, int]):
        """return source Object to desired pos"""
        raise NotImplementedError
