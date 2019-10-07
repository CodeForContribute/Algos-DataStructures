from collections import defaultdict


class Graph:
    def __init__(self, v):
        self.v = v
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def topologicalSortDepart(self):
        departureTime = [-1] * (self.v + 1)
        time = [0]
        visited = [False for i in range(self.v)]
        for i in range(self.v):
            self.DFS(i, visited, time, departureTime)
        print(departureTime)

    def DFS(self, src, visited, time, departureTime):
        visited[src] = True
        for neighbor in self.graph[src]:
            if not visited[neighbor]:
                self.DFS(neighbor, visited, time, departureTime)
        departureTime[time[0]] = src
        time[0] = time[0] + 1


if __name__ == '__main__':
    g = Graph(6)
    g.addEdge(5, 2)
    g.addEdge(5, 0)
    g.addEdge(4, 0)
    g.addEdge(4, 1)
    g.addEdge(2, 3)
    g.addEdge(3, 1)
    g.topologicalSortDepart()
