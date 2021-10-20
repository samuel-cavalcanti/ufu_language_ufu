from typing import Optional

from src.ufu_parser.syntactic_graphs.syntactic_graph import SyntacticGraph
from src.ufu_parser.scanner_consumer import ScannerConsumer
from src.ufu_parser.syntax_tree import SyntaxNode


class ListaComandos:
    comando: SyntacticGraph

    def parse(self, consumer: ScannerConsumer) -> Optional[SyntaxNode]:
        child = self.comando.parse(consumer)
        if not child:
            return None

        node = SyntaxNode(self.__class__.__name__)

        while child:
            node.children.append(child)
            child = self.comando.parse(consumer)

        return node
