import numpy as np

from enum import Enum


class SolutionAim(Enum):
    MIN = 1
    MAX = 2


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
        min_value = np.inf
        permissive_line = -1
        for index, value in enumerate(self.vectors[permissive_column]):
            if value <= 0:
                continue

            divided_value = self.b[index] / value
            if divided_value < min_value:
                min_value = divided_value
                permissive_line = index

        return permissive_line

    def solve_min(self) -> (np.array, float):
        new_basis_content = np.copy(self.basis_content)

        b_j = np.dot(self.basis, self.b)
        a_j = np.array([])
        for index, vector in enumerate(self.vectors):
            a_j = np.append(a_j, np.dot(self.basis, vector) - self.func_vector[index])

        while np.any(a_j > 0):
            permissive_column = int(np.argmax(a_j))
            permissive_line = self.__find_permissive_line(permissive_column)
            permissive_element = self.vectors[permissive_column][permissive_line]

            new_basis_content[permissive_line] = permissive_column
            self.basis[permissive_line] = self.func_vector[permissive_column]

            new_b = np.full(self.b.shape, np.inf)
            new_b[permissive_line] = self.b[permissive_line] / permissive_element

            new_vectors = np.full(self.vectors.shape, np.inf)
            for index, value in enumerate(self.vectors[:, permissive_line]):
                new_vectors[index, permissive_line] = value / permissive_element

            for index, line_number in enumerate(new_basis_content):
                new_vectors[line_number, :] = 0
                new_vectors[line_number, index] = 1

            for index, value in enumerate(new_b):
                if value != np.inf:
                    continue

                subtrahend = (self.b[permissive_line] * self.vectors[permissive_column, index]) / permissive_element
                new_b[index] = self.b[index] - subtrahend

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

        non_zero_indexes = np.setdiff1d(new_basis_content, self.basis_content)
        answer = np.zeros(self.func_vector.size - self.basis.size)
        answer[non_zero_indexes] = self.b[non_zero_indexes]
        return b_j, answer

    def solve_max(self) -> (np.array, float):
        new_basis_content = np.copy(self.basis_content)

        b_j = np.dot(self.basis, self.b)
        a_j = np.array([])
        for index, vector in enumerate(self.vectors):
            a_j = np.append(a_j, np.dot(self.basis, vector) - self.func_vector[index])

        # Difference between min and max is only in these 2 lines, but im too lazy to make to separate it :)
        while np.any(a_j < 0):
            permissive_column = int(np.argmin(a_j))
        # TODO: remove code duplication
            permissive_line = self.__find_permissive_line(permissive_column)
            permissive_element = self.vectors[permissive_column][permissive_line]

            new_basis_content[permissive_line] = permissive_column
            self.basis[permissive_line] = self.func_vector[permissive_column]

            new_b = np.full(self.b.shape, np.inf)
            new_b[permissive_line] = self.b[permissive_line] / permissive_element

            new_vectors = np.full(self.vectors.shape, np.inf)
            for index, value in enumerate(self.vectors[:, permissive_line]):
                new_vectors[index, permissive_line] = value / permissive_element

            for index, line_number in enumerate(new_basis_content):
                new_vectors[line_number, :] = 0
                new_vectors[line_number, index] = 1

            for index, value in enumerate(new_b):
                if value != np.inf:
                    continue

                subtrahend = (self.b[permissive_line] * self.vectors[permissive_column, index]) / permissive_element
                new_b[index] = self.b[index] - subtrahend

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

        non_zero_indexes = np.setdiff1d(new_basis_content, self.basis_content)
        answer = np.zeros(self.func_vector.size - self.basis.size)
        answer[non_zero_indexes] = self.b[non_zero_indexes]
        return b_j, answer

    def solve(self) -> (np.array, float):
        if self.solution_aim == SolutionAim.MIN:
            return self.solve_min()

        return self.solve_max()


if __name__ == '__main__':
    pass
