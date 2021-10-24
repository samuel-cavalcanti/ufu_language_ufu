from .scope_node import ScopeNode

from src.symbol_tables import SymbolTable, Symbol

from typing import Optional


class ScopeTree:
    root: ScopeNode
    current_scope: ScopeNode

    def __init__(self, table: SymbolTable):
        self.root = ScopeNode(table=table, name='Global', children=list(), level=0, parent=None)
        self.current_scope = self.root

    def new_scope(self, table: SymbolTable, scope_name: str):
        node = ScopeNode(table=table,
                         name=scope_name,
                         children=list(),
                         level=self.current_scope.level + 1,
                         parent=self.current_scope)

        self.current_scope = node

    def back_scope(self):
        if self.current_scope.parent:
            self.current_scope = self.current_scope.parent

    def look_up(self, variable_id: str) -> Optional[Symbol]:
        return self.__get_symbol(variable_id, self.current_scope)

    def __get_symbol(self, variable_id: str, node: ScopeNode) -> Optional[Symbol]:
        symbol = node.table.get(variable_id)
        if symbol:
            return symbol

        if node.parent:
            return self.__get_symbol(variable_id, node.parent)

        return None
