from typing import Optional

from src.ufu_parser.syntactic_graphs.syntactic_graph import SyntacticGraph
from src.ufu_parser.scanner_consumer import ScannerConsumer
from src.ufu_token import UfuTokenType
from src.ufu_parser.syntax_tree import SyntaxNode


class ExpressaoAritmeticaOuConstAscii:
    expressao_aritmetica: SyntacticGraph

    def parse(self, consumer: ScannerConsumer) -> Optional[SyntaxNode]:
        if consumer.eat(UfuTokenType.CONST_ASCII):
            return SyntaxNode(UfuTokenType.CONST_ASCII.name)
        expressao = self.expressao_aritmetica.parse(consumer)

        node = SyntaxNode(self.__class__.__name__)
        node.children.append(expressao)
        return node
