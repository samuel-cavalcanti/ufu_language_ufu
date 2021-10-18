from typing import Protocol

from src.ufu_scanner import Scanner


class Parser(Protocol):

    def run(self, scanner: Scanner):
        "Run parser"


class UfuParserException(Exception):
    pass
