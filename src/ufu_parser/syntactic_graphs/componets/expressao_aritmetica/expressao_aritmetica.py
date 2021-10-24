from typing import Optional

from src.ufu_parser.syntactic_graphs.syntactic_graph import SyntacticGraph
from src.ufu_parser.scanner_consumer import ScannerConsumer
from src.ufu_token import UfuTokenType
from src.ufu_parser.syntax_tree import SyntaxNode


class ExpressaoAritmetica:
    termo: SyntacticGraph
    expressao_aritmetica_linha: SyntacticGraph

    def parse(self, consumer: ScannerConsumer) -> Optional[SyntaxNode]:
        termo = self.termo.parse(consumer)
        expressao_linha = self.expressao_aritmetica_linha.parse(consumer)

        if expressao_linha:
            if termo.name in [UfuTokenType.DIV.name, UfuTokenType.MUL.name]:
                expressao_linha.children.insert(0, termo)
            else:
                expressao_linha.children.append(termo)
            return expressao_linha

        return termo
