import math
import matplotlib.pyplot as plt
# дано U, R, r, l, E, v0, e

# Globals
e = -1.6 * 1 ** (-19)
m = 9.1 * 1 ** (-31)
frequency = 10**5


def calculate_a(y, U, R, r):
    d = R - r
    return -(e * U / (y * math.log(R / d)))/m


def graph(U, R, r, l, E, v0):
    shift = (2*R - r)/2
    v = [v0]
    v_x = [v0]
    v_y = [0]
    a_y = [0]
    space = R - r
    x = [0]
    y = [r/2]
    t = [0]
    dt = 1
    while x[-1] <= l and space < shift < R:
        t.append(dt / frequency)
        a_y.append(calculate_a(shift, U, R, r))
        v_y.append(a_y[-1] * dt / frequency**2)
        v_x.append(v0)
        shift += v_y[-1] / frequency
        x.append(v_x[-1] * dt / frequency ** 2)
        y.append(shift - space)
        v.append(math.sqrt(v_x[-1]**2 + v_y[-1]**2))
        dt += 1
    plt.figure(figsize=(8, 8))
    plt.subplot(2, 2, 1)
    plt.title("y(x)")
    plt.plot(y, x)
    plt.subplot(2, 2, 2)
    plt.title("y(t)")
    plt.plot(y, t)
    plt.subplot(2, 2, 3)
    plt.title("v(t)")
    plt.plot(v, t)
    plt.subplot(2, 2, 4)
    plt.title("a(t)")
    plt.plot(a_y, t)
    plt.show()

