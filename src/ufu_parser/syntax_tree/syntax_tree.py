from .syntax_node import SyntaxNode


class SyntaxTree:
    root: SyntaxNode
    parent: SyntaxNode

    def __init__(self, root: SyntaxNode):
        self.parent = root
        self.root = root

    def insert_new_parent(self, node: SyntaxNode):
        self.parent.childs.append(node)
        self.parent = node

    def insert_node_in_parent(self, node: SyntaxNode):
        self.parent.childs.append(node)

