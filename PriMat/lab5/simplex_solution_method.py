import numpy as np

from enum import Enum


class SolutionAim(Enum):
    MIN = "min"
    MAX = "max"


class SimplexSolutionMethod:
    def __init__(self,
                 solution_aim: SolutionAim,
                 func_vector: np.array,
                 b: np.array,
                 vectors: np.array,
                 basis: np.array,
                 basis_content: np.array):

        self.solution_aim = solution_aim
        self.func_vector = func_vector
        self.b = b
        self.vectors = vectors
        self.basis = basis
        self.basis_content = basis_content

    def __find_permissive_line(self, permissive_column: int) -> int:
        permissive_line = -1
        min_value = np.inf

        for index, value in enumerate(self.vectors[permissive_column]):
            if value <= 0:
                continue

            divided_value = self.b[index] / value
            if divided_value < min_value:
                min_value = divided_value
                permissive_line = index

        return permissive_line

    def __find_permissive_element(self, a_j: np.array) -> (int, int, int):
        permissive_line = -1
        permissive_column = -1

        permissive_lines = np.where(self.b < 0)[0]
        if permissive_lines.size != 0:
            permissive_line = permissive_lines[0]
            permissive_column = np.where(self.vectors[:, permissive_line] != 0)[0][0]
            return permissive_column, permissive_line, self.vectors[permissive_column][permissive_line]

        match self.solution_aim:
            case SolutionAim.MIN:
                permissive_column = int(np.argmax(a_j))
            case SolutionAim.MAX:
                permissive_column = int(np.argmin(a_j))
            case _:
                raise ValueError("Unknown solution aim")

        permissive_line = self.__find_permissive_line(permissive_column)
        return permissive_column, permissive_line, self.vectors[permissive_column][permissive_line]

    def __make_answer(self, result: float, new_basis_content: np.array) -> (float, np.array):
        non_zero_indexes = np.isin(new_basis_content, self.basis_content, invert=True)
        answer = np.zeros(self.func_vector.size - self.basis.size)
        for index, value in enumerate(non_zero_indexes):
            if value:
                answer[new_basis_content[index]] = self.b[index]

        return result, answer

    def solve(self, val: float) -> (np.array, float):
        new_basis_content = np.copy(self.basis_content)

        b_j = np.dot(self.basis, self.b)
        a_j = np.array([])
        for index, vector in enumerate(self.vectors):
            a_j = np.append(a_j, np.dot(self.basis, vector) - self.func_vector[index])

        while (self.solution_aim == SolutionAim.MIN) == np.any(a_j > 0):
            permissive_column, permissive_line, permissive_element = self.__find_permissive_element(a_j)

            new_basis_content[permissive_line] = permissive_column
            self.basis[permissive_line] = self.func_vector[permissive_column]

            new_b = np.full(self.b.shape, np.inf)
            new_b[permissive_line] = self.b[permissive_line] / permissive_element
            for index, value in enumerate(new_b):
                if value != np.inf:
                    continue

                subtrahend = (self.b[permissive_line] * self.vectors[permissive_column, index]) / permissive_element
                new_b[index] = self.b[index] - subtrahend

            new_vectors = np.full(self.vectors.shape, np.inf)
            for index, value in enumerate(self.vectors[:, permissive_line]):
                new_vectors[index, permissive_line] = value / permissive_element

            for index, line_number in enumerate(new_basis_content):
                new_vectors[line_number, :] = 0
                new_vectors[line_number, index] = 1

            for index_cl, line in enumerate(new_vectors):
                for index_ln, value in enumerate(line):
                    if value != np.inf:
                        continue

                    multiplier = self.vectors[permissive_column, index_ln] * self.vectors[index_cl, permissive_line]
                    subtrahend = multiplier / permissive_element

                    new_vectors[index_cl, index_ln] = self.vectors[index_cl, index_ln] - subtrahend

            b_j = np.dot(self.basis, new_b)
            a_j = np.array([])
            for index, vector in enumerate(new_vectors):
                a_j = np.append(a_j, np.dot(self.basis, vector) - self.func_vector[index])

            self.b = new_b
            self.vectors = new_vectors

        return self.__make_answer(b_j + val, new_basis_content)


if __name__ == '__main__':
    pass
