from typing import Optional

from src.ufu_parser.syntactic_graphs.syntactic_graph import SyntacticGraph
from src.ufu_parser.scanner_consumer import ScannerConsumer
from src.ufu_token import UfuTokenType, UfuToken
from src.ufu_parser.syntax_tree import SyntaxNode


class DeclaracaoDeVariavel:
    lista_ids: SyntacticGraph

    def parse(self, consumer: ScannerConsumer) -> Optional[SyntaxNode]:
        type_variable = consumer.eat(UfuTokenType.TYPE_VARIABLE)
        if not type_variable:
            return None

        consumer.eat_or_exception(UfuTokenType.COLON)
        lista_ids = self.lista_ids.parse(consumer)
        consumer.eat_or_exception(UfuTokenType.SEMICOLON)

        node = self.__create_syntax_node(lista_ids, type_variable)
        consumer.parser_subject.on_complete(type(self), node)
        return node

    def __create_syntax_node(self, lista_ids: SyntaxNode, type_variable: UfuToken) -> SyntaxNode:
        attributes_node = {
            type_variable.type.value: type_variable.content,
            UfuTokenType.ID.value: [node.information.content for node in lista_ids.children],  # ListaIDS:[id,id,... ]
        }
        node = SyntaxNode(self.__class__.__name__, information=attributes_node)
        node.children.append(SyntaxNode.from_ufu_token(type_variable))
        node.children.append(SyntaxNode(UfuTokenType.COLON.name))
        node.children.append(lista_ids)
        node.children.append(SyntaxNode(UfuTokenType.SEMICOLON.name))

        return node
