from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(set)

    def addEdge(self, u, v):
        self.graph[u].add(v)

    def printGraph(self):
        v = len(self.graph)
        for key in self.graph.keys():
            print(str(key) + "->" + str(self.graph[key]), end=" ")


if __name__ == '__main__':
    g = Graph()
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 3)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 3)
    g.printGraph()
