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

    def print(self):
        for row in self.arr:
            print(row)

    def __getitem__(self, index: int) -> []:
        return self.arr[index]

    def __mul__(self, other: 'SquareMatrix') -> 'SquareMatrix':
        n = len(self.arr)
        matrix = SquareMatrix.of_size(n)
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    matrix.arr[i][j] += self.arr[i][k] * other.arr[k][j]

        return matrix

    @staticmethod
    def of_size(n: int):
        return SquareMatrix([[0 for _ in range(n)] for _ in range(n)])

    @staticmethod
    def from_SCRMatrix(matrix):
        return matrix.to_SquareMatrix()
