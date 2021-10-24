import unittest
from unittest import mock
from src.ufu_parser.parser_observer import ParserSubject, SubjectException, Subject
from src.ufu_parser.syntax_tree import SyntaxNode
from src.ufu_parser.syntactic_graphs.componets import *


class TestParserObserverCase(unittest.TestCase):

    def test_notification(self):
        subject: Subject = ParserSubject()
        name = 'test'
        another_name = 'test2'

        observer = mock.MagicMock()
        observer.on_next = lambda node: self.assertEqual(node.name, name)

        error_observer = mock.MagicMock()
        error_observer.on_next = lambda node: self.assertEqual(node.name, another_name)

        subject.attach(DeclaracaoDeVariavel, observer)
        subject.attach(DeclaracaoDeVariavel, observer)
        subject.on_next(DeclaracaoDeVariavel, SyntaxNode(name))

        subject.attach(DeclaracaoDeVariavel, error_observer)

        with self.assertRaises(AssertionError):
            subject.on_next(DeclaracaoDeVariavel, SyntaxNode(name))

        subject.detach(DeclaracaoDeVariavel, error_observer)

        subject.on_next(DeclaracaoDeVariavel, SyntaxNode(name))

        with self.assertRaises(ValueError):
            subject.detach(DeclaracaoDeVariavel, error_observer)

        with self.assertRaises(SubjectException):
            subject.attach(Subject, error_observer)


if __name__ == '__main__':
    unittest.main()
