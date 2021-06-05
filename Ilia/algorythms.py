import fourHeap


class Edge:
    def __init__(self, startNode_, endNode_, length_):
        self.startNode = startNode_
        self.endNode = endNode_
        self.length = length_

    def __str__(self):
        return str([self.startNode, self.endNode, self.length])


def dijkstra(s, numOfNodes, graph):
    d = [fourHeap.INF for _ in range(numOfNodes)]
    queue = fourHeap.fourHeap([])
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
    d = [fourHeap.INF for _ in range(numOfNodes)]
    d[s - 1] = 0
    while True:
        any = False
        for edge in Edges:
            if d[edge.startNode - 1] < fourHeap.INF:
                if d[edge.endNode - 1] > d[edge.startNode - 1] + edge.length:
                    d[edge.endNode - 1] = d[edge.startNode - 1] + edge.length
                    any = True
        if not any:
            break
    return d
