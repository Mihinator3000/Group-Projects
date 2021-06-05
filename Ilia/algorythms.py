import Dheap


class Edge:
    def __init__(self, startNode_, endNode_, length_):
        self.startNode = startNode_
        self.endNode = endNode_
        self.length = length_

    def __str__(self):
        return str([self.startNode, self.endNode, self.length])


def dijkstra_old(s, numOfNodes, availableWays, lengthOfWays):
    d = [Dheap.INF for _ in range(numOfNodes)]
    used = [False for _ in range(numOfNodes)]
    d[s - 1] = 0
    for i in range(numOfNodes):
        v = -1
        for j in range(numOfNodes):
            if not used[j] and (v == - 1 or d[j] < d[v]):
                v = j
        if d[v] == Dheap.INF:
            break
        used[v] = True
        for j in range(len(availableWays[v])):
            if d[availableWays[v][j]] > d[v] + lengthOfWays[v][j]:
                d[availableWays[v][j]] = d[v] + lengthOfWays[v][j]


def dijkstra(s, numOfNodes, graph):
    d = [Dheap.INF for _ in range(numOfNodes)]
    queue = Dheap.MinHeap(4, [])
    d[s - 1] = 0
    queue.add_element([[0, s]])
    while queue.length() != 0:
        cur_d, v = queue.extract_root()
        if cur_d > d[v - 1]:
            continue
        for j in range(len(graph[v - 1])):
            length, to = graph[v - 1][j]
            if d[v - 1] + length < d[to - 1]:
                d[to - 1] = d[v - 1] + length
                queue.add_element([[d[to - 1], to]])
    return d


def ford_bellman(s, numOfNodes, Edges):
    d = [Dheap.INF for _ in range(numOfNodes)]
    d[s - 1] = 0
    while True:
        any = False
        for edge in Edges:
            if d[edge.startNode - 1] < Dheap.INF:
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
# test = []
# heappush_max(test, [-3, 1])
# heappush_max(test, [-5, 2])
# tmp = heappop_max(test)
# to, v = -tmp[0], tmp[1]
# print(to, v)
# print(dijkstra(1, 3, [[[5, 2], [7, 3]], [[1, 3]], []]))
# array = [[5, 2], [7, 1]]
# max_heap_4_children = MinHeap(4, array)
# max_heap_4_children.add_element([[0, 5]])
# print(max_heap_4_children.elements())
# print(max_heap_4_children.extract_root())
