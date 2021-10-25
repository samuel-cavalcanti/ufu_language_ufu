from .ufu_parser import UfuParser
from .ufu_parser_plugin import UfuParserPlugin
from src.ufu_scanner import Scanner
from src.ufu_parser.parser_observer import Observer


class UfuParserBuilder:
    __scanner: Scanner
    __plugins: list[UfuParserPlugin]
    __observers: list[tuple[type, Observer]]

    def __init__(self):
        self.__plugins = list()
        self.__observers = list()

    def set_scanner(self, scanner: Scanner):
        self.__scanner = scanner
        return self

    def add_plugin(self, plugin: UfuParserPlugin):
        self.__plugins.append(plugin)
        return self

    def add_observer(self, graph: type, observer: Observer):
        self.__observers.append((graph, observer))
        return self

    def build(self) -> UfuParser:
        parser = UfuParser(self.__scanner)

        for plugin in self.__plugins:
            plugin.build(parser)

        for graph, observer in self.__observers:
            parser.register_observer(graph, observer)

        return parser
