from src.ufu_parser.syntactic_graphs.syntactic_graph import SyntacticGraph
from src.ufu_parser.scanner_consumer import ScannerConsumer
from src.ufu_token import UfuTokenType


class Software:
    bloco: SyntacticGraph

    def parse(self, consumer: ScannerConsumer) -> bool:
        consumer.eat_or_exception(UfuTokenType.PROGRAMA)
        consumer.eat_or_exception(UfuTokenType.ID)
        self.bloco.parse(consumer)
        return True
