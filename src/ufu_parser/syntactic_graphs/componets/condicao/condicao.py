from typing import Optional

from src.ufu_parser.syntactic_graphs.syntactic_graph import SyntacticGraph
from src.ufu_parser.scanner_consumer import ScannerConsumer
from src.ufu_token import UfuTokenType
from src.ufu_parser.syntax_tree import SyntaxNode


class Condicao:
    id_ou_constante: SyntacticGraph
    condicao_linha: SyntacticGraph

    def parse(self, consumer: ScannerConsumer) -> Optional[SyntaxNode]:
        const = self.id_ou_constante.parse(consumer)
        consumer.eat_or_exception(UfuTokenType.RELATIONAL_OPERATOR)
        const_2 = self.id_ou_constante.parse(consumer)

        node = SyntaxNode(self.__class__.__name__)
        node.children.append(const)
        node.children.append(SyntaxNode(UfuTokenType.RELATIONAL_OPERATOR.name))
        node.children.append(const_2)

        return node
