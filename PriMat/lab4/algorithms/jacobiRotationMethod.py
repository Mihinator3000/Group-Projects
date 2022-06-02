import threading

from lab3.entities.scrMatrix import *
from math import *


class JacobiRotationMethod:
    def __init__(self, a: SCRMatrix, precision: float):
        self.a = a
        self.precision = precision

    def solve(self) -> (SCRMatrix, SCRMatrix, int):
        m = SCRMatrix.with_diagonal_ones(self.a.get_n())
        iteration_count = 0

        while True:
            k, l = self.__max_element_indexes()
            self.a, m1 = self.__rotation(k, l)
            m = m * m1
            iteration_count += 1
            if self.__calculate_precision() < self.precision:
                return self.a, m, iteration_count

    def __max_element_indexes(self) -> (int, int):
        max_element = 0
        k = l = 0

        n = self.a.get_n()

        for i in range(n - 1):
            for j in range(i + 1, n):
                element = abs(self.a.get(i, j))
                if element > max_element:
                    max_element = element
                    k, l = i, j

        return k, l

    def __rotation(self, k: int, l: int) -> (SCRMatrix, SCRMatrix):
        m = SCRMatrix.with_diagonal_ones(self.a.get_n())

        phi = pi / 4 if self.a.get(k, k) == self.a.get(l, l)\
            else 0.5 * atan(2.0 * self.a.get(k, l) / (self.a.get(k, k) - self.a.get(l, l)))

        c = cos(phi)
        s = sin(phi)
        m.set(k, k, c)
        m.set(l, l, c)
        m.set(k, l, -s)
        m.set(l, k, s)

        return m * self.a * m.transpose(), m

    def __calculate_precision(self):
        n = self.a.get_n()

        elements_sum = 0

        for i in range(n - 1):
            for j in range(i + 1, n):
                elements_sum += self.a.get(i, j) ** 2

        return sqrt(elements_sum)
