from typing import Optional

from src.ufu_parser.syntactic_graphs.syntactic_graph import SyntacticGraph
from src.ufu_parser.scanner_consumer import ScannerConsumer
from src.ufu_token import UfuTokenType
from src.ufu_parser.syntax_tree import SyntaxNode


class MultOuDiv:

    def parse(self, consumer: ScannerConsumer) -> Optional[SyntaxNode]:

        node = SyntaxNode(self.__class__.__name__)

        if consumer.eat(UfuTokenType.MUL):
            node.children.append(SyntaxNode(UfuTokenType.MUL.name))
            return node

        if consumer.eat(UfuTokenType.DIV):
            node.children.append(SyntaxNode(UfuTokenType.DIV.name))
            return node

        return None
