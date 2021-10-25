import os
import pathlib
import unittest
from typing import List

from src.scope_detection import ScopeDetectionPlugin, ScopeException
from src.source_program import TensorSourceProgram, SourceProgram
from src.symbol_tables import SymbolTableException
from src.ufu_parser import UfuParserBuilder
from src.ufu_scanner import UfuScanner, Scanner
from src.ufu_scanner.ad_hoc_scanner import SingleCharTokenScanCreator
from src.ufu_scanner.direct_coded_scanner import AssignmentOperatorWithColonInDirectCodedScanner
from src.ufu_scanner.direct_coded_scanner import ConstAsciiDirectCodedScanner
from src.ufu_scanner.direct_coded_scanner import ConstNumberDirectCodedScanner
from src.ufu_scanner.direct_coded_scanner import LettersWithDigitsDirectCodedScanner
from src.ufu_scanner.direct_coded_scanner import RelacionalOperatorDirectCodedScanner


class ScannerParserAndScopeDetectionTestCase(unittest.TestCase):
    def test_declaration_error(self):
        directory = pathlib.Path('tests', 'assets', 'wrong_sources', 'wrong_declaration_sources')
        symbol_table_erros_dir = directory.joinpath('symbol_table_erros')

        for wrong_file in os.listdir(symbol_table_erros_dir):
            print(f"file path: {os.path.join(symbol_table_erros_dir, wrong_file)}")

            lines = self.__load_file(symbol_table_erros_dir.joinpath(wrong_file))

            tensor_source = TensorSourceProgram(lines)

            scanner = self.__create_full_scanner(tensor_source)

            parser = UfuParserBuilder() \
                .set_scanner(scanner) \
                .add_plugin(ScopeDetectionPlugin()) \
                .build()

            with self.assertRaises(SymbolTableException):
                parser.run()

    def test_not_found_variable_error(self):
        directory = pathlib.Path('tests', 'assets', 'wrong_sources', 'wrong_declaration_sources')
        symbol_table_erros_dir = directory.joinpath('not_found_id')

        for wrong_file in os.listdir(symbol_table_erros_dir):
            print(f"file path: {os.path.join(symbol_table_erros_dir, wrong_file)}")

            lines = self.__load_file(symbol_table_erros_dir.joinpath(wrong_file))

            tensor_source = TensorSourceProgram(lines)

            scanner = self.__create_full_scanner(tensor_source)

            parser = UfuParserBuilder() \
                .set_scanner(scanner) \
                .add_plugin(ScopeDetectionPlugin()) \
                .build()

            with self.assertRaises(ScopeException):
                parser.run()

    @staticmethod
    def __load_file(file_name: pathlib.Path) -> List[str]:
        with open(file_name) as ufu_file:
            return ufu_file.readlines()

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
