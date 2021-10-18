from src.ufu_parser.syntactic_graphs.syntactic_graph import SyntacticGraph
from src.ufu_parser.scanner_consumer import ScannerConsumer
from src.ufu_token import UfuTokenType


class CmdAtribuicao:
    expressao: SyntacticGraph

    def parse(self, consumer: ScannerConsumer) -> bool:
        if consumer.eat(UfuTokenType.ID):
            consumer.eat_or_exception(UfuTokenType.ASSIGNMENT_OPERATOR)
            self.expressao.parse(consumer)
            consumer.eat_or_exception(UfuTokenType.SEMICOLON)

            return True

        return False
