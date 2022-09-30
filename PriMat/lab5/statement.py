import numpy as np

import restriction as r


class Statement:
    def __init__(self,
                 func_coefficients: np.array,
                 restrictions: list,
                 value: float = 0,
                 input_basis: np.array = None):

        self.func_coefficients = func_coefficients
        self.restrictions = restrictions
        self.value = value
        self.input_basis = input_basis

    def __str__(self):
        return f"{self.func_coefficients} {self.restrictions} {self.value}"

    def __restrictions_count(self) -> int:
        return len(self.restrictions)

    def __equal_restrictions_count(self) -> int:
        return len([re for re in self.restrictions if re.restriction_type == r.RestrictionType.EQUAL])

    def to_canonical(self) -> None:
        for restriction in self.restrictions:
            restriction.to_canonical()

    def create_statement_vectors(self) -> (np.array, np.array, np.array):
        self.to_canonical()
        func_vector = np.concatenate((self.func_coefficients, np.zeros(self.__restrictions_count())))
        b = np.array([])
        vectors = []

        for index, restriction in enumerate(self.restrictions):
            additional_vector = np.zeros(self.__restrictions_count())
            b = np.append(b, restriction.value)
            if restriction.restriction_type == r.RestrictionType.GREATER:
                additional_vector = np.zeros(self.__restrictions_count())
                additional_vector[index] = -1
            elif restriction.restriction_type == r.RestrictionType.LESS:
                additional_vector = np.zeros(self.__restrictions_count())
                additional_vector[index] = 1

            vectors.append(np.concatenate((restriction.coefficients, additional_vector)))

        vectors = np.asarray(vectors)
        vectors_transpose = vectors.T
        return func_vector, b, vectors_transpose

    def create_basis(self) -> np.array:
        if self.input_basis is not None:
            return self.input_basis

        return np.zeros(self.__restrictions_count())

    def create_basis_content(self) -> np.array:
        return np.arange(
            self.func_coefficients.size,
            self.func_coefficients.size + self.__restrictions_count() - self.__equal_restrictions_count(),
            step=1)


if __name__ == '__main__':
    pass
