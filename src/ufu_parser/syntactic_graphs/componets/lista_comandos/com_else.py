from typing import Optional

from src.ufu_parser.syntactic_graphs.syntactic_graph import SyntacticGraph
from src.ufu_parser.scanner_consumer import ScannerConsumer
from src.ufu_token import UfuTokenType
from src.ufu_parser.syntax_tree import SyntaxNode


class ComElse:
    bloco: SyntacticGraph

    def parse(self, consumer: ScannerConsumer) -> Optional[SyntaxNode]:
        if not consumer.eat(UfuTokenType.ELSE):
            return None

        bloco = self.bloco.parse(consumer)
        node = SyntaxNode(self.__class__.__name__)
        node.children.append(SyntaxNode(UfuTokenType.ELSE.name))
        node.children.append(bloco)
        return node
