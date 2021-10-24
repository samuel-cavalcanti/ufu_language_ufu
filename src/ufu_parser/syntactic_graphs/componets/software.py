from typing import Optional

from src.ufu_parser.syntactic_graphs.syntactic_graph import SyntacticGraph
from src.ufu_parser.scanner_consumer import ScannerConsumer
from src.ufu_token import UfuTokenType
from src.ufu_parser.syntax_tree import SyntaxNode, SyntaxTree


class Software:
    bloco: SyntacticGraph

    def parse(self, consumer: ScannerConsumer) -> Optional[SyntaxNode]:
        consumer.eat_or_exception(UfuTokenType.PROGRAMA)
        consumer.eat_or_exception(UfuTokenType.ID)
        block_node = self.bloco.parse(consumer)

        node = SyntaxNode(self.__class__.__name__)

        node.children.append(SyntaxNode(UfuTokenType.PROGRAMA.name))
        node.children.append(SyntaxNode(UfuTokenType.ID.name))
        node.children.append(block_node)

        return node
