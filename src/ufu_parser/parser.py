from typing import Protocol

from src.ufu_scanner import Scanner
from src.ufu_parser.syntax_tree import SyntaxTree


class Parser(Protocol):

    def run(self, scanner: Scanner) -> SyntaxTree:
        "Run parser"


class UfuParserException(Exception):
    pass
