from collections import defaultdict


class Graph:
    def __init__(self, v):
        self.v = v
        self.graph = defaultdict(list)

    def addEdge(self, u, v, w):
        self.graph[u].append([v, w])

    def topologicalSorting(self):
        stack = []
        visited = [False for i in range(self.v)]
        for i in range(self.v):
            self.DFS(i, visited, stack)
        return stack

    def DFS(self, node, visited, stack):
        visited[node] = True
        for neighbor in self.graph[node]:
            if not visited[neighbor]:
                self.DFS(neighbor, visited, stack)
        stack.append(node)

    def longestPath(self, source):
        distance = [float("inf")] * self.v
        distance[source] = 0
        stack = self.topologicalSorting()
        while len(stack):
            u = stack.pop()
            if distance[u] != float("inf"):
                for neighbor in self.graph[u]:
                    if distance[neighbor[0]] > distance[u] + distance[neighbor[1] * -1]:
                        distance[neighbor[0]] = distance[u] + distance[neighbor[1] * -1]
        for i in range(self.v):
            if distance[i] == float("inf"):
                print(float("-inf"), end=" ")
            else:
                print(distance[i] * -1, end=" ")


if __name__ == '__main__':
    g = Graph(6)
    g.addEdge(0, 1, 5)
    g.addEdge(0, 2, 3)
    g.addEdge(1, 3, 6)
    g.addEdge(1, 2, 2)
    g.addEdge(2, 4, 4)
    g.addEdge(2, 5, 2)
    g.addEdge(2, 3, 7)
    g.addEdge(3, 5, 1)
    g.addEdge(3, 4, -1)
    g.addEdge(4, 5, -2)
    s = 1
    g.longestPath(s)
