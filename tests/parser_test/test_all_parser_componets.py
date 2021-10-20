import unittest

from unittest.mock import Mock, MagicMock
from src.ufu_token.ufu_token import UfuToken, UfuTokenType

from src.ufu_parser.syntactic_graphs.componets import *
from src.ufu_parser.scanner_consumer import ScannerConsumer, UfuParserException


class MockScanner:

    def __init__(self):
        self.tokens = [
            UfuToken(token_type=UfuTokenType.ID, pos=(1, 1)),
            UfuToken(token_type=UfuTokenType.ID, pos=(1, 1)),
            UfuToken(token_type=UfuTokenType.ID, pos=(1, 1), content='não é veficado'),
        ]
        self.current_token = 0

    def get_token(self) -> UfuToken:
        """Retorna o próximo token um erro caso o token não seja reconhecido"""
        token = self.tokens[self.current_token]
        self.current_token += 1

        return token


class ParserTestCase(unittest.TestCase):

    def test_software_graph(self):
        graph = Software()
        mock_scanner = MockScanner()
        consumer = ScannerConsumer(mock_scanner)

        mock_bloco = Mock()
        mock_bloco.parse = MagicMock(return_value=True)
        graph.bloco = mock_bloco

        with self.assertRaises(UfuParserException):
            graph.parse(consumer)

        mock_scanner.current_token = 0
        mock_scanner.tokens[0] = UfuToken(token_type=UfuTokenType.PROGRAMA, pos=(1, 1))
        consumer = ScannerConsumer(mock_scanner)
        graph.parse(consumer)
