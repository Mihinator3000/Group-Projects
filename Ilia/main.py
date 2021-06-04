import time
import random
from random import randint
import matplotlib.pyplot as plt
import algorythms
from sys import *
import threading

setrecursionlimit(10 ** 9)
threading.stack_size(2 ** 27)

q = 1
n = 10000
r = 1000000

T_a = []
M_a = []

T_b = []
M_b = []


def execution(m):
    arr = []
    for _ in range(m):
        e = algorythms.Edge(randint(0, n - 1), randint(0, n - 1), randint(q, r))
        arr.append(e)
    d = [algorythms.INF for _ in range(n)]
    algorythms.ford_bellman(0, d, arr)
    print(m)


def work():
    for i in range(100000, 1000000, 100000):
        start_time = time.time()
        M_a.append(i)
        execution(i)
        T_a.append(time.time() - start_time)

    for i in range(1000, 100000, 1000):
        start_time = time.time()
        M_b.append(i)
        execution(i)
        T_b.append(time.time() - start_time)

    plt.figure(figsize=(8, 4))
    plt.subplot(1, 2, 1)
    plt.title("Ta(m):")
    plt.plot(T_a, M_a)
    plt.subplot(1, 2, 2)
    plt.title("Tb(m):")
    plt.plot(T_b, M_b)
    plt.show()


thread = threading.Thread(target=work)
thread.start()

