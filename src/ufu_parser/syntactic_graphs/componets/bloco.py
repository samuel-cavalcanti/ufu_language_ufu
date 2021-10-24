from typing import Optional

from src.ufu_parser.scanner_consumer import ScannerConsumer
from src.ufu_parser.syntactic_graphs.syntactic_graph import SyntacticGraph
from src.ufu_token import UfuTokenType
from src.ufu_parser.syntax_tree import SyntaxNode


class Bloco:
    conteudo_bloco: SyntacticGraph

    def parse(self, consumer: ScannerConsumer) -> Optional[SyntaxNode]:
        node = SyntaxNode(self.__class__.__name__)
        consumer.parser_subject.on_create(type(self), node)

        consumer.eat_or_exception(UfuTokenType.OPEN_BRACKETS)
        content_block_node = self.conteudo_bloco.parse(consumer)
        consumer.eat_or_exception(UfuTokenType.CLOSE_BRACKETS)

        node.children.append(SyntaxNode(UfuTokenType.OPEN_BRACKETS.name))
        if content_block_node:
            node.children.append(content_block_node)

        node.children.append(SyntaxNode(UfuTokenType.CLOSE_PARENTHESES.name))

        consumer.parser_subject.on_complete(type(self), node)
        return node
