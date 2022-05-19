import lab3.entities.squareMatrix as squareMatrix
from lab3.algorithms.inverseFromLU import InverseFromLU
from lab3.algorithms.luDecomposition import LUDecomposition
from lab3.algorithms.systemSolver import SystemSolver

if __name__ == "__main__":
    matrix = squareMatrix.SquareMatrix([
        [1, 0, 5, 0, 3],
        [4, 5, 0, 9, 2],
        [1, 0, 7, 2, 0],
        [0, 0, 3, 4, 0],
        [3, 4, 0, 2, 9]
    ])

    scr_matrix = matrix.to_SCRMatrix()
    scr_matrix.print()

    square_matrix = scr_matrix.to_SquareMatrix()
    square_matrix.print()

    l, u = LUDecomposition(scr_matrix).decompose()
    print()
    l.to_SquareMatrix().print()
    print()
    u.to_SquareMatrix().print()
    print()
    (l.to_SquareMatrix() * u.to_SquareMatrix()).print()
    print()
    x = SystemSolver(scr_matrix, [9, 1, 4, 3, 5]).solve()
    print(x, "\n")

    #matrix.transpose().print()
    inverse_matrix = InverseFromLU(scr_matrix).calculate()
    inverse_matrix.to_SquareMatrix().print()
    print()
    (matrix * inverse_matrix.to_SquareMatrix()).print()