from typing import Optional

from src.ufu_parser.syntactic_graphs.syntactic_graph import SyntacticGraph
from src.ufu_parser.scanner_consumer import ScannerConsumer
from src.ufu_token import UfuTokenType
from src.ufu_parser.syntax_tree import SyntaxNode


class ListaIDs:
    mais_de_um_id: SyntacticGraph

    def parse(self, consumer: ScannerConsumer) -> Optional[SyntaxNode]:
        id_token = consumer.eat_or_exception(UfuTokenType.ID)
        child = self.mais_de_um_id.parse(consumer)

        node = SyntaxNode(self.__class__.__name__)
        node.children.append(SyntaxNode(id_token.type.name, id_token))
        if child:
            node.children += child.children

        return node
