import unittest

from src.ufu_scanner.direct_coded_scanner.assignment_operator_with_colon_direct_coded_scanner import \
    AssignmentOperatorWithColonInDirectCodedScanner
from src.ufu_scanner import UfuScanner, ScannerException
from src.source_program import TensorSourceProgram, SourceProgramException
from src.ufu_scanner.direct_coded_scanner.letters_with_digitis_direct_coded_scanner import \
    LettersWithDigitsDirectCodedScanner
from src.ufu_scanner.direct_coded_scanner.relational_operator_direct_coded_scanner import \
    RelacionalOperatorDirectCodedScanner
from src.ufu_scanner.direct_coded_scanner.const_ascii_direct_coded_scanner import ConstAsciiDirectCodedScanner
from src.ufu_token import UfuToken, UfuTokenType
from src.ufu_scanner.direct_coded_scanner.const_number_direct_coded_scanner import ConstNumberDirectCodedScanner


class DirectCodedScannersTest(unittest.TestCase):
    def test_assignment_operator_scanner(self):
        lines = ['a:int;', 'a := 2']
        assert ':' == lines[0][1]
        assert ':' == lines[1][2]
        expected_tokens = [UfuToken(token_type=UfuTokenType.COLON, pos=(0, 1)),
                           UfuToken(token_type=UfuTokenType.ASSIGNMENT_OPERATOR, pos=(1, 2))]
        scanners = [AssignmentOperatorWithColonInDirectCodedScanner()]

        source = TensorSourceProgram(lines)

        ufu_scanner = UfuScanner(token_scanners=scanners, source=source)

        for_limit = 20
        result = self.__run_scanner(ufu_scanner, it_limit=for_limit)

        self.assertEqual(result, expected_tokens)

    def test_relational_operator_scanner(self):
        lines = ['(a <> b)', '(a > b)', '(a < b)',
                 '(a >= b)', '(a <= b)', '(a == b)']
        lines += ['(a != b)', '(a = b)']
        assert '<>' == lines[0][3:5]
        assert '>' == lines[1][3]
        assert '<' == lines[2][3]
        assert '>=' == lines[3][3:5]
        assert '<=' == lines[4][3:5]
        assert '==' == lines[5][3:5]

        limit = len(lines) * len(lines[0]) + 10

        expected_tokens = [
            UfuToken(token_type=UfuTokenType.RELATIONAL_OPERATOR,
                     pos=(0, 3), content='<>'),
            UfuToken(token_type=UfuTokenType.RELATIONAL_OPERATOR,
                     pos=(1, 3), content='>'),
            UfuToken(token_type=UfuTokenType.RELATIONAL_OPERATOR,
                     pos=(2, 3), content='<'),
            UfuToken(token_type=UfuTokenType.RELATIONAL_OPERATOR,
                     pos=(3, 3), content='>='),
            UfuToken(token_type=UfuTokenType.RELATIONAL_OPERATOR,
                     pos=(4, 3), content='<='),
            UfuToken(token_type=UfuTokenType.RELATIONAL_OPERATOR,
                     pos=(5, 3), content='=='),
        ]

        source = TensorSourceProgram(lines)
        scanners = [RelacionalOperatorDirectCodedScanner()]
        ufu_scanner = UfuScanner(token_scanners=scanners, source=source)
        results = self.__run_scanner(ufu_scanner, it_limit=limit)

        self.assertEqual(results, expected_tokens)

    def test_letters_with_digits_scanner(self):
        lines = ['int:a,b,c;', 'ascii:c;',
                 'real:numero10,numero11;', 'if (a == b) then {} else{}']
        assert 'int' == lines[0][0:3]
        assert 'a' == lines[0][4]
        assert 'b' == lines[0][6]
        assert 'c' == lines[0][8]

        assert 'ascii' == lines[1][0:5]
        assert 'c' == lines[1][6]

        assert 'real' == lines[2][0:4]
        assert 'numero10' == lines[2][5:13]
        assert 'numero11' == lines[2][14:22]

        assert 'if' == lines[3][0:2]
        assert 'a' == lines[3][4]
        assert 'b' == lines[3][9]
        assert 'then' == lines[3][12:16]
        assert 'else' == lines[3][20:24]

        limit = len(lines) * len(lines[-1]) + 10

        expected_tokens = [
            UfuToken(token_type=UfuTokenType.TYPE_VARIABLE,
                     pos=(0, 0), content='int'),
            UfuToken(token_type=UfuTokenType.ID,
                     pos=(0, 4), content='a'),
            UfuToken(token_type=UfuTokenType.ID,
                     pos=(0, 6), content='b'),
            UfuToken(token_type=UfuTokenType.ID,
                     pos=(0, 8), content='c'),

            UfuToken(token_type=UfuTokenType.TYPE_VARIABLE,
                     pos=(1, 0), content='ascii'),
            UfuToken(token_type=UfuTokenType.ID,
                     pos=(1, 6), content='c'),

            UfuToken(token_type=UfuTokenType.TYPE_VARIABLE,
                     pos=(2, 0), content='real'),
            UfuToken(token_type=UfuTokenType.ID,
                     pos=(2, 5), content='numero10'),
            UfuToken(token_type=UfuTokenType.ID,
                     pos=(2, 14), content='numero11'),

            UfuToken(token_type=UfuTokenType.IF, pos=(3, 0)),
            UfuToken(token_type=UfuTokenType.ID,
                     pos=(3, 4), content='a'),
            UfuToken(token_type=UfuTokenType.ID,
                     pos=(3, 9), content='b'),
            UfuToken(token_type=UfuTokenType.THEN, pos=(3, 12)),
            UfuToken(token_type=UfuTokenType.ELSE, pos=(3, 20)),

        ]

        source = TensorSourceProgram(lines)
        scanners = [LettersWithDigitsDirectCodedScanner()]

        ufu_scanner = UfuScanner(token_scanners=scanners, source=source)
        results = self.__run_scanner(ufu_scanner, it_limit=limit)

        self.assertEqual(results, expected_tokens)

    def test_const_number_scanner(self):
        numbers = ['+12', '-12', '+12.4', '-12.4', '3.1415', '3e+15', '-3e-15', '1e+', '2e-', '1e1']

        lines = [f'a :={number};' for number in numbers]

        assert '+12' == lines[0][4:-1]

        start_column = 4
        start_row = 0

        limit = len(lines) * len(lines[-1]) + 10

        expected_tokens = [
            UfuToken(token_type=UfuTokenType.CONST_INT, pos=(start_row, start_column), content=numbers[0]),
            UfuToken(token_type=UfuTokenType.CONST_INT, pos=(start_row + 1, start_column), content=numbers[1]),
            UfuToken(token_type=UfuTokenType.CONST_REAL, pos=(start_row + 2, start_column), content=numbers[2]),
            UfuToken(token_type=UfuTokenType.CONST_REAL, pos=(start_row + 3, start_column), content=numbers[3]),
            UfuToken(token_type=UfuTokenType.CONST_REAL, pos=(start_row + 4, start_column), content=numbers[4]),
            UfuToken(token_type=UfuTokenType.CONST_REAL, pos=(start_row + 5, start_column), content=numbers[5]),
            UfuToken(token_type=UfuTokenType.CONST_REAL, pos=(start_row + 6, start_column), content=numbers[6]),
            UfuToken(token_type=UfuTokenType.CONST_REAL, pos=(len(numbers) - 1, start_column), content=numbers[-1]),
        ]

        source = TensorSourceProgram(lines)
        scanners = [ConstNumberDirectCodedScanner()]

        ufu_scanner = UfuScanner(token_scanners=scanners, source=source)

        results = self.__run_scanner(ufu_scanner, it_limit=limit)

        self.assertEqual(results, expected_tokens)

    def test_const_ascii_scanner(self):
        chars = ['oi', 'tudo bem ?', 'tudo !', 'que bom :)']
        lines = [f"c := '{char}'" for char in chars]

        start_index = 5
        final_index = start_index + len(chars[0]) + 2

        assert "'oi'" == lines[0][start_index:final_index], f'lines: {lines[0][start_index:final_index]}'

        limit = len(lines) * len(lines[-1]) + 10

        expected_tokens = [UfuToken(token_type=UfuTokenType.CONST_ASCII, pos=(index, start_index), content=char)
                           for index, char in enumerate(chars)]
        source = TensorSourceProgram(lines)
        scanners = [ConstAsciiDirectCodedScanner()]

        ufu_scanner = UfuScanner(token_scanners=scanners, source=source)

        results = self.__run_scanner(ufu_scanner, it_limit=limit)

        self.assertEqual(expected_tokens, results)

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
                """occurs when scanner is not capable to recognize the char"""

        return results_tokens
