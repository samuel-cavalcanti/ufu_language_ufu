from .symbol import Symbol
from .symbol_table import SymbolTableException
from typing import Dict, Optional, List


class UFUSymbolTable:
    __table = Dict[str, Symbol]

    def __init__(self):
        self.__table = dict()

    def __str__(self) -> str:
        return str(self.__table)

    def insert(self, symbol: Symbol):
        s: Optional[Symbol] = self.__table.get(symbol.name)

        if s:
            raise SymbolTableException(f"ID exist! {s.name}")

        self.__table[symbol.name] = symbol

    def get(self, variable_id: str) -> Optional[Symbol]:
        return self.__table.get(variable_id)
