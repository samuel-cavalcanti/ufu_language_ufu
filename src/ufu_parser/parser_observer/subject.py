from typing import Protocol

from src.ufu_parser.syntax_tree import SyntaxNode
from .observer import Observer


class SubjectException(Exception):
    pass


class Subject(Protocol):

    def attach(self, graph: type, observer: Observer) -> None:
        ...

    def detach(self, graph: type,  observer: Observer) -> None:
        ...

    def on_create(self, graph: type, node: SyntaxNode) -> None:
        ...

    def on_next(self, graph: type, node: SyntaxNode) -> None:
        ...

    def on_complete(self, graph: type, node: SyntaxNode) -> None:
        ...
