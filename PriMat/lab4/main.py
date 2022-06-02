from lab3.entities.gilbertMatrix import *
from algorithms.jacobiRotationMethod import *

if __name__ == "__main__":
    matrix = squareMatrix.SquareMatrix.fill_symmetrical_da(5)
    matrix.print()

    values, vectors, iteration_count = JacobiRotationMethod(matrix.to_SCRMatrix(), 10 ** -3).solve()

    values.print()
    print()
    vectors.print()
    print(iteration_count + '\n')

