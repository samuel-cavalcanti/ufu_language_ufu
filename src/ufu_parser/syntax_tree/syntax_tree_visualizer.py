import textwrap
from .syntax_node import SyntaxNode


class SyntaxTreeGraphvizVisualizer(object):
    def __init__(self):

        self.dot_header = [textwrap.dedent("""\
        digraph astgraph {
          node [shape=none, fontsize=12, fontname="Courier", height=.1];
          ranksep=.3;
          edge [arrowsize=.5]
        """)]
        self.dot_body = []
        self.dot_footer = ['}']

    def __append_node_on_body(self, node: SyntaxNode):
        self.dot_body.append(f'node{id(node)} [label="{node.name}"]\n')

    def __append_node_connection_on_body(self, origin: SyntaxNode, target: SyntaxNode):
        self.dot_body.append(f'  node{id(origin)} -> node{id(target)}\n')

    def __bfs(self, node: SyntaxNode):

        queue = [node]

        self.__append_node_on_body(node)

        while len(queue) != 0:
            node = queue.pop(0)
            for child_node in node.children:
                self.__append_node_on_body(child_node)
                self.__append_node_connection_on_body(node, child_node)
                queue.append(child_node)

    def generate_graphviz_file(self, root: SyntaxNode) -> str:
        self.__bfs(root)
        return ''.join(self.dot_header + self.dot_body + self.dot_footer)
