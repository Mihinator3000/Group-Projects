from math import *
from matplotlib import pyplot as plt

n_red = 1.331
phi1_red = []
phi2_red = []

n_purple = 1.343
phi1_purple = []
phi2_purple = []

y_positive = [i/100 for i in range(0, 100, 1)]
y_negative = [i/100 for i in range(-99, 0, 1)]

for y in y_positive:
    alpha1 = asin(y)
    alpha2_red = asin(y/n_red)
    alpha2_purple = asin(y / n_purple)

    phi1_red.append(4 * alpha2_red - 2 * alpha1)
    phi1_purple.append(4 * alpha2_purple - 2 * alpha1)

for y in y_negative:
    alpha1 = asin(-1 * y)
    alpha2_red = asin(-1 * y / n_red)
    alpha2_purple = asin(-1 * y / n_purple)

    phi2_red.append(pi - 6 * alpha2_red + 2 * alpha1)
    phi2_purple.append(pi - 6 * alpha2_purple + 2 * alpha1)


n_purple = 1.346
I = []
phi_red = []
phi_purple = []
der_phi_red = []
der_phi_purple = []
arr_y = [i/1000 for i in range(1, 1000)]

for y in arr_y:
    phi_red.append(4 * asin(y / n_red) - 2 * asin(y))
    phi_purple.append(4 * asin(y / n_purple) - 2 * asin(y))
    der_phi_red.append(1/(4 / (sqrt(n_red**2 - y**2)) - 2 / sqrt(1 - y**2)))
    der_phi_purple.append(1/(4 / (sqrt(n_purple ** 2 - y ** 2)) - 2 / sqrt(1 - y ** 2)))


def task1():
    print(f"Maximum phi1 for red light is {round(degrees(max(phi1_red)), 2)}")
    print(f"Minimum phi2 for red light is {round(degrees(min(phi2_red)), 2)}")
    print(f"Maximum phi1 for purple light is {round(degrees(max(phi1_purple)), 2)}")
    print(f"Minimum phi2 for purple light is {round(degrees(min(phi2_purple)), 2)}")

    plt.figure(figsize=(16, 16))
    plt.subplot(1, 2, 1)
    plt.title("Phi1(y)")
    plt.plot(y_positive, phi1_red)
    plt.plot(y_positive, phi1_purple)
    plt.subplot(1, 2, 2)
    plt.title("Phi2(y)")
    plt.plot(y_negative, phi2_red)
    plt.plot(y_negative, phi2_purple)
    plt.show()


def task2():
    plt.figure(figsize=(16, 16))
    plt.title("I(phi)")
    plt.plot(phi_red, der_phi_red)
    plt.plot(phi_purple, der_phi_purple)
    plt.show()


task1()
task2()
