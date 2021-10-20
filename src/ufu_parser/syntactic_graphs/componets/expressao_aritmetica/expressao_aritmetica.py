from src.ufu_parser.syntactic_graphs.syntactic_graph import SyntacticGraph
from src.ufu_parser.scanner_consumer import ScannerConsumer
from src.ufu_token import UfuTokenType


class ExpressaoAritmetica:
    termo: SyntacticGraph
    expressao_aritmetica_linha: SyntacticGraph

    def parse(self, consumer: ScannerConsumer) -> bool:
        self.termo.parse(consumer)
        self.expressao_aritmetica_linha.parse(consumer)

        return True
