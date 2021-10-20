from typing import Optional

from src.ufu_parser.syntactic_graphs.syntactic_graph import SyntacticGraph
from src.ufu_parser.scanner_consumer import ScannerConsumer
from src.ufu_parser.syntax_tree import SyntaxNode, SyntaxTree
from src.ufu_parser.syntax_tree import SyntaxNode


class ConteudoBloco:
    lista_variaveis: SyntacticGraph
    lista_comandos: SyntacticGraph

    def parse(self, consumer: ScannerConsumer) -> Optional[SyntaxNode]:
        node = SyntaxNode(self.__class__.__name__)
        variables = self.lista_variaveis.parse(consumer)
        commands = self.lista_comandos.parse(consumer)

        if not variables and not commands:
            return None

        if variables:
            node.children.append(variables)

        if commands:
            node.children.append(commands)

        return node
