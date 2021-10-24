from typing import Protocol, Optional

from .symbol import Symbol


class SymbolTableException(Exception):
    pass


class SymbolTable(Protocol):

    def insert(self, symbol: Symbol) -> None:
        ...

    def get(self, variable_id: str) -> Optional[Symbol]:
        ...
