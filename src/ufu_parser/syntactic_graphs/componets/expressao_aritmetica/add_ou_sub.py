from typing import Optional

from src.ufu_parser.syntactic_graphs.syntactic_graph import SyntacticGraph
from src.ufu_parser.scanner_consumer import ScannerConsumer
from src.ufu_token import UfuTokenType
from src.ufu_parser.syntax_tree import SyntaxNode


class AddOuSUb:

    def parse(self, consumer: ScannerConsumer) -> Optional[SyntaxNode]:

        for token_type in [UfuTokenType.ADD, UfuTokenType.SUB]:
            token = consumer.eat(token_type)
            if token:
                return SyntaxNode.from_ufu_token(token)

        return None
