from typing import Protocol, Optional

from .symbol import Symbol


class SymbolTableException(Exception):
    pass


class SymbolTable(Protocol):

    def insert(self, symbol: Symbol) -> None:
        ...

    def get(self, variable_id: str) -> Optional[Symbol]:
        ...

    def create_table(self) -> None:
        ...

    def drop_table(self) -> None:
        ...
