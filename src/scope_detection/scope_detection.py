from src.semantic_elaboration.scope_tree import ScopeTree
from src.ufu_parser.parser_observer import Observer, ObserverBuilder
from src.ufu_parser.syntax_tree import SyntaxNode
from src.symbol_tables import UFUSymbolTable, Symbol
from src.ufu_token import UfuTokenType
from typing import Optional


class ScopeException(Exception):
    pass


class ScopeDetection:
    scope_tree: Optional[ScopeTree]

    def __init__(self):
        self.scope_tree = None

    def verify_variable_declaration(self, variable_id: str):

        symbol = self.scope_tree.look_up(variable_id)

        if symbol:
            return

        raise ScopeException(f"Variable not declared: {variable_id}")

    def new_scope(self, name: str):
        if self.scope_tree is None:
            self.scope_tree = ScopeTree(UFUSymbolTable())
            return
        self.scope_tree.new_scope(table=UFUSymbolTable(), scope_name=name)

    def back_scope(self):
        self.scope_tree.back_scope()

    def insert_symbol_on_current_scope(self, symbol: Symbol):
        self.scope_tree.insert_symbol(symbol)
