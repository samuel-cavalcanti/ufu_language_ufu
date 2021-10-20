from typing import Optional
from src.ufu_parser.syntactic_graphs.syntactic_graph import SyntacticGraph
from src.ufu_parser.scanner_consumer import ScannerConsumer
from src.ufu_token import UfuTokenType
from src.ufu_parser.syntax_tree import SyntaxNode


class CmdRepeticaoDoUntil:
    bloco: SyntacticGraph
    condicao: SyntacticGraph

    def parse(self, consumer: ScannerConsumer) -> Optional[SyntaxNode]:
        if not consumer.eat(UfuTokenType.DO):
            return None

        bloco = self.bloco.parse(consumer)
        consumer.eat_or_exception(UfuTokenType.UNTIL)
        consumer.eat_or_exception(UfuTokenType.OPEN_PARENTHESES)
        condicao = self.condicao.parse(consumer)
        consumer.eat_or_exception(UfuTokenType.CLOSE_PARENTHESES)
        consumer.eat_or_exception(UfuTokenType.SEMICOLON)

        node = SyntaxNode(self.__class__.__name__)

        node.children.append(SyntaxNode(UfuTokenType.DO.name))
        node.children.append(bloco)
        node.children.append(SyntaxNode(UfuTokenType.UNTIL.name))
        node.children.append(SyntaxNode(UfuTokenType.OPEN_PARENTHESES.name))
        node.children.append(condicao)
        node.children.append(SyntaxNode(UfuTokenType.CLOSE_PARENTHESES.name))
        node.children.append(SyntaxNode(UfuTokenType.SEMICOLON.name))

        return node
