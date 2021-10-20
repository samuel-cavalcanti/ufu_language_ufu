from typing import Optional

from src.ufu_parser.syntactic_graphs.syntactic_graph import SyntacticGraph
from src.ufu_parser.scanner_consumer import ScannerConsumer
from src.ufu_token import UfuTokenType
from src.ufu_parser.syntax_tree import SyntaxNode


class MaisDeUmID:
    lista_ids: SyntacticGraph

    def parse(self, consumer: ScannerConsumer) -> Optional[SyntaxNode]:
        if consumer.eat(UfuTokenType.COMMA) is False:
            return None

        child = self.lista_ids.parse(consumer)
        node = SyntaxNode(self.__class__.__name__)
        node.children.append(SyntaxNode(UfuTokenType.COMMA.name))
        node.children.append(child)
        return node
