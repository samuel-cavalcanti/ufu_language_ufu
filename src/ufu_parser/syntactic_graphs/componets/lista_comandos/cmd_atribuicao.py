from typing import Optional

from src.ufu_parser.syntactic_graphs.syntactic_graph import SyntacticGraph
from src.ufu_parser.scanner_consumer import ScannerConsumer
from src.ufu_token import UfuTokenType
from src.ufu_parser.syntax_tree import SyntaxNode


class CmdAtribuicao:
    expressao_aritmetica_ou_const_ascii: SyntacticGraph

    def parse(self, consumer: ScannerConsumer) -> Optional[SyntaxNode]:
        id_token = consumer.eat(UfuTokenType.ID)
        if not id_token:
            return None

        consumer.eat_or_exception(UfuTokenType.ASSIGNMENT_OPERATOR)
        expressao = self.expressao_aritmetica_ou_const_ascii.parse(consumer)
        consumer.eat_or_exception(UfuTokenType.SEMICOLON)

        node = SyntaxNode(self.__class__.__name__, information={id_token.type.value: id_token.content})

        node.children.append(SyntaxNode.from_ufu_token(id_token))
        node.children.append(SyntaxNode(UfuTokenType.ASSIGNMENT_OPERATOR.name))
        node.children.append(expressao)
        node.children.append(SyntaxNode(UfuTokenType.SEMICOLON.name))

        consumer.parser_subject.on_complete(type(self), node)

        return node
