from typing import Protocol, Callable

from src.ufu_parser.syntax_tree import SyntaxNode


class SubjectException(Exception):
    pass


class Subject(Protocol):

    def attach(self, graph: type, callback: Callable[[SyntaxNode], None]) -> None:
        ...

    def detach(self, graph: type, callback: Callable[[SyntaxNode], None]) -> None:
        ...

    def notify(self, graph: type, node: SyntaxNode) -> None:
        ...
