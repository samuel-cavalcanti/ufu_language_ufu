from typing import Optional

from src.ufu_parser.syntactic_graphs.syntactic_graph import SyntacticGraph
from src.ufu_parser.scanner_consumer import ScannerConsumer
from src.ufu_token import UfuTokenType
from src.ufu_parser.syntax_tree import SyntaxNode


class DeclaracaoDeVariavel:
    lista_ids: SyntacticGraph

    def parse(self, consumer: ScannerConsumer) -> Optional[SyntaxNode]:
        type_variable = consumer.eat(UfuTokenType.TYPE_VARIABLE)
        if not type_variable:
            return None

        consumer.eat_or_exception(UfuTokenType.COLON)
        child = self.lista_ids.parse(consumer)
        consumer.eat_or_exception(UfuTokenType.SEMICOLON)

        node = SyntaxNode(self.__class__.__name__)
        node.children.append(SyntaxNode(UfuTokenType.TYPE_VARIABLE.name))
        node.children.append(SyntaxNode(UfuTokenType.COLON.name))
        node.children.append(child)
        node.children.append(SyntaxNode(UfuTokenType.SEMICOLON.name))

        return node
