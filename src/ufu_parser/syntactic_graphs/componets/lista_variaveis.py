from src.ufu_parser.syntactic_graphs.syntactic_graph import SyntacticGraph
from src.ufu_parser.scanner_consumer import ScannerConsumer


class ListaVariaveis:
    declaracao_de_variavel: SyntacticGraph

    def parse(self, consumer: ScannerConsumer) -> bool:
        while self.declaracao_de_variavel.parse(consumer):
            pass

        return True
