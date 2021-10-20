from typing import Optional

from src.ufu_parser.syntactic_graphs.syntactic_graph import SyntacticGraph
from src.ufu_parser.scanner_consumer import ScannerConsumer
from src.ufu_token import UfuTokenType
from src.ufu_parser.syntax_tree import SyntaxNode


class IdOuConstante:

    def parse(self, consumer: ScannerConsumer) -> Optional[SyntaxNode]:

        node = SyntaxNode(self.__class__.__name__)

        if consumer.eat(UfuTokenType.ID):
            node.children.append(SyntaxNode(UfuTokenType.ID.name))
            return node

        if consumer.eat(UfuTokenType.CONST_INT):
            node.children.append(SyntaxNode(UfuTokenType.CONST_INT.name))
            return node

        if consumer.eat(UfuTokenType.CONST_REAL):
            node.children.append(SyntaxNode(UfuTokenType.CONST_REAL.name))
            return node

        consumer.eat_or_exception(UfuTokenType.CONST_ASCII)
        node.children.append(SyntaxNode(UfuTokenType.CONST_ASCII.name))

        return node
