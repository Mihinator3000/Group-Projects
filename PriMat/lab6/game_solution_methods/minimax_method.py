import numpy as np


class MinimaxMethod:
    def __init__(self, matrix: np.array):
        self.__matrix = matrix
        self.solution = None

    def solve(self) -> None:
        max_min_rows = np.max(np.min(self.__matrix, axis=1))
        min_max_columns = np.min(np.max(self.__matrix, axis=0))
        self.solution = np.array([max_min_rows, min_max_columns])

    def has_saddle_point(self) -> bool:
        return self.solution[0] == self.solution[1]
