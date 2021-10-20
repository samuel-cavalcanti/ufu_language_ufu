from typing import Optional

from src.ufu_parser.syntactic_graphs.syntactic_graph import SyntacticGraph
from src.ufu_parser.scanner_consumer import ScannerConsumer
from src.ufu_token import UfuTokenType
from src.ufu_parser.syntax_tree import SyntaxNode


class CondicaoLinha:
    condicao: SyntacticGraph

    def parse(self, consumer: ScannerConsumer) -> Optional[SyntaxNode]:
        if not consumer.eat(UfuTokenType.RELATIONAL_OPERATOR):
            return None

        condicao = self.condicao.parse(consumer)

        node = SyntaxNode(self.__class__.__name__)
        node.children.append(SyntaxNode(UfuTokenType.RELATIONAL_OPERATOR.name))
        node.children.append(condicao)

        return node
