from typing import Protocol

from src.ufu_parser.syntax_tree import SyntaxNode


class Observer(Protocol):

    def on_create(self, node: SyntaxNode) -> None:
        ...

    def on_next(self, node: SyntaxNode) -> None:
        ...

    def on_complete(self, node: SyntaxNode) -> None:
        ...
