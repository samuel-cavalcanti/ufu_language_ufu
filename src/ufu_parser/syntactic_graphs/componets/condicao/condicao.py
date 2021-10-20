from src.ufu_parser.syntactic_graphs.syntactic_graph import SyntacticGraph
from src.ufu_parser.scanner_consumer import ScannerConsumer
from src.ufu_token import UfuTokenType


class Condicao:
    id_ou_constante: SyntacticGraph
    condicao_linha: SyntacticGraph

    def parse(self, consumer: ScannerConsumer) -> bool:
        self.id_ou_constante.parse(consumer)
        consumer.eat_or_exception(UfuTokenType.RELATIONAL_OPERATOR)
        self.id_ou_constante.parse(consumer)
        self.condicao_linha.parse(consumer)

        return True
