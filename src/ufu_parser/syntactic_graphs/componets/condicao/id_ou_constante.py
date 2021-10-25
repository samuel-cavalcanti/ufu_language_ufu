from typing import Optional

from src.ufu_parser.syntactic_graphs.syntactic_graph import SyntacticGraph
from src.ufu_parser.scanner_consumer import ScannerConsumer
from src.ufu_token import UfuTokenType
from src.ufu_parser.syntax_tree import SyntaxNode


class IdOuConstante:

    def parse(self, consumer: ScannerConsumer) -> Optional[SyntaxNode]:

        for type_token in [UfuTokenType.ID, UfuTokenType.CONST_INT, UfuTokenType.CONST_REAL]:
            token = consumer.eat(type_token)
            if token:
                node = SyntaxNode.from_ufu_token(token)
                consumer.parser_subject.on_complete(type(self), node)
                return node

        token = consumer.eat_or_exception(UfuTokenType.CONST_ASCII)
        node = SyntaxNode.from_ufu_token(token)
        consumer.parser_subject.on_complete(type(self), node)

        return node
