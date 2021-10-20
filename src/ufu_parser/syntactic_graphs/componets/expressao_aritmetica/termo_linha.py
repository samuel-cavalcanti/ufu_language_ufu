from src.ufu_parser.syntactic_graphs.syntactic_graph import SyntacticGraph
from src.ufu_parser.scanner_consumer import ScannerConsumer
from src.ufu_token import UfuTokenType


class TermoLinha:
    mult_ou_div: SyntacticGraph
    fator: SyntacticGraph

    def parse(self, consumer: ScannerConsumer) -> bool:
        if self.mult_ou_div.parse(consumer):
            self.fator.parse(consumer)

        return True
