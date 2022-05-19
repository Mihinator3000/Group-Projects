from lab3.algorithms.systemSolver import SystemSolver
from lab3.entities.scrMatrix import SCRMatrix
from lab3.entities.squareMatrix import SquareMatrix


class InverseFromLU:
    def __init__(self, a: SCRMatrix):
        self.a = a
        self.n = a.get_n()

    def calculate(self) -> SCRMatrix:
        matrix = []
        for i in range(self.n):
            column = [0 for _ in range(self.n)]
            column[i] = 1
            matrix.append(SystemSolver(self.a, column).solve())

        return SquareMatrix(matrix).transpose().to_SCRMatrix()


