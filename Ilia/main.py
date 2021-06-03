import time
import random
from random import randint
import matplotlib.pyplot as plt

q = 1
n = 10000
r = 1000000

T_a = []
M_a = []

T_b = []
M_b = []


class Edge:
    def __init__(self, startNode_, endNode_, length_):
        self.startNode = startNode_
        self.endNode = endNode_
        self.length = length_


def algorithms(m):
    arr = []
    for _ in range(m):
        e = Edge(randint(0, n - 1), randint(0, n - 1), randint(q, r))
        arr.append(e)
        # do your fuckery


start_time = time.time()
for i in range(100000, 10000000, 100000):
    M_a.append(i)
    algorithms(i)
    T_a.append(time.time() - start_time)

start_time = time.time()
for i in range(1000, 100000, 1000):
    M_b.append(i)
    algorithms(i)
    T_b.append(time.time() - start_time)

plt.figure(figsize=(8, 4))
plt.subplot(1, 2, 1)
plt.title("Ta(m):")
plt.plot(T_a, M_a)
plt.subplot(1, 2, 2)
plt.title("Tb(m):")
plt.plot(T_b, M_b)
plt.show()

