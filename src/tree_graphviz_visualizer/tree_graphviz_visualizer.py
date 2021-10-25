import textwrap
from .graphviz_node import GraphvizNode
from .graphviz_node_wrapper import GraphvizNodeWrapper


class TreeGraphvizVisualizer:
    def __init__(self):

        self.dot_header = [textwrap.dedent("""\
        digraph astgraph {
          node [shape=none, fontsize=12, fontname="Courier", height=.1];
          ranksep=.3;
          edge [arrowsize=.5]
        """)]
        self.dot_body = []
        self.dot_footer = ['}']

    def __append_node_on_body(self, node: GraphvizNode):

        self.dot_body.append(f'node{node.uuid} [label="{node.name}\n {node.information}"]\n')

    def __append_node_connection_on_body(self, origin: GraphvizNode, target: GraphvizNode):
        self.dot_body.append(f'  node{origin.uuid} -> node{target.uuid}\n')

    def __bfs(self, node: GraphvizNodeWrapper):

        queue = [node]

        self.__append_node_on_body(node.to_graphviz_node())

        while len(queue) != 0:
            node = queue.pop(0)
            for child_node in node.children:
                graphviz_node_child = child_node.to_graphviz_node()
                self.__append_node_on_body(graphviz_node_child)
                self.__append_node_connection_on_body(node.to_graphviz_node(), graphviz_node_child)
                queue.append(child_node)

    def generate_graphviz_file(self, root: GraphvizNodeWrapper) -> str:
        self.__bfs(root)
        return ''.join(self.dot_header + self.dot_body + self.dot_footer)
