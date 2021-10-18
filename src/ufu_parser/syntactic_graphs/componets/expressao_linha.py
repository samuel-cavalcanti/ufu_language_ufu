from src.ufu_parser.syntactic_graphs.syntactic_graph import SyntacticGraph
from src.ufu_parser.scanner_consumer import ScannerConsumer
from src.ufu_token import UfuTokenType


class ExpressaoLinha:
    expressao: SyntacticGraph

    def parse(self, consumer: ScannerConsumer) -> bool:
        if consumer.eat(UfuTokenType.ARITHMETIC_OPERATOR):
            self.expressao.parse(consumer)

        return True
