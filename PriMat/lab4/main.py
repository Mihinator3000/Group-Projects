from lab3.entities.gilbertMatrix import *
from algorithms.jacobiRotationMethod import *


def test_matrix_functions_and_eigenvalues():
    print("Square symmetrical matrix")
    matrix = squareMatrix.SquareMatrix.fill_symmetrical_da(3)
    matrix.print()

    print("\nSquare symmetrical matrix")
    gilbert_matrix = GilbertMatrix(3).fill()
    gilbert_matrix.print()

    print("\nJacobi method")
    values, vectors, iteration_count = JacobiRotationMethod(gilbert_matrix.to_SCRMatrix(), 10 ** -3).solve()

    print("\nEigenvalues")
    print(values)
    print("\nEigenvectors")
    vectors.to_SquareMatrix().print()
    print("\nIteration amount")
    print(iteration_count)


if __name__ == "__main__":
    test_matrix_functions_and_eigenvalues()


