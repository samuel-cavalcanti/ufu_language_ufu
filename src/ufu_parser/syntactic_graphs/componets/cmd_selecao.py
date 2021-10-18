from src.ufu_parser.syntactic_graphs.syntactic_graph import SyntacticGraph
from src.ufu_parser.scanner_consumer import ScannerConsumer
from src.ufu_token import UfuTokenType


class CmdSelecao:
    condicao: SyntacticGraph
    bloco: SyntacticGraph
    com_else: SyntacticGraph

    def parse(self, consumer: ScannerConsumer) -> bool:
        if consumer.eat(UfuTokenType.IF):
            self.condicao.parse(consumer)
            consumer.eat_or_exception(UfuTokenType.THEN)
            self.bloco.parse(consumer)
            self.com_else.parse(consumer)
            return True

        return False
