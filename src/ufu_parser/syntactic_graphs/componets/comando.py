from src.ufu_parser.syntactic_graphs.syntactic_graph import SyntacticGraph
from src.ufu_parser.scanner_consumer import ScannerConsumer


class Comando:
    cmd_selecao: SyntacticGraph
    cmd_repeticao: SyntacticGraph
    cmd_atribuicao: SyntacticGraph

    def parse(self, consumer: ScannerConsumer) -> bool:
        if self.cmd_selecao.parse(consumer):
            return True
        if self.cmd_repeticao.parse(consumer):
            return True
        if self.cmd_atribuicao.parse(consumer):
            return True

        return False
