from typing import Tuple, List
from .source_program import SourceProgramException

import numpy as np


class TensorSourceProgram:
    __tensor: np.ndarray
    __current_row: int
    __current_col: int

    def __init__(self, lines: list[str]):
        char_matrix = []
        for line in lines:
            char_array = [char for char in line]
            char_matrix.append(np.array(char_array, dtype=object))

        self.__tensor = np.array(char_matrix, dtype=object)

        self.__current_col = 0
        self.__current_row = 0

    def current_char(self) -> str:
        if self.__current_row == -1:
            raise SourceProgramException('End file')

        return self.__tensor[self.__current_row][self.__current_col]

    def next_char(self):
        self.__current_col += 1
        if self.__current_col >= len(self.__tensor[self.__current_row]):
            self.__current_col = 0
            self.__current_row += 1
            if self.__current_row >= len(self.__tensor):
                self.__current_col = -1
                self.__current_row = -1
                raise SourceProgramException('End file')

    def __str__(self):
        s = f'shape: {self.__tensor.shape}\n'
        for row in self.__tensor:
            s += f'{row}\n'
        return s

    def current_pos(self) -> Tuple[int, int]:
        if self.__current_row == -1 or self.__current_col == -1:
            raise SourceProgramException('end file')

        return self.__current_row, self.__current_col

    def back(self, pos: Tuple[int, int]):
        row, col = pos
        if row < 0 or col < 0 or row >= len(self.__tensor):
            raise SourceProgramException(f'unable to return to pos: {pos}')

        if col >= len(self.__tensor[row]):
            raise SourceProgramException(f'unable to return to pos: {pos}')

        self.__current_row = row
        self.__current_col = col
