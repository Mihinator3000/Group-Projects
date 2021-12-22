from math import *
from matplotlib import pyplot as plt


def calculate_x(t, C1, C2, C3, a):
    return C1 + C2 * cos(2 * t / a) + C3 * sin(2 * t / a)


def calculate_y(t, C2, C3, C4, a):
    return C4 + C3 * (2 / a**2) * cos(2 * t / a) - C2 * (2 / a**2) * sin(2 * t / a)


def make_graph(m, q, v, B, alpha, color: str):
    a = q * B / m

    C1 = (v * sin(alpha) * a**3) / 4
    C2 = -1 * C1
    C3 = (v * cos(alpha)) / 2
    C4 = (-1 * v * cos(alpha)) / a

    arr_x = []
    arr_y = []
    arr_t = [i for i in range(10**5)]

    for num, t in enumerate(arr_t):
        arr_x.append(calculate_x(t, C1, C2, C3, a))
        arr_y.append(calculate_y(t, C2, C3, C4, a))
        if arr_y[-1] < -0.05:
            arr_t = arr_t[0:num]
            break

    plt.plot(arr_x, arr_y, color=color)
    plt.title("y(x)")
    plt.show()
