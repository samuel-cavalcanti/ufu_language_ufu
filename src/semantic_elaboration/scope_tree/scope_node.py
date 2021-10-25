from dataclasses import dataclass

from src.symbol_tables.symbol_table import SymbolTable
from src.tree_graphviz_visualizer import GraphvizNode
from typing import Any, Optional


@dataclass
class ScopeNode:
    table: SymbolTable
    name: str
    children: list
    level: int
    parent: Optional[Any]  # Optional[ScopeNode]

    def to_graphviz_node(self) -> GraphvizNode:
        return GraphvizNode(name=self.name, children=self.children, information=self.table, uuid=id(self))
