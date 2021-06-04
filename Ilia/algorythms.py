from heapq_max import *

INF = 10**14


class Edge:
    def __init__(self, startNode_, endNode_, length_):
        self.startNode = startNode_
        self.endNode = endNode_
        self.length = length_

    def __str__(self):
        return str([self.startNode, self.endNode, self.length])


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
            if d[edge.startNode - 1] < INF:
                if d[edge.endNode - 1] > d[edge.startNode - 1] + edge.length:
                    d[edge.endNode - 1] = d[edge.startNode - 1] + edge.length
                    any = True
        if not any:
            break
    return d


# e1 = Edge(1, 2, 5)
# e2 = Edge(1, 3, 7)
# e3 = Edge(2, 3, 1)
# Edges = [e1, e2, e3]
# print(ford_bellman(1, 3, Edges))