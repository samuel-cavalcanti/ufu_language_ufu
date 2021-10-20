from typing import Optional

from src.ufu_parser.syntactic_graphs.syntactic_graph import SyntacticGraph
from src.ufu_parser.scanner_consumer import ScannerConsumer
from src.ufu_token import UfuTokenType
from src.ufu_parser.syntax_tree import SyntaxNode


class CmdSelecao:
    condicao: SyntacticGraph
    bloco: SyntacticGraph
    com_else: SyntacticGraph

    def parse(self, consumer: ScannerConsumer) -> Optional[SyntaxNode]:
        if not consumer.eat(UfuTokenType.IF):
            return None

        consumer.eat_or_exception(UfuTokenType.OPEN_PARENTHESES)
        condicao = self.condicao.parse(consumer)
        consumer.eat_or_exception(UfuTokenType.CLOSE_PARENTHESES)
        consumer.eat_or_exception(UfuTokenType.THEN)

        bloco = self.bloco.parse(consumer)
        com_else = self.com_else.parse(consumer)

        node = SyntaxNode(self.__class__.__name__)

        node.children.append(SyntaxNode(UfuTokenType.IF.name))
        node.children.append(SyntaxNode(UfuTokenType.OPEN_PARENTHESES.name))
        node.children.append(condicao)
        node.children.append(SyntaxNode(UfuTokenType.CLOSE_PARENTHESES.name))
        node.children.append(SyntaxNode(UfuTokenType.THEN.name))
        node.children.append(bloco)
        if com_else:
            node.children.append(com_else)

        return node
