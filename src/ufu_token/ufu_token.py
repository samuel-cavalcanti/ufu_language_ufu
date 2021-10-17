from dataclasses import dataclass
from enum import Enum, auto
from typing import Optional, Tuple


class UfuTokenException(Exception):
    pass


class UfuTokenType(Enum):
    OPEN_PARENTHESES = auto()
    CLOSE_PARENTHESES = auto()
    ADD = auto()
    SUB = auto()
    DIV = auto()
    MUL = auto()
    OPEN_BRACKETS = auto()
    CLOSE_BRACKETS = auto()
    SEMICOLON = auto()
    COMMA = auto()
    COLON = auto()
    ASSIGNMENT_OPERATOR = auto()
    RELATIONAL_OPERATOR = auto()
    IF = auto()
    THEN = auto()
    ELSE = auto()
    WHILE = auto()
    DO = auto()
    UNTIL = auto()
    SOFTWARE = auto()
    TYPE_VARIABLE = auto()
    VARIABLE_ID = auto()
    CONST_INT = auto()
    CONST_REAL = auto()
    CONST_ASCII = auto()


@dataclass()
class UfuToken:
    type: UfuTokenType
    content: Optional[str]
    file_pos: Tuple[int, int]
    __slots__ = ['type', 'content', 'file_pos']

    def __init__(self, token_type: UfuTokenType, pos: Tuple[int, int], content: str = None):
        self.type = token_type
        self.content = content
        self.file_pos = pos
