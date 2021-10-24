from dataclasses import dataclass

from src.symbol_tables.symbol_table import SymbolTable
from typing import Any, Optional


@dataclass
class ScopeNode:
    table: SymbolTable
    name: str
    children: list
    level: int
    parent: Optional[Any]  # Optional[ScopeNode]
