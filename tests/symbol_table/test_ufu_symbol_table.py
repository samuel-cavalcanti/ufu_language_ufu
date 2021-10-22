import unittest

from src.symbol_tables import Symbol, SymbolTable, UFUSymbolTable, SymbolTableException


class UFUSymbolTableTestCase(unittest.TestCase):
    def test_ufu_symbol_table(self):
        symbol_table: SymbolTable = UFUSymbolTable()

        symbol_id = 'id123'

        symbol = Symbol('int', symbol_id, '25')

        symbol_table.insert(symbol)

        with self.assertRaises(SymbolTableException):
            symbol_table.insert(symbol)

        self.assertEqual(symbol, symbol_table.get(symbol_id))

        symbol_table.create_table()

        """Variável de mesmo nome mas em outro contexto"""
        same_id = Symbol('int', symbol_id, '5')
        symbol_table.insert(same_id)

        self.assertEqual(same_id, symbol_table.get(symbol_id))

        symbol_table.drop_table()

        self.assertEqual(symbol_table.get(symbol_id), symbol)


if __name__ == '__main__':
    unittest.main()
