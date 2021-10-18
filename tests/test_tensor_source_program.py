import unittest

from src.source_program.tensor_source_program import TensorSourceProgram, SourceProgramException


class TensorSourceProgramTest(unittest.TestCase):

    def test_to_string_tensor_source(self):
        lines = ['0', '1', '2', '3']
        source = TensorSourceProgram(lines)
        assert str(source)

        lines = ['01', '11', '21', '31']
        source = TensorSourceProgram(lines)
        assert str(source)

    def test_current_and_next_char(self):
        lines = ['0', '1', '2', '3']

        last_index = len(lines) - 1
        source = TensorSourceProgram(lines)

        for line in lines:
            char = source.current_char()
            assert char == line

            if char != lines[last_index]:
                source.next_char()

        with self.assertRaises(SourceProgramException):
            source.next_char()

        with self.assertRaises(SourceProgramException):
            source.current_char()

    def test_current_pos(self):
        lines = ['01', '11', '21', '31']
        source = TensorSourceProgram(lines)
        last_index_line = 3
        last_index_col = 1

        for i in range(len(lines)):
            for j in range(2):
                pos = source.current_pos()
                assert pos == (i , j), f"Error: pos: {pos}, i:{i} j:{j}"
                if i == last_index_line and j == last_index_col:
                    pass
                else:
                    source.next_char()

        with self.assertRaises(SourceProgramException):
            source.next_char()

        with self.assertRaises(SourceProgramException):
            source.current_pos()

    def test_to_back(self):
        lines = ['01', '11', '21', '31']
        source = TensorSourceProgram(lines)

        source.next_char()
        source.next_char()

        self.assertEqual(source.current_pos(), (1, 0))

        source.back((0, 0))

        self.assertEqual(source.current_pos(), (0, 0))

        wrongs_pos = [(-1, 0), (0, -1), (4, 2), (3, 4)]

        for pos in wrongs_pos:
            with self.assertRaises(SourceProgramException):
                source.back(pos)


if __name__ == '__main__':
    unittest.main()
