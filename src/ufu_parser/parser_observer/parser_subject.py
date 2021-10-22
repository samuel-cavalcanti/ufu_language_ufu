from typing import List, Optional, Any, Dict, Callable
from .subject import SubjectException
from src.ufu_parser.syntactic_graphs import componets as graph_components
from src.ufu_parser.syntax_tree import SyntaxNode
from src.ufu_parser.syntactic_graphs.componets import *
import inspect


class ParserSubject:
    __listeners: Dict[type, List[Callable[[SyntaxNode], None]]]

    def __init__(self):
        self.__listeners = {}
        for name, obj in inspect.getmembers(graph_components):
            if inspect.isclass(obj):
                self.__listeners[obj] = []
        # self.__listeners = {
        #     Bloco: [],
        #     DeclaracaoDeVariavel: [],
        #     CmdAtribuicao: [],
        #     IdOuConstante: [],
        #     Fator: [],
        # }

    def attach(self, graph: type, callback: Callable[[SyntaxNode], None]) -> None:
        observers = self.__observers_or_exception(graph)

        observers.append(callback)

    def detach(self, graph: type, callback: Callable[[SyntaxNode], None]) -> None:
        observers = self.__observers_or_exception(graph)

        observers.remove(callback)

    def on_next(self, graph: type, node: SyntaxNode) -> None:
        for observer in self.__observers_or_exception(graph):
            observer(node)

    def on_complete(self, graph: type, node: SyntaxNode) -> None:
        self.on_next(graph, node)

    def __observers_or_exception(self, graph: type) -> List[Callable[[SyntaxNode], None]]:
        callbacks = self.__listeners.get(graph, None)

        if callbacks is None:
            raise SubjectException(f"Observers Not Found for {graph}")

        return callbacks
