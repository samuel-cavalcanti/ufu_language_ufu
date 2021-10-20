from src.ufu_parser.syntactic_graphs.syntactic_graph import SyntacticGraph
from src.ufu_parser.scanner_consumer import ScannerConsumer
from src.ufu_token import UfuTokenType


class IdOuConstante:

    def parse(self, consumer: ScannerConsumer) -> bool:
        if consumer.eat(UfuTokenType.ID):
            return True

        if consumer.eat(UfuTokenType.CONST_INT):
            return True

        if consumer.eat(UfuTokenType.CONST_REAL):
            return True

        consumer.eat_or_exception(UfuTokenType.CONST_ASCII)

        return True
