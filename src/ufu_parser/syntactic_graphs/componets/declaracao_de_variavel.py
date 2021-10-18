from src.ufu_parser.syntactic_graphs.syntactic_graph import SyntacticGraph
from src.ufu_parser.scanner_consumer import ScannerConsumer
from src.ufu_token import UfuTokenType


class DeclaracaoDeVariavel:
    lista_ids: SyntacticGraph

    def parse(self, consumer: ScannerConsumer) -> bool:
        if consumer.eat(UfuTokenType.TYPE_VARIABLE):
            consumer.eat_or_exception(UfuTokenType.COLON)
            self.lista_ids.parse(consumer)
            consumer.eat_or_exception(UfuTokenType.SEMICOLON)
            return True
        return False
