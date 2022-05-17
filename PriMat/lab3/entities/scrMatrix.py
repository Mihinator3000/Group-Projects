import lab3.entities.squareMatrix as squareMatrix


class SCRMatrix:
    def __init__(self, data: [] = None, ind: [] = None, ind_ptr: [] = None):
        self.data = data if data is not None else []
        self.ind = ind if ind is not None else []
        self.ind_ptr = ind_ptr if ind_ptr is not None else [1]

    def to_SquareMatrix(self):
        matrix = squareMatrix.SquareMatrix.of_size(len(self.ind_ptr) - 1)
        iterator = 0

        for i in range(1, len(self.ind_ptr)):
            count = self.ind_ptr[i] - self.ind_ptr[i - 1]
            for _ in range(count):
                matrix[i - 1][self.ind[iterator]] = self.data[iterator]
                iterator += 1

        return matrix

    def get(self, a: int, b: int):
        row_beginning = self.ind_ptr[a] - 1
        row_end = self.ind_ptr[a + 1] - 1
        row_indexes = self.ind[row_beginning: row_end]

        return self.data[row_beginning + row_indexes.index(b)] if b in row_indexes else 0

    def print(self):
        print(self.data)
        print(self.ind)
        print(self.ind_ptr)

    @staticmethod
    def from_SquareMatrix(matrix):
        return matrix.to_SCRMatrix()
