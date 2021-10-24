from typing import List, Optional, Any, Dict, Callable, NewType
from .subject import SubjectException
from src.ufu_parser.syntactic_graphs import componets as graph_components
from src.ufu_parser.syntax_tree import SyntaxNode
from src.ufu_parser.syntactic_graphs.componets import *
import inspect

from .observer import Observer


class ParserSubject:
    __observers: Dict[type, List[Observer]]

    def __init__(self):
        self.__observers = {}

        for name, obj in inspect.getmembers(graph_components):
            if inspect.isclass(obj):
                self.__observers[obj] = []

    def attach(self, graph: type, observer: Observer) -> None:
        observers = self.__observers_or_exception(graph)
        observers.append(observer)

    def detach(self, graph: type, observer: Observer) -> None:
        observers = self.__observers_or_exception(graph)
        observers.remove(observer)

    def on_create(self, graph: type, node: SyntaxNode) -> None:
        for observer in self.__observers_or_exception(graph):
            observer.on_create(node)

    def on_next(self, graph: type, node: SyntaxNode) -> None:
        for observer in self.__observers_or_exception(graph):
            observer.on_next(node)

    def on_complete(self, graph: type, node: SyntaxNode) -> None:
        for observer in self.__observers_or_exception(graph):
            observer.on_complete(node)

    def __observers_or_exception(self, graph: type, ) -> List[Observer]:

        observers = self.__observers.get(graph, None)

        if observers is None:
            raise SubjectException(f"Observers Not Found for {graph}")

        return observers
