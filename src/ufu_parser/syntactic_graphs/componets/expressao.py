from src.ufu_parser.syntactic_graphs.syntactic_graph import SyntacticGraph
from src.ufu_parser.scanner_consumer import ScannerConsumer
from src.ufu_token import UfuTokenType


class Expressao:
    id_ou_constante: SyntacticGraph
    expressao_linha: SyntacticGraph

    def parse(self, consumer: ScannerConsumer) -> bool:
        self.id_ou_constante.parse(consumer)
        self.expressao_linha.parse(consumer)

        return True
