from typing import Optional

from src.ufu_parser.syntactic_graphs.syntactic_graph import SyntacticGraph
from src.ufu_parser.scanner_consumer import ScannerConsumer
from src.ufu_token import UfuTokenType
from src.ufu_parser.syntax_tree import SyntaxNode


class Fator:

    def parse(self, consumer: ScannerConsumer) -> Optional[SyntaxNode]:

        node = SyntaxNode(self.__class__.__name__)

        expected_tokens_type = [UfuTokenType.ID, UfuTokenType.CONST_INT, UfuTokenType.CONST_REAL]

        for token_type in expected_tokens_type:
            token = consumer.eat(token_type)
            if token:
                # node.children.append(SyntaxNode.from_ufu_token(token))
                return SyntaxNode.from_ufu_token(token)

        consumer.eat_or_exception(UfuTokenType.OPEN_PARENTHESES)

        expressao = self.expressao_aritmetica.parse(consumer)

        consumer.eat_or_exception(UfuTokenType.CLOSE_PARENTHESES)

        return expressao
