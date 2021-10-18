from typing import Protocol

from src.ufu_parser.scanner_consumer import ScannerConsumer


class SyntacticGraph(Protocol):

    def parse(self, consumer: ScannerConsumer) -> bool:
        ...
