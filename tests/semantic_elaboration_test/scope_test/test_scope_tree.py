import pathlib
import unittest
from unittest.mock import Mock, MagicMock
from src.semantic_elaboration.scope_tree import ScopeTree, ScopeNode
from src.symbol_tables import SymbolTable, Symbol
from src.tree_graphviz_visualizer import TreeGraphvizVisualizer


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

    @staticmethod
    def __generate_graphviz_file(root: ScopeNode, output_file_path: pathlib.Path):
        with open(output_file_path, 'w') as file:
            content_file = TreeGraphvizVisualizer().generate_graphviz_file(root)
            file.write(content_file)

    def test_searching_on_scope(self):
        table = self.__create_mock_table()
        symbol_type = 'type'
        symbol_id = 'id'
        value_1 = 'value 1'
        value_2 = 'value 2'

        tree = ScopeTree(table)

        self.assertEqual(tree.current_scope.level, 0)

        tree.new_scope(self.__create_mock_table(), 'scope_tree 1')

        self.assertEqual(tree.current_scope.level, 1)

        tree.current_scope.table.insert(Symbol(symbol_type, symbol_id, value_1))
        tree.new_scope(self.__create_mock_table(), 'scope_tree 1-1')

        self.assertEqual(tree.current_scope.level, 2)

        self.assertEqual(tree.look_up(symbol_id).value, value_1)

        """Back to scope_tree 1"""
        tree.back_scope()
        self.assertEqual(tree.current_scope.level, 1)

        self.assertEqual(tree.look_up(symbol_id).value, value_1)
        """Back to  global scope_tree"""
        tree.back_scope()
        self.assertEqual(tree.current_scope.level, 0)

        self.assertEqual(tree.look_up(symbol_id), None)

        tree.new_scope(self.__create_mock_table(), 'scope_tree 2')

        tree.current_scope.table.insert(Symbol(symbol_type, symbol_id, value_2))

        self.assertEqual(tree.look_up(symbol_id).value, value_2)

        """Back to  global scope_tree"""
        tree.back_scope()

        self.assertEqual(tree.look_up(symbol_id), None)
        path_dir = pathlib.Path('tests', 'assets', 'dot_files')
        self.__generate_graphviz_file(tree.root, path_dir.joinpath('test_scope.dot'))
