import matplotlib.pyplot as plt
import numdifftools as nd
from math import sqrt, fabs

INF = 10 ** 9


def drawGraph(func):
    def wrapper(solution):
        result = func(solution)

        print("Minimum found, value is: ", result)
        # plt.plot([i for i in range(result[2])], result[1], label=func.__name__)

        return result

    return wrapper


class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __str__(self):
        return f"x: {self.x}, y: {self.y}"

    def __repr__(self):
        return f"x: {self.x}, y: {self.y}"

    def distance_to_other(self, other):
        return sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

    def func_distance_to_other(self, other):
        return fabs(Solution.__func__([self.x, self.y]) - Solution.__func__([other.x, other.y]))

    def to_list(self):
        return [self.x, self.y]

    def __add__(self, other):
        if type(other) != Point:
            raise ValueError

        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        if type(other) != Point:
            raise ValueError

        return Point(self.x - other.x, self.y - other.y)

    def __mul__(self, number):
        return Point(self.x * number, self.y * number)

    def __truediv__(self, number):
        return Point(self.x / number, self.y / number)


class Solution:
    def __init__(self, start_point: Point, precision: float):
        self.__start_point = start_point
        self.__precision = precision

    def constant_learning_rate_method(self, learning_rate):
        prev_point = Point(INF, INF)
        optimization_point = self.__start_point
        amount_func_calculations = 0
        optimization_points = []

        while True:
            optimization_points.append(optimization_point)

            amount_func_calculations += 2
            if (optimization_point.distance_to_other(prev_point) <= self.__precision or
                    optimization_point.func_distance_to_other(prev_point) <= self.__precision):
                return optimization_points, amount_func_calculations

            prev_point.x, prev_point.y = optimization_point.x, optimization_point.y
            x, y = nd.Gradient(self.__func__)(optimization_point.to_list())
            optimization_point.x -= x * learning_rate
            optimization_point.y -= y * learning_rate
            amount_func_calculations += 1

    def step_fragmentation_method(self, const, fragmentation_const):
        prev_point = Point(INF, INF)
        optimization_point = self.__start_point
        amount_func_calculations = 0
        start_learning_rate = 1
        learning_rate = start_learning_rate
        optimization_points = []

        while True:
            optimization_points.append(optimization_point)

            amount_func_calculations += 2
            if (optimization_point.distance_to_other(prev_point) <= self.__precision or
                    optimization_point.func_distance_to_other(prev_point) <= self.__precision):
                return optimization_points, amount_func_calculations

            prev_point.x, prev_point.y = optimization_point.x, optimization_point.y
            x, y = nd.Gradient(self.__func__)(optimization_point.to_list())
            optimization_point.x -= x * learning_rate
            optimization_point.y -= y * learning_rate
            amount_func_calculations += 1

            func_of_point = self.__func__([optimization_point.x, optimization_point.y])
            func_of_prev_point = self.__der_func__([prev_point.x, prev_point.y])
            amount_func_calculations += 2

            while func_of_point <= func_of_prev_point - const * learning_rate * fabs(func_of_prev_point):
                learning_rate *= fragmentation_const

    def golden_ratio_method(self):
        prev_point = Point(INF, INF)
        optimization_point = self.__start_point
        amount_func_calculations = 0
        optimization_points = []

        while True:
            optimization_points.append(optimization_point)
            prev_point.x, prev_point.y = optimization_point.x, optimization_point.y

            amount_func_calculations += 2
            if (optimization_point.distance_to_other(prev_point) <= self.__precision or
                    optimization_point.func_distance_to_other(prev_point) <= self.__precision):
                return optimization_points, amount_func_calculations

            x, y = nd.Gradient(self.__func__)(optimization_point.to_list())
            gradient = Point(x, y)

            learning_rate = self.__golden_search__(optimization_point, gradient, 0, 1)

            optimization_point.x -= x * learning_rate
            optimization_point.y -= y * learning_rate

    def __golden_search__(self, point, gradient, left_border, right_border):
        ratio_const = (3 - sqrt(5)) / 2
        left_ratio_point = left_border + (right_border - left_border) * ratio_const
        right_ratio_point = right_border - (right_border - left_border) * ratio_const

        while fabs(left_border - right_border) > self.__precision:
            func_of_left = self.__func__((point - gradient * left_ratio_point).to_list())
            func_of_right = self.__func__((point - gradient * right_ratio_point).to_list())

            if func_of_left < func_of_right:
                right_border = right_ratio_point
            else:
                left_border = left_ratio_point

            left_ratio_point = left_border + (right_border - left_border) * ratio_const
            right_ratio_point = right_border - (right_border - left_border) * ratio_const

        return (left_border + right_border) / 2

    @staticmethod
    def __func__(args):
        return args[0] ** 2 + args[1] ** 2

    @staticmethod
    def __der_func__(args):
        return 2 * args[0] + 2 * args[1]
