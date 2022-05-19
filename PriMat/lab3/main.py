import random

from lab3.algorithms.seidelSystemSolver import SeidelSystemSolver
from lab3.entities.squareMatrix import SquareMatrix
from lab3.entities.gilbertMatrix import GilbertMatrix
from lab3.algorithms.inverseFromLU import InverseFromLU
from lab3.algorithms.jacobiSystemSolver import JacobiSystemSolver
from lab3.algorithms.luDecomposition import LUDecomposition
from lab3.algorithms.gaussSystemSolver import GaussSystemSolver

from time import time
import matplotlib.pyplot as plt
import sys
import threading

sys.setrecursionlimit(10 ** 9)
threading.stack_size(2 ** 27)


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


def test_system_solutions_on_diagonal_matrices():
    N = [50 * i for i in range(1, 11)]

    t_gauss = []
    t_jacobi = []

    for n in N:
        matrix = SquareMatrix.fill_diagonal_advantage(n).to_SCRMatrix()
        F = [random.randint(-n // 2, n // 2) for _ in range(n)]

        start_time = time()
        x_gauss = GaussSystemSolver(matrix, F).solve()
        t_gauss.append(time() - start_time)

        start_time = time()
        x_jacobi = JacobiSystemSolver(matrix, F, 10 ** (-3)).solve()
        t_jacobi.append(time() - start_time)

        errors = []
        for gauss, jacobi in zip(x_gauss, x_jacobi):
            errors.append(abs(1 - jacobi / gauss))

        print(f"Average error is {sum(errors) / n}")

    plt.plot(N, t_gauss, color="orange")
    plt.plot(N, t_jacobi, color="blue")
    plt.legend(["Gauss Method", "Jacobi Method"])
    plt.xlabel("N")
    plt.ylabel("t, c")
    plt.show()


def test_system_solutions_on_gilbert_matrices():
    N = [20 * i for i in range(1, 11)]

    t_gauss = []
    t_jacobi = []

    for n in N:
        matrix = GilbertMatrix(n).to_SCRMatrix()
        F = [random.randint(n // 2, n * 2) for _ in range(n)]

        start_time = time()
        x_gauss = GaussSystemSolver(matrix, F).solve()
        t_gauss.append(time() - start_time)

        start_time = time()
        x_jacobi = JacobiSystemSolver(matrix, F, 10 ** (-6)).solve()
        t_jacobi.append(time() - start_time)

        errors = []
        for gauss, jacobi in zip(x_gauss, x_jacobi):
            errors.append(abs(1 - jacobi / gauss))

        print(f"Average error is {sum(errors) / n}")

    plt.plot(N, t_gauss, color="orange")
    plt.plot(N, t_jacobi, color="blue")
    plt.legend(["Gauss Method", "Jacobi Method"])
    plt.xlabel("N")
    plt.ylabel("t, c")
    plt.show()


if __name__ == "__main__":
    # test_matrix_functions_and_system_solutions()
    thread1 = threading.Thread(target=test_system_solutions_on_diagonal_matrices())
    thread1.start()
    # thread2 = threading.Thread(target=test_system_solutions_on_gilbert_matrices())
    # thread2.start()


