from heapq_max import *

INF = 100000000001


class Edge:
    def __init__(self, startNode_, endNode_, length_):
        self.startNode = startNode_
        self.endNode = endNode_
        self.length = length_


def dijkstra(s, numOfNodes, graph):
    d = [INF for _ in range(numOfNodes)]
    queue = []
    d[s - 1] = 0
    heappush_max(queue, [0, s])
    while queue:
        cur_d, v = heappop_max(queue)
        if cur_d > d[v - 1]:
            continue
        for j in range(len(graph[v - 1])):
            length, to = graph[v - 1][j]
            if d[v - 1] + length < d[to - 1]:
                d[to - 1] = d[v - 1] + length
                heappush_max(queue, [d[to - 1], to])
    return d


def ford_bellman(s, numOfNodes, Edges):
    d = [INF for _ in range(numOfNodes)]
    d[s - 1] = 0
    while True:
        any = False
        for edge in Edges:
            if d[edge.startNode] < INF:
                if d[edge.endNode] > d[edge.startNode] + edge.length:
                    d[edge.endNode] = d[edge.startNode] + edge.length
                    any = True
        if not any:
            break
    return d