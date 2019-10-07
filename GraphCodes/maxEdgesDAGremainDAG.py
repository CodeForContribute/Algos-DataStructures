from collections import defaultdict


class Graph:
    def __init__(self, v):
        self.v = v
        self.Indegree = [0] * self.v
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)
        # self.Indegree[v] += 1

    def topolgicalSort(self):
        for node in range(self.v):
            for neighbor in self.graph[node]:
                self.Indegree[neighbor] += 1
        q = []
        topologicalOrder = []
        for node in self.graph:
            if self.Indegree[node] == 0:
                q.append(node)
        while len(q):
            u = q.pop(0)
            topologicalOrder.append(u)
            for v in self.graph[u]:
                self.Indegree[v] -= 1
                if self.Indegree[v] == 0:
                    q.append(v)
        return topologicalOrder

    def returnMaxEdgeAddition(self):
        visited = [False] * self.v
        top_order = self.topolgicalSort()
        for i in range(len(top_order)):
            u = top_order[i]
            for v in self.graph[u]:
                visited[v] = True
            for j in range(i + 1, len(top_order)):
                if not visited[top_order[j]]:
                    print(u, '-->', top_order[j], end=",")

                visited[top_order[j]] = False


if __name__ == '__main__':
    g = Graph(6)
    g.addEdge(5, 2)
    g.addEdge(5, 0)
    g.addEdge(4, 0)
    g.addEdge(4, 1)
    g.addEdge(2, 3)
    g.addEdge(3, 1)
    g.returnMaxEdgeAddition()
