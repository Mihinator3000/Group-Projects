from lab3.entities.scrMatrix import SCRMatrix
from lab3.entities.squareMatrix import SquareMatrix


class InverseFromLU:
    def __init__(self, L: SCRMatrix, U: SCRMatrix):
        (self.L, self.U) = (L, U)

    def calculate(self) -> SquareMatrix:
        n = self.L.get_n()

        #for i in range(n):

