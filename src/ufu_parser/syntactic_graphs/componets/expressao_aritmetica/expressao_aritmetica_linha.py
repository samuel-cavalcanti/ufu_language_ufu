from src.ufu_parser.syntactic_graphs.syntactic_graph import SyntacticGraph
from src.ufu_parser.scanner_consumer import ScannerConsumer
from src.ufu_token import UfuTokenType


class ExpressaoAritmeticaLinha:
    add_ou_sub: SyntacticGraph
    termo: SyntacticGraph

    def parse(self, consumer: ScannerConsumer) -> bool:
        if self.add_ou_sub.parse(consumer):
            self.termo.parse(consumer)

        return True
