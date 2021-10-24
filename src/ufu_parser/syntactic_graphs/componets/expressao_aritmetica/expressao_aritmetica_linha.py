from typing import Optional

from src.ufu_parser.syntactic_graphs.syntactic_graph import SyntacticGraph
from src.ufu_parser.scanner_consumer import ScannerConsumer
from src.ufu_token import UfuTokenType
from src.ufu_parser.syntax_tree import SyntaxNode


class ExpressaoAritmeticaLinha:
    add_ou_sub: SyntacticGraph
    termo: SyntacticGraph

    def parse(self, consumer: ScannerConsumer) -> Optional[SyntaxNode]:
        add_ou_sub = self.add_ou_sub.parse(consumer)

        if not add_ou_sub:
            return None

        termo = self.termo.parse(consumer)
        expressao_linha = self.parse(consumer)

        if expressao_linha:
            expressao_linha.children.append(termo)
            add_ou_sub.children.append(expressao_linha)

        else:
            add_ou_sub.children.append(termo)

        return add_ou_sub
