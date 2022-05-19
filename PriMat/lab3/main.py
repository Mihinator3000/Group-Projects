from lab3.entities.squareMatrix import SquareMatrix
from lab3.entities.gilbertMatrix import GilbertMatrix
from lab3.algorithms.inverseFromLU import InverseFromLU
from lab3.algorithms.jacobiSystemSolver import JacobiSystemSolver
from lab3.algorithms.luDecomposition import LUDecomposition
from lab3.algorithms.gaussSystemSolver import GaussSystemSolver


def test_matrix_functions_and_system_solutions():
    matrix = SquareMatrix([
        [10, 0, 5, 0, 3],
        [4, 50, 0, 9, 2],
        [1, 0, 70, 2, 0],
        [0, 0, 3, 40, 0],
        [3, 4, 0, 2, 90]
    ])

    print("SCR Matrix")
    scr_matrix = matrix.to_SCRMatrix()
    scr_matrix.print()

    print("Square Matrix")
    square_matrix = scr_matrix.to_SquareMatrix()
    square_matrix.print()

    print("LU Decomposition")
    l, u = LUDecomposition(scr_matrix).decompose()

    print("L Matrix")
    l.to_SquareMatrix().print()

    print("U Matrix")
    u.to_SquareMatrix().print()

    print("L * U = A")
    (l.to_SquareMatrix() * u.to_SquareMatrix()).print()

    print("System solution via Gauss Method")
    x_gauss = GaussSystemSolver(scr_matrix, [9, 1, 4, 3, 5]).solve()
    print(x_gauss)

    print("System solution via Jacobi Method")
    x_jacobi = JacobiSystemSolver(scr_matrix, [9, 1, 4, 3, 5], 10 ** (-6)).solve()
    print(x_jacobi)

    print("Inverse matrix")
    inverse_matrix = InverseFromLU(scr_matrix).calculate()
    inverse_matrix.to_SquareMatrix().print()

    print("A * A^(-1)")
    (matrix * inverse_matrix.to_SquareMatrix()).print()

    print("Gilbert Matrix")
    gilbert_matrix = GilbertMatrix(5)
    gilbert_matrix.print()

    print("Diagonal Matrix")
    diagonal_matrix = SquareMatrix.fill_diagonal_advantage(5)
    diagonal_matrix.print()


if __name__ == "__main__":
    test_matrix_functions_and_system_solutions()

