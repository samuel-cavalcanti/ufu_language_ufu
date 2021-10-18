from src.ufu_parser.syntactic_graphs.syntactic_graph import SyntacticGraph
from src.ufu_parser.scanner_consumer import ScannerConsumer
from src.ufu_token import UfuTokenType


class ListaIDs:
    mais_de_um_id: SyntacticGraph

    def parse(self, consumer: ScannerConsumer) -> bool:
        consumer.eat_or_exception(UfuTokenType.ID)
        self.mais_de_um_id.parse(consumer)

        return True
