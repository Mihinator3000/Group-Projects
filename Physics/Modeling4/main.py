from math import *
from matplotlib import pyplot as plt

m = 20 * 1.66 * 10**(-27)
q = 1.6 * 10**(-19)
v = 10**3
B = 10**(-2)

alpha = radians(60)
C1 = v * cos(alpha) + (v * sin(alpha) * m) / (q * B)
C2 = -1 * (v * sin(alpha) * m) / (q * B)


def calculate_x(t):
    return C1 * t - ((C2 * m**2)/(q**2 * B)) * exp(-q**2 * B * t / m**2)


def calculate_y(t):
    return (C2 * m / q) * exp(-q**2 * B * t / m**2)


arr_x = []
arr_y = []
arr_t = [i / 10**15 for i in range(1, 10000)]
for t in arr_t:
    arr_x.append(calculate_x(t))
    arr_y.append(calculate_y(t))

plt.plot(arr_x, arr_y)
plt.show()
