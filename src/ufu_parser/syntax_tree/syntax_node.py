from typing import Optional
from src.ufu_token import UfuToken
from src.tree_graphviz_visualizer import GraphvizNode


class SyntaxNode:
    name: str
    children: list
    information = Optional[dict]

    def __init__(self, name: str, information: Optional[dict] = None):
        self.name = name
        self.children = list()
        self.information = information

    def to_graphviz_node(self) -> GraphvizNode:
        return GraphvizNode(name=self.name, children=self.children, information=self.information, uuid=id(self))

    @staticmethod
    def from_ufu_token(token: UfuToken):
        return SyntaxNode(token.type.name, information={token.type.value: token.content})

    def __str__(self):
        return f"name: {self.name} children: {self.children} information: {self.information}"
