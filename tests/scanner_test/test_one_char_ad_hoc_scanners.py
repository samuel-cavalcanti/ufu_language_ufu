import unittest


from src.source_program.tensor_source_program import TensorSourceProgram, SourceProgramException
from src.ufu_token.ufu_token import UfuToken, UfuTokenType
from src.ufu_scanner.ad_hoc_scanner.one_char_ad_hoc_scanner import OneCharAdHocScanner, OneCharScannerException
from src.ufu_scanner.ufu_scanner import UfuScanner, ScannerException
from src.ufu_scanner.single_char_token_scan_creator import SingleCharTokenScanCreator

class OneCharAdHocScannersTest(unittest.TestCase):

    def test_fail_init(self):
        with self.assertRaises(OneCharScannerException):
            OneCharAdHocScanner(char='12', token_type=UfuTokenType.CONST_INT)

    def test_dot_comma_colon_scan(self):
        lines = [': sa,das :=.;']
        """
            Esse teste mostra o porque não pode ser utilizado OneCharScanner
            para recuperar o Token :
            pois OneCharScanner é o ad hoc, com a limitação de não poder chamar o próximo char
        """
        assert ':' == lines[0][0]
        assert ',' == lines[0][4]
        assert ':' == lines[0][9]
        assert ';' == lines[0][12]

        for_limit = 12 + 10

        expected_tokens = [
            UfuToken(token_type=UfuTokenType.COLON, pos=(0, 0)),
            UfuToken(token_type=UfuTokenType.COMMA, pos=(0, 4)),
            UfuToken(token_type=UfuTokenType.ASSIGNMENT_OPERATOR, pos=(0, 9)),
            UfuToken(token_type=UfuTokenType.SEMICOLON, pos=(0, 12)),
        ]

        scanners = [
            OneCharAdHocScanner(char=':', token_type=UfuTokenType.COLON),
            SingleCharTokenScanCreator().create_token_scan(UfuTokenType.COMMA),
            SingleCharTokenScanCreator().create_token_scan(UfuTokenType.SEMICOLON),
        ]

        source = TensorSourceProgram(lines)
        ufu_scanner = UfuScanner(token_scanners=scanners, source=source)
        tokens = self.__run_scanner(ufu_scanner, it_limit=for_limit)

        self.assertNotEqual(tokens, expected_tokens)

    def test_brackets_scan(self):
        lines = ['{ a:int;b:ascii;}']
        last_index = len(lines[0]) - 1
        assert '{' == lines[0][0]
        assert '}' == lines[0][last_index]

        expected_tokens = [UfuToken(token_type=UfuTokenType.OPEN_BRACKETS, pos=(0, 0)),
                           UfuToken(token_type=UfuTokenType.CLOSE_BRACKETS, pos=(0, last_index))]

        for_limit = len(lines[0]) + 10
        source = TensorSourceProgram(lines)

        scanners = [
            SingleCharTokenScanCreator().create_token_scan(UfuTokenType.OPEN_BRACKETS),
            SingleCharTokenScanCreator().create_token_scan(UfuTokenType.CLOSE_BRACKETS),
        ]
        ufu_scanner = UfuScanner(token_scanners=scanners, source=source)

        tokens = self.__run_scanner(scanner=ufu_scanner, it_limit=for_limit)

        self.assertEqual(tokens, expected_tokens)

    def test_parentheses_scan(self):
        lines = [') a = b', '0) a = (b)']
        assert ')' == lines[0][0]
        assert ')' == lines[1][1]
        assert '(' == lines[1][7]
        assert ')' == lines[1][9]
        expected_tokens = [
            UfuToken(UfuTokenType.CLOSE_PARENTHESES, pos=(0, 0)),
            UfuToken(UfuTokenType.CLOSE_PARENTHESES, pos=(1, 1)),
            UfuToken(UfuTokenType.OPEN_PARENTHESES, pos=(1, 7)),
            UfuToken(UfuTokenType.CLOSE_PARENTHESES, pos=(1, 9)),
        ]
        tensor_source = TensorSourceProgram(lines=lines)

        token_scanners = [
            SingleCharTokenScanCreator().create_token_scan(UfuTokenType.OPEN_PARENTHESES),
            SingleCharTokenScanCreator().create_token_scan(UfuTokenType.CLOSE_PARENTHESES),
        ]

        ufu_scanner = UfuScanner(token_scanners=token_scanners, source=tensor_source)

        for_limit = len(lines[0]) + len(lines[1]) + 10
        result_tokens = self.__run_scanner(ufu_scanner, it_limit=for_limit)

        self.assertEqual(len(result_tokens), len(expected_tokens))

        self.assertEqual(result_tokens, expected_tokens)

    @staticmethod
    def __run_scanner(scanner: UfuScanner, it_limit: int):
        results_tokens = []

        for _ in range(it_limit):
            try:
                token = scanner.get_token()
                results_tokens.append(token)
            except SourceProgramException:
                """occurs when source is End of File"""
                break
            except ScannerException:
                """occurs when scanner is capable to recognize the symbol"""

        return results_tokens

    def test_arithmetic_operation_scan(self):
        line = ['a+b-c*d/e']
        assert '+' == line[0][1]
        assert '-' == line[0][3]
        assert '*' == line[0][5]
        assert '/' == line[0][7]

        source = TensorSourceProgram(line)
        expected_tokens = [
            UfuToken(token_type=UfuTokenType.ADD, pos=(0, 1)),
            UfuToken(token_type=UfuTokenType.SUB, pos=(0, 3)),
            UfuToken(token_type=UfuTokenType.MUL, pos=(0, 5)),
            UfuToken(token_type=UfuTokenType.DIV, pos=(0, 7)),
        ]
        scanners = [
            SingleCharTokenScanCreator().create_token_scan(UfuTokenType.ADD),
            SingleCharTokenScanCreator().create_token_scan(UfuTokenType.SUB),
            SingleCharTokenScanCreator().create_token_scan(UfuTokenType.MUL),
            SingleCharTokenScanCreator().create_token_scan(UfuTokenType.DIV),
        ]
        ufu_scanner = UfuScanner(token_scanners=scanners, source=source)

        results_tokens = self.__run_scanner(scanner=ufu_scanner, it_limit=len(line[0]) + 10)

        self.assertEqual(results_tokens, expected_tokens)

        if __name__ == '__main__':
            unittest.main()
