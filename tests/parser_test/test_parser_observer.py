import unittest

from src.ufu_parser.parser_observer import ParserSubject, SubjectException, Subject
from src.ufu_parser.syntax_tree import SyntaxNode
from src.ufu_parser.syntactic_graphs.componets import *


class TestParserObserverCase(unittest.TestCase):

    def test_notification(self):
        subject: Subject = ParserSubject()
        name = 'test'
        another_name = 'test2'

        notification = lambda node: self.assertEqual(node.name, another_name)

        subject.attach(DeclaracaoDeVariavel, lambda node: self.assertEqual(node.name, name))
        subject.attach(DeclaracaoDeVariavel, lambda node: self.assertNotEqual(node.name, another_name))
        subject.on_next(DeclaracaoDeVariavel, SyntaxNode(name))

        subject.attach(DeclaracaoDeVariavel, notification)

        with self.assertRaises(AssertionError):
            subject.on_next(DeclaracaoDeVariavel, SyntaxNode(name))

        subject.detach(DeclaracaoDeVariavel, notification)

        subject.on_next(DeclaracaoDeVariavel, SyntaxNode(name))

        with self.assertRaises(ValueError):
            subject.detach(DeclaracaoDeVariavel, notification)

        with self.assertRaises(SubjectException):
            subject.attach(Subject, notification)


if __name__ == '__main__':
    unittest.main()
