from src.ufu_parser.scanner_consumer import ScannerConsumer
from src.ufu_parser.syntactic_graphs.syntactic_graph import SyntacticGraph
from src.ufu_token import UfuTokenType


class Bloco:
    conteudo_bloco: SyntacticGraph

    def parse(self, consumer: ScannerConsumer) -> bool:
        consumer.eat_or_exception(UfuTokenType.OPEN_BRACKETS)
        self.conteudo_bloco.parse(consumer)
        consumer.eat_or_exception(UfuTokenType.CLOSE_BRACKETS)
        return True
