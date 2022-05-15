import lab3.entities.scrMatrix as scrMatrix


class SquareMatrix:
    def __init__(self, arr: [[]]):
        self.arr = arr

    def to_SCRMatrix(self):
        data = []
        ind = []
        ind_ptr = [1]

        for row in self.arr:
            count_not_zero = 0
            for i in range(len(row)):
                if row[i] == 0:
                    continue

                data.append(row[i])
                ind.append(i)
                count_not_zero += 1
            ind_ptr.append(ind_ptr[-1] + count_not_zero)

        return scrMatrix.SCRMatrix(data, ind, ind_ptr)

    def __getitem__(self, index: int) -> []:
        return self.arr[index]

    @staticmethod
    def of_size(n: int):
        return SquareMatrix([[0 for _ in range(n)] for _ in range(n)])

    @staticmethod
    def from_SCRMatrix(matrix):
        return matrix.to_SquareMatrix()
