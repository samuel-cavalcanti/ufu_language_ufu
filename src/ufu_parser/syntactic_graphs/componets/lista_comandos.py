from src.ufu_parser.syntactic_graphs.syntactic_graph import SyntacticGraph
from src.ufu_parser.scanner_consumer import ScannerConsumer


class ListaComandos:
    comando: SyntacticGraph

    def parse(self, consumer: ScannerConsumer) -> bool:
        while self.comando.parse(consumer):
            pass

        return True
