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

from src.ufu_parser import UfuParser, UfuParserException


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

        wrong_files = ['tests/wrong_files/wrong_software_1.ufu', 'tests/wrong_files/wrong_software_2.ufu']

        for wrong_file in wrong_files:
            lines = self.__load_file(wrong_file)

            tensor_source = TensorSourceProgram(lines)

            scanner = self.__create_full_scanner(tensor_source)

            parser = UfuParser(scanner)

            with self.assertRaises(UfuParserException):
                while True:
                    parser.run()


if __name__ == '__main__':
    unittest.main()
