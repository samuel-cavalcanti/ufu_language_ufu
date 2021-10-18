import unittest
from typing import List

from src.source_program import TensorSourceProgram, SourceProgram
from src.source_program.source_program import SourceProgramException
from src.ufu_scanner import UfuScanner, Scanner
from src.ufu_scanner.ad_hoc_scanner import SingleCharTokenScanCreator
from src.ufu_scanner.direct_coded_scanner import LettersWithDigitsDirectCodedScanner
from src.ufu_scanner.direct_coded_scanner import RelacionalOperatorDirectCodedScanner
from src.ufu_scanner.direct_coded_scanner import ConstNumberDirectCodedScanner
from src.ufu_scanner.direct_coded_scanner import ConstAsciiDirectCodedScanner
from src.ufu_scanner.direct_coded_scanner import AssignmentOperatorWithColonInDirectCodedScanner
from src.ufu_parser import UfuParser, UfuParserException

import os


class FullTestCase(unittest.TestCase):

    @staticmethod
    def __load_file(file_name: str) -> List[str]:
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

    def test_wrong_file(self):
        directory = 'tests/wrong_sources'
        for wrong_file in os.listdir(directory):
            print(f"file path: {os.path.join(directory, wrong_file)}")

            lines = self.__load_file(os.path.join(directory, wrong_file))

            tensor_source = TensorSourceProgram(lines)

            scanner = self.__create_full_scanner(tensor_source)

            parser = UfuParser(scanner)

            with self.assertRaises(UfuParserException):
                parser.run()

        
    def test_correct_source(self):
        directory = 'tests/correct_sources'
        for correct_file in os.listdir(directory):
            print(f"file path: {os.path.join(directory, correct_file)}")

            lines = self.__load_file(os.path.join(directory, correct_file))

            tensor_source = TensorSourceProgram(lines)

            scanner = self.__create_full_scanner(tensor_source)

            parser = UfuParser(scanner)

            try:
                parser.run()
            except SourceProgramException as error:
                """ esse erro deve ocorrer com o fim do arquivo """
                print(error)
               
              


if __name__ == '__main__':
    unittest.main()
