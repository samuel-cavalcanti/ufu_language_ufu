from src.ufu_parser.syntactic_graphs.syntactic_graph import SyntacticGraph
from src.ufu_parser.scanner_consumer import ScannerConsumer
from src.ufu_token import UfuTokenType


class ExpressaoAritmeticaOuConstAscii:
    expressao_aritmetica: SyntacticGraph

    def parse(self, consumer: ScannerConsumer) -> bool:
        if consumer.eat(UfuTokenType.CONST_ASCII):
            return True

        self.expressao_aritmetica.parse(consumer)
        return True
