import Dheap


INF = 100000000001


class Edge:
    def __init__(self, startNode_, endNode_, length_):
        self.startNode = startNode_
        self.endNode = endNode_
        self.length = length_


def dijkstra(s, numOfNodes, d, used, availableWays, lengthOfWays):
    d[s - 1] = 0
    for i in range(numOfNodes):
        v = -1
        for j in range(numOfNodes):
            if not used[j] and (v == - 1 or d[j] < d[v]):
                v = j
        if d[v] == INF:
            break
        used[v] = True
        for j in range(availableWays[v].length()):
            if d[availableWays[v][j]] > d[v] + lengthOfWays[v][j]:
                d[availableWays[v][j]] = d[v] + lengthOfWays[v][j]


def ford_bellman(s, d, Edges):
    d[s] = 0
    while True:
        any = False
        for edge in Edges:
            if d[edge.startNode] < INF:
                if d[edge.endNode] > d[edge.startNode] + edge.length:
                    d[edge.endNode] = d[edge.startNode] + edge.length
                    any = True
        if not any:
            break
