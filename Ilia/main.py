import time
from random import randint
import matplotlib.pyplot as plt
import algorythms
import threading

threading.stack_size(2 ** 27)

q = 1
n = 10000
r = 1000000

T_fb = []
M_fb = []

T_d = []
M_d = []


def task(m_min, m_step, m_max):
    # creating data
    for m in range(m_min, m_max, m_step):
        arr_edges = []
        for _ in range(m):
            e = algorythms.Edge(randint(1, n), randint(1, n), randint(q, r))
            arr_edges.append(e)
        start_time = time.time()
        M_fb.append(m)
        # execute ford_bellman
        print(algorythms.ford_bellman(1, n, arr_edges))
        T_fb.append(time.time() - start_time)

        arr_pairs = [[] for _ in range(n)]
        for i in arr_edges:
            arr_pairs[i.startNode - 1].append([i.length, i.endNode])
        start_time = time.time()
        M_d.append(m)
        #  execute dijkstra
        print(algorythms.dijkstra(1, n, arr_pairs))
        T_d.append(time.time() - start_time)
        # for e in arr_edges:
        #     print(e, end=" ")
        # print(arr_pairs)
        print(m)


plt.figure(figsize=(8, 8))
thread_a = threading.Thread(target=task(100000, 100000, 10000000))
thread_a.start()
plt.subplot(2, 2, 1)
plt.title("a) T(m) FB:")
plt.plot(T_fb, M_fb)
plt.subplot(2, 2, 2)
plt.title("a) T(m) D:")
plt.plot(T_d, M_d)
T_fb = []
M_fb = []
T_d = []
M_d = []
thread_b = threading.Thread(target=task(1000, 1000, 10000))
thread_b.start()
plt.subplot(2, 2, 3)
plt.title("b) T(m) FB:")
plt.plot(T_fb, M_fb)
plt.subplot(2, 2, 4)
plt.title("b) T(m) D:")
plt.plot(T_d, M_d)
plt.show()

