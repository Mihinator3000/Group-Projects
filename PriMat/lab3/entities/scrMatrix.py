import lab3.entities.squareMatrix as squareMatrix


class SCRMatrix:
    def __init__(self, data: [], ind: [], ind_ptr: []):
        self.data = data
        self.ind = ind
        self.ind_ptr = ind_ptr

    def to_SquareMatrix(self):
        matrix = squareMatrix.SquareMatrix.of_size(len(self.ind_ptr) - 1)
        iterator = 0

        for i in range(1, len(self.ind_ptr)):
            count = self.ind_ptr[i] - self.ind_ptr[i - 1]
            for _ in range(count):
                matrix[i - 1][self.ind[iterator]] = self.data[iterator]
                iterator += 1

        return matrix

    @staticmethod
    def from_SquareMatrix(matrix):
        return matrix.to_SCRMatrix()
