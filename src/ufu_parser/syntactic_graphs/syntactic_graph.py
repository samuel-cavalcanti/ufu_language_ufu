from typing import Protocol, Optional

from src.ufu_parser.scanner_consumer import ScannerConsumer
from src.ufu_parser.syntax_tree import SyntaxNode


class SyntacticGraph(Protocol):

    def parse(self, consumer: ScannerConsumer) -> Optional[SyntaxNode]:
        ...
