from collections import defaultdict


class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = defaultdict(list)
        self.tc = [[0 for j in range(self.vertices)] for i in range(self.vertices)]

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def DFSUtil(self, s, v):
        self.tc[s][v] = 1
        for i in self.graph[v]:
            if self.tc[s][i] == 0:
                self.DFSUtil(s, i)

    def transitiveClosure(self):
        for i in range(self.vertices):
            self.DFSUtil(i, i)
        for i in range(self.vertices):
            print(self.tc[i])


if __name__ == '__main__':
    g = Graph(4)
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 3)

    print("Transitive closure matrix is")
    g.transitiveClosure()
