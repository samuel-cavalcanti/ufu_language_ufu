import unittest
from unittest.mock import Mock, MagicMock
from src.semantic_elaboration.scope import ScopeTree, ScopeNode
from src.symbol_tables import SymbolTable, Symbol


class ScopeTreeTestCase(unittest.TestCase):

    @staticmethod
    def __create_mock_table() -> SymbolTable:
        table: SymbolTable = Mock()
        table.dict = dict()
        table.get = table.dict.get

        def insert(s: Symbol):
            table.dict[s.name] = s

        table.insert = insert

        return table

    def test_searching_on_scope(self):
        table = self.__create_mock_table()
        symbol_type = 'type'
        symbol_id = 'id'
        value_1 = 'value 1'
        value_2 = 'value 2'

        tree = ScopeTree(table)

        tree.new_scope(self.__create_mock_table(), 'scope 1')

        tree.current_scope.table.insert(Symbol(symbol_type, symbol_id, value_1))
        tree.new_scope(self.__create_mock_table(), 'scope 1-1')

        self.assertEqual(tree.look_up(symbol_id).value, value_1)

        """Back to scope 1"""
        tree.back_scope()

        self.assertEqual(tree.look_up(symbol_id).value, value_1)
        """Back to  global scope"""
        tree.back_scope()

        self.assertEqual(tree.look_up(symbol_id), None)

        tree.new_scope(self.__create_mock_table(), 'scope 2')

        tree.current_scope.table.insert(Symbol(symbol_type, symbol_id, value_2))

        self.assertEqual(tree.look_up(symbol_id).value, value_2)

        """Back to  global scope"""
        tree.back_scope()

        self.assertEqual(tree.look_up(symbol_id), None)


if __name__ == '__main__':
    unittest.main()
