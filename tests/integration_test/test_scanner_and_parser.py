import unittest
from typing import List

from src.source_program import TensorSourceProgram, SourceProgram
from src.ufu_scanner import UfuScanner, Scanner
from src.ufu_scanner.ad_hoc_scanner import SingleCharTokenScanCreator
from src.ufu_scanner.direct_coded_scanner import LettersWithDigitsDirectCodedScanner
from src.ufu_scanner.direct_coded_scanner import RelacionalOperatorDirectCodedScanner
from src.ufu_scanner.direct_coded_scanner import ConstNumberDirectCodedScanner
from src.ufu_scanner.direct_coded_scanner import ConstAsciiDirectCodedScanner
from src.ufu_scanner.direct_coded_scanner import AssignmentOperatorWithColonInDirectCodedScanner
from src.ufu_parser import UfuParser, UfuParserException, UfuParserBuilder
from src.ufu_parser.syntactic_graphs.componets import *
from src.ufu_parser.syntax_tree import SyntaxNode
from src.scope_detection import ScopeDetectionPlugin
from src.tree_graphviz_visualizer import TreeGraphvizVisualizer
import os
import pathlib


class FullTestCase(unittest.TestCase):

    @staticmethod
    def __load_file(file_name: str) -> List[str]:
        with open(file_name) as ufu_file:
            return ufu_file.readlines()

    @staticmethod
    def __generate_graphviz_file(root: SyntaxNode, output_file_path: pathlib.Path):
        with open(output_file_path, 'w') as file:
            content_file = TreeGraphvizVisualizer().generate_graphviz_file(root)
            file.write(content_file)

    @staticmethod
    def __create_full_scanner(source: SourceProgram) -> Scanner:
        ad_hoc_scanners = SingleCharTokenScanCreator().create_all_token_scans()
        direct_coded_scanners = [
            AssignmentOperatorWithColonInDirectCodedScanner(),
            LettersWithDigitsDirectCodedScanner(),
            RelacionalOperatorDirectCodedScanner(),
            ConstNumberDirectCodedScanner(),
            ConstAsciiDirectCodedScanner()
        ]

        return UfuScanner(token_scanners=ad_hoc_scanners + direct_coded_scanners, source=source)

    def test_wrong_file(self):
        directory = 'tests/assets/wrong_sources'
        for wrong_file in os.listdir(directory):
            print(f"file path: {os.path.join(directory, wrong_file)}")

            lines = self.__load_file(os.path.join(directory, wrong_file))

            tensor_source = TensorSourceProgram(lines)

            scanner = self.__create_full_scanner(tensor_source)

            parser = UfuParserBuilder() \
                .set_scanner(scanner) \
                .add_plugin(ScopeDetectionPlugin()) \
                .build()

            with self.assertRaises(UfuParserException):
                parser.run()

    def test_correct_source(self):
        directory = pathlib.Path('tests', 'assets', 'correct_sources')  # 'tests/assets/correct_sources'
        path_dir = pathlib.Path('tests', 'assets', 'dot_files')

        for correct_file in os.listdir(directory):
            print(f"file path: {os.path.join(directory, correct_file)}")

            lines = self.__load_file(os.path.join(directory, correct_file))

            tensor_source = TensorSourceProgram(lines)

            scanner = self.__create_full_scanner(tensor_source)
            scope_plugin = ScopeDetectionPlugin()
            parser = UfuParserBuilder() \
                .set_scanner(scanner) \
                .add_plugin(scope_plugin) \
                .build()

            tree = parser.run()

            self.__create_dir_if_not_exist(path_dir)
            self.__generate_graphviz_file(tree.root, path_dir.joinpath(f'correct_sources_{correct_file}.dot'))
            self.__generate_graphviz_file(scope_plugin.scope_detection.scope_tree.root,
                                          path_dir.joinpath(f'scope_tree_{correct_file}.dot'))

    @staticmethod
    def __create_dir_if_not_exist(path: pathlib.Path):

        if path.is_dir():
            return

        path.mkdir()
