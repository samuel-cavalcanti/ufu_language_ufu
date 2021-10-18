from src.ufu_parser.syntactic_graphs.syntactic_graph import SyntacticGraph
from src.ufu_parser.scanner_consumer import ScannerConsumer
from src.ufu_token import UfuTokenType


class CmdRepeticaoWhile:
    condicao: SyntacticGraph
    bloco: SyntacticGraph

    def parse(self, consumer: ScannerConsumer) -> bool:
        if consumer.eat(UfuTokenType.WHILE):
            consumer.eat_or_exception(UfuTokenType.OPEN_PARENTHESES)
            self.condicao.parse(consumer)
            consumer.eat_or_exception(UfuTokenType.CLOSE_PARENTHESES)
            return True
        return False
    