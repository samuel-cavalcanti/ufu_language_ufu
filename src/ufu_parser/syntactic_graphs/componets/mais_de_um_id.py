from src.ufu_parser.syntactic_graphs.syntactic_graph import SyntacticGraph
from src.ufu_parser.scanner_consumer import ScannerConsumer
from src.ufu_token import UfuTokenType


class MaisDeUmID:
    lista_ids: SyntacticGraph

    def parse(self, consumer: ScannerConsumer) -> bool:
        if consumer.eat(UfuTokenType.COMMA):
            self.lista_ids.parse(consumer)
        return True
