import math
import matplotlib.pyplot as plt

# Globals
e = -1.6 * 1 ** (-19)
m = 9.1 * 1 ** (-31)
delta_t = 10**6


def calculate_a(y, U, R, r):
    r_inner = R - r
    return (e * U / (y * math.log(R / r_inner))) / m


def graph(U, R, r, l, v0):
    r_inner = R - r
    v = [v0]
    v_x, v_y = [v0], [0]
    a_y = [0]
    x, y = [0], [r_inner + r/2]
    t = [0]
    dt = 1
    while x[-1] < l and r_inner < y[-1] < R:
        v.append(math.sqrt(v_x[-1] ** 2 + v_y[-1] ** 2))
        t.append(dt / delta_t)
        a_y.append(calculate_a(y[-1], U, R, r))
        v_y.append(a_y[-1] * dt)
        v_x.append(v0)
        y.append(r_inner + r/2 + (a_y[-1] * dt**2)/(2 * delta_t))
        x.append(v0 * dt / delta_t)

        dt += 1

    if x[-1] < l:
        print("Электрон вылетел из конденсатора!")
    else:
        print("Электрон ударился об верхнюю / нижнюю стенку!")

    plt.figure(figsize=(16, 16))
    plt.subplot(2, 2, 1)
    plt.title("y(x)")
    plt.plot(x, y)
    plt.subplot(2, 2, 2)
    plt.title("y(t)")
    plt.plot(t, y)
    plt.subplot(2, 2, 3)
    plt.title("v(t)")
    plt.plot(t, v)
    plt.subplot(2, 2, 4)
    plt.title("a(t)")
    plt.plot(t[1::-1], a_y[1::-1])
    plt.show()

