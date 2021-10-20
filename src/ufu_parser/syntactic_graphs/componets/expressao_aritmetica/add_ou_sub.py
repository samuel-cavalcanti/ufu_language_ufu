from src.ufu_parser.syntactic_graphs.syntactic_graph import SyntacticGraph
from src.ufu_parser.scanner_consumer import ScannerConsumer
from src.ufu_token import UfuTokenType


class AddOuSUb:

    def parse(self, consumer: ScannerConsumer) -> bool:

        if consumer.eat(UfuTokenType.ADD):
            return True

        if consumer.eat(UfuTokenType.SUB):
            return True

        return False
