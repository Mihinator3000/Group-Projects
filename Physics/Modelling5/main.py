import cmath as c
import matplotlib.pyplot as plt

from math import factorial, sqrt, pi, cos, exp, acos
from scipy.misc import derivative


def f(x, l):
    return (x ** 2 - 1) ** l


def der_f(x, l, m):
    order = l + abs(m)
    return derivative(f, x0=x, n=order, args=[l], order=2 * order + 1)


def calculate_func(theta, l, m):
    cos_theta = [cos(x) for x in theta]
    a_lm = sqrt(factorial(l - abs(m)) * (2 * l + 1) / (factorial(l + abs(m)) * 4 * pi))
    deg = complex(0, m)
    return [(a_lm * c.exp(acos(cos_x) * deg).real * 1 / 2 ** l * 1 / factorial(l) * (1 - cos_x ** 2) ** (abs(m) / 2) *
             der_f(cos_x, l, m))**2 for cos_x in cos_theta]


def draw_axis(y_lim: list):
    fig = plt.figure()
    rect = [0.1, 0.1, 0.8, 0.8]

    ax_linear = fig.add_axes(rect)
    ax_linear.axes.get_xaxis().set_visible(False)
    ax_linear.spines["right"].set_visible(False)
    ax_linear.spines["top"].set_visible(False)
    ax_linear.spines["bottom"].set_visible(False)
    ax_linear.set_ylim(y_lim)

    ax_polar = fig.add_axes(rect, polar=True, frameon=False)
    ax_polar.set_theta_zero_location("N")
    ax_polar.set_xticks([i / 10000 for i in range(0, 2 * 31415 + 1, 5236)])
    return ax_polar


def draw_tick_circles(polar_subplot, max_r):
    colors = ["green", "blue"]
    circle_amount = 1
    while max_r / circle_amount > 0.05:
        circle_amount += 1

    for i in range(circle_amount):
        polar_subplot.plot(theta,
                           [(i + 1) * max_r / circle_amount for _ in range(len(theta))],
                           color=colors[i % 2],
                           linewidth=0.5)


def draw_func_plot(theta, r, polar_subplot):
    polar_subplot.plot(theta, r, color="black", linewidth=0.5)


if __name__ == '__main__':
    theta = [i / 1000 for i in range(2 * 3141 + 1)]

    r = calculate_func(theta, 1, 1)
    max_r = max(r)
    print(theta[1], r[1])

    polar_subplot = draw_axis([-max_r, max_r])

    draw_tick_circles(polar_subplot, max_r)
    draw_func_plot(theta, r, polar_subplot)

    plt.yticks([])
    plt.show()
