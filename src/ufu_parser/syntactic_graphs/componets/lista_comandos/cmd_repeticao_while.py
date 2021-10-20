from typing import Optional

from src.ufu_parser.syntactic_graphs.syntactic_graph import SyntacticGraph
from src.ufu_parser.scanner_consumer import ScannerConsumer
from src.ufu_token import UfuTokenType
from src.ufu_parser.syntax_tree import SyntaxNode


class CmdRepeticaoWhile:
    condicao: SyntacticGraph
    bloco: SyntacticGraph

    def parse(self, consumer: ScannerConsumer) -> Optional[SyntaxNode]:
        if not consumer.eat(UfuTokenType.WHILE):
            return None

        consumer.eat_or_exception(UfuTokenType.OPEN_PARENTHESES)
        condicao = self.condicao.parse(consumer)
        consumer.eat_or_exception(UfuTokenType.CLOSE_PARENTHESES)
        bloco = self.bloco.parse(consumer)

        node = SyntaxNode(self.__class__.__name__)
        node.children.append(SyntaxNode(UfuTokenType.WHILE.name))
        node.children.append(SyntaxNode(UfuTokenType.OPEN_PARENTHESES.name))
        node.children.append(condicao)
        node.children.append(SyntaxNode(UfuTokenType.CLOSE_PARENTHESES.name))
        node.children.append(bloco)

        return node
