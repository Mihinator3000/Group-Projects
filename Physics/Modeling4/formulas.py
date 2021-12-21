from math import *
from matplotlib import pyplot as plt


def calculate_x(t, C1, C2, a):
    return C1 * t - ((C2 * exp(-1 * a**2 * t)) / a**2)


def calculate_y(t, C2, a):
    return C2 * exp(-1 * a**2 * t) / a


def make_graph(m, q, v, B, alpha, color: str):
    a = q * B / m
    C1 = (v * (a * cos(alpha) + sin(alpha))) / a
    C2 = -1 * (v * sin(alpha)) / a

    arr_x = []
    arr_y = []
    arr_t = [i / 10**14 for i in range(2 * 10**5)]

    for t in arr_t:
        arr_x.append(calculate_x(t, C1, C2, a))
        arr_y.append(calculate_y(t, C2, a))

    min_y = abs(min(arr_y))
    arr_y_normalized = [y + min_y for y in arr_y]
    plt.plot(arr_x, arr_y_normalized, color=color)
    plt.title("y(x)")
    plt.show()
