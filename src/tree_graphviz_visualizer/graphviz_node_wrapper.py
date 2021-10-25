from typing import Protocol

from .graphviz_node import GraphvizNode


class GraphvizNodeWrapper(Protocol):

    def to_graphviz_node(self) -> GraphvizNode:
        ...
