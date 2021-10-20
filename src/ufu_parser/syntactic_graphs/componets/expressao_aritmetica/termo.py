from src.ufu_parser.syntactic_graphs.syntactic_graph import SyntacticGraph
from src.ufu_parser.scanner_consumer import ScannerConsumer
from src.ufu_token import UfuTokenType


class Termo:
    fator: SyntacticGraph
    termo_linha: SyntacticGraph

    def parse(self, consumer: ScannerConsumer) -> bool:
        self.fator.parse(consumer)
        self.termo_linha.parse(consumer)

        return True
