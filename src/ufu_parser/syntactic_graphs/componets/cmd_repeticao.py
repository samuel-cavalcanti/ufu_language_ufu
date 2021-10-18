from src.ufu_parser.syntactic_graphs.syntactic_graph import SyntacticGraph
from src.ufu_parser.scanner_consumer import ScannerConsumer
from src.ufu_token import UfuTokenType


class CmdRepeticao:
    cmd_repeticao_while: SyntacticGraph
    cmd_repeticao_do_until: SyntacticGraph

    def parse(self, consumer: ScannerConsumer) -> bool:

        if self.cmd_repeticao_while.parse(consumer):
            return True

        if self.cmd_repeticao_do_until.parse(consumer):
            return True

        return False
