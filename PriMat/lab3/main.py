import lab3.entities.squareMatrix as squareMatrix
from lab3.algorithms.inverseFromLU import InverseFromLU
from lab3.algorithms.jacobiSystemSolver import JacobiSystemSolver
from lab3.algorithms.luDecomposition import LUDecomposition
from lab3.algorithms.gaussSystemSolver import GaussSystemSolver

if __name__ == "__main__":
    matrix = squareMatrix.SquareMatrix([
        [10, 0, 5, 0, 3],
        [4, 50, 0, 9, 2],
        [1, 0, 70, 2, 0],
        [0, 0, 3, 40, 0],
        [3, 4, 0, 2, 90]
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
    x_gauss = GaussSystemSolver(scr_matrix, [9, 1, 4, 3, 5]).solve()
    print(x_gauss, "\n")
    x_jacobi = JacobiSystemSolver(scr_matrix, [9, 1, 4, 3, 5], 10**(-6)).solve()
    print(x_jacobi, "\n")

    #matrix.transpose().print()
    inverse_matrix = InverseFromLU(scr_matrix).calculate()
    inverse_matrix.to_SquareMatrix().print()
    print()
    (matrix * inverse_matrix.to_SquareMatrix()).print()