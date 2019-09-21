from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    # Time Complexity : O(V+E) where V->number of vertcies & E-number of Edges
    def DFS(self, v):
        # pass
        if v not in self.graph.keys():
            return
        visited = [False] * len(self.graph)
        self.DFSUtil(v, visited)

    def DFSUtil(self, v, visited):
        visited[v] = True
        print(v, end=" ")
        for i in self.graph[v]:
            if visited[i] is False:
                self.DFSUtil(i, visited)


if __name__ == '__main__':
    g = Graph()
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 3)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 3)
    print("Depth First Traversal")
    g.DFS(0)
