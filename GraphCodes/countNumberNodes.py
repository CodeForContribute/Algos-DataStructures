from collections import defaultdict


class Graph:
    def __init__(self, v):
        self.v = v
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def BFS(self, source, level):
        visited = [False for i in range(self.v)]
        q = []
        Level = [0 for j in range(self.v)]
        visited[source] = True
        q.append(source)
        Level[source] = 0
        while len(q):
            s = q.pop(0)
            for i in self.graph[s]:
                if not visited[i]:
                    visited[i] = True
                    Level[i] = Level[s] + 1
                    q.append(i)
        count = 0
        for i in Level:
            if i == level:
                count += 1
        return count


if __name__ == '__main__':
    g = Graph(6)
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 3)
    g.addEdge(2, 4)
    g.addEdge(2, 5)
    level = 2
    print(g.BFS(0, level))
