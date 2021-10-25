from typing import Callable
from src.ufu_parser.syntax_tree import SyntaxNode
from .observer import Observer


class SimpleObserver:
    def on_create(self, node: SyntaxNode) -> None:
        pass

    def on_next(self, node: SyntaxNode) -> None:
        pass

    def on_complete(self, node: SyntaxNode) -> None:
        pass


class ObserverBuilder:
    __observer: Observer

    def __init__(self):
        self.__observer = SimpleObserver()

    def set_on_create(self, function: Callable[[SyntaxNode], None]):
        self.__observer.on_create = function
        return self

    def set_on_next(self, function: Callable[[SyntaxNode], None]):
        self.__observer.on_next = function
        return self

    def set_on_complete(self, function: Callable[[SyntaxNode], None]):
        self.__observer.on_complete = function
        return self

    def build(self) -> Observer:
        return self.__observer
