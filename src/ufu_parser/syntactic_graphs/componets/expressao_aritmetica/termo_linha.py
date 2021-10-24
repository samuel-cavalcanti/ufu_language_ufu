from typing import Optional

from src.ufu_parser.syntactic_graphs.syntactic_graph import SyntacticGraph
from src.ufu_parser.scanner_consumer import ScannerConsumer
from src.ufu_token import UfuTokenType
from src.ufu_parser.syntax_tree import SyntaxNode


class TermoLinha:
    mult_ou_div: SyntacticGraph
    fator: SyntacticGraph

    def parse(self, consumer: ScannerConsumer) -> Optional[SyntaxNode]:
        mult_ou_div = self.mult_ou_div.parse(consumer)

        if not mult_ou_div:
            return None

        fator = self.fator.parse(consumer)
        termo_linha = self.parse(consumer)

        mult_ou_div.children.append(fator)

        if termo_linha:
            mult_ou_div.children.append(termo_linha)

        return mult_ou_div
