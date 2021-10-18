from src.ufu_parser.syntactic_graphs.syntactic_graph import SyntacticGraph
from src.ufu_parser.scanner_consumer import ScannerConsumer


class ConteudoBloco:
    lista_variaveis: SyntacticGraph
    lista_comandos: SyntacticGraph

    def parse(self, consumer: ScannerConsumer) -> bool:
        self.lista_variaveis.parse(consumer)
        self.lista_comandos.parse(consumer)
        return True
