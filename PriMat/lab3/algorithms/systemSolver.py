from lab3.algorithms.luDecomposition import LUDecomposition
from lab3.entities.scrMatrix import SCRMatrix


class SystemSolver:
    def __init__(self, a: SCRMatrix, b: []):
        self.a = a
        (self.l, self.u) = LUDecomposition(a).decompose()
        self.b = b

    def solve(self) -> []:
        y = self.calculate_y()
        print(y)
        x = self.calculate_x(y)
        return x

    def calculate_y(self) -> []:
        n = self.a.get_n()
        y = [self.b[0] / self.l.get(0, 0)]

        for i in range(1, n):
            yi = self.b[i]
            for j in range(i - 1):
                yi -= y[j] * self.l.get(i, j)
                print(y[j], self.l.get(i, j), i, j, end='      ')
            y.append(yi / self.l.get(i, i))
            print()

        return y

    def calculate_x(self, y: []) -> []:
        n = self.a.get_n()
        x = [0 for _ in range(n)]
        x[n - 1] = (y[n - 1] / self.u.get(n - 1, n - 1))

        for i in range(n - 1, 0, -1):
            xi = y[i]
            for j in range(n - 1, i, -1):
                xi -= x[j] * self.l.get(i, j)
            x[n - i] = (xi / self.l.get(i, i))

        return x
