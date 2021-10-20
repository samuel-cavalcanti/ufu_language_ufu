from typing import Optional

from src.ufu_parser.syntactic_graphs.syntactic_graph import SyntacticGraph
from src.ufu_parser.scanner_consumer import ScannerConsumer
from src.ufu_parser.syntax_tree import SyntaxNode


class Comando:
    cmd_selecao: SyntacticGraph
    cmd_atribuicao: SyntacticGraph
    cmd_repeticao_while: SyntacticGraph
    cmd_repeticao_do_until: SyntacticGraph

    def parse(self, consumer: ScannerConsumer) -> Optional[SyntaxNode]:
        node = SyntaxNode(self.__class__.__name__)

        select = self.cmd_selecao.parse(consumer)
        if select:
            node.children.append(select)
            return node

        repeat_while = self.cmd_repeticao_while.parse(consumer)
        if repeat_while:
            node.children.append(repeat_while)
            return node

        repeat_until = self.cmd_repeticao_do_until.parse(consumer)
        if repeat_until:
            node.children.append(repeat_until)
            return node

        attr = self.cmd_atribuicao.parse(consumer)
        if attr:
            node.children.append(attr)
            return node

        return None
