from typing import Protocol

from .ufu_parser import UfuParser


class UfuParserPlugin(Protocol):

    def build(self, parser: UfuParser) -> None:
        ...
