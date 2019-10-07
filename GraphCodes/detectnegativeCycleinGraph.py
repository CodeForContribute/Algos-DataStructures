class Graph:
    def __init__(self, v):
        self.v = v
        self.graph = []

    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])

    def isNegativeCycle(self, src, distance):
        import sys
        # distance = [sys.maxsize for i in range(self.v)]
        distance[src] = 0
        for i in range(self.v - 1):
            for u, v, w in self.graph:
                if distance[u] != sys.maxsize and distance[v] > distance[u] + w:
                    distance[v] = distance[u] + w

        for u, v, w in self.graph:
            if distance[u] != sys.maxsize and distance[v] > distance[u] + w:
                # print("Negative Cycle is present")
                return True

    def forDiscconectedGraphAlso(self):
        visited = [False for i in range(self.v)]
        import sys
        distance = [sys.maxsize for i in range(self.v)]
        for i in range(self.v):
            if not visited[i]:
                if self.isNegativeCycle(i, distance):
                    return True
                for i in range(len(distance)):
                    if distance[i] != sys.maxsize:
                        visited[i] = True
        return False


if __name__ == '__main__':
    g = Graph(5)
    g.addEdge(0, 1, 1)
    # g.addEdge(0, 2, 4)
    g.addEdge(1, 2, -1)
    g.addEdge(2, 3, -1)
    # g.addEdge(1, 4, 2)
    # g.addEdge(3, 2, 5)
    g.addEdge(3, 0, -1)
    # g.addEdge(4, 3, -3)
    print(g.forDiscconectedGraphAlso())
