from typing import Optional

from src.ufu_parser.syntactic_graphs.syntactic_graph import SyntacticGraph
from src.ufu_parser.scanner_consumer import ScannerConsumer
from src.ufu_token import UfuTokenType
from src.ufu_parser.syntax_tree import SyntaxNode


class Termo:
    fator: SyntacticGraph
    termo_linha: SyntacticGraph

    def parse(self, consumer: ScannerConsumer) -> Optional[SyntaxNode]:
        fator = self.fator.parse(consumer)
        termo_linha = self.termo_linha.parse(consumer)

        if termo_linha:
            termo_linha.children.insert(0, fator)
            return termo_linha

        return fator
