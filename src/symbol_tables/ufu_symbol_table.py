from .symbol import Symbol
from .symbol_table import SymbolTableException
from typing import Dict, Optional, List


class UFUSymbolTable:
    __tables = List[Dict[str, Symbol]]

    def __init__(self):
        self.__tables = [{}]

    def insert(self, symbol: Symbol):
        last_table = self.__tables[-1]
        s: Optional[Symbol] = last_table.get(symbol.name)

        if s:
            raise SymbolTableException(f"ID exist! {s.name}")

        last_table[symbol.name] = symbol

    def get(self, variable_id: str) -> Optional[Symbol]:

        for table in reversed(self.__tables):
            symbol = table.get(variable_id)
            if symbol:
                return symbol

        return None

    def new_table(self) -> None:
        self.__tables.append({})
