from typing import Optional

from src.ufu_parser.syntactic_graphs.syntactic_graph import SyntacticGraph
from src.ufu_parser.scanner_consumer import ScannerConsumer
from src.ufu_token import UfuTokenType
from src.ufu_parser.syntax_tree import SyntaxNode


class AddOuSUb:

    def parse(self, consumer: ScannerConsumer) -> Optional[SyntaxNode]:

        node = SyntaxNode(self.__class__.__name__)

        if consumer.eat(UfuTokenType.ADD):
            node.children.append(SyntaxNode(UfuTokenType.ADD.name))
            return node

        if consumer.eat(UfuTokenType.SUB):
            node.children.append(SyntaxNode(UfuTokenType.SUB.name))
            return node

        return None
