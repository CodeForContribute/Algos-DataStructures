from collections import defaultdict


class Graph:
    def __init__(self, v):
        self.v = v
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    # Time Complexity: The program does a simple DFS Traversal of graph and graph is represented using adjacency list.
    # So the time complexity is O(V+E)
    def isCycleUndirected(self, node, visited, parent):
        visited[node] = True
        for neighbor in self.graph[node]:
            if not visited[neighbor]:
                if self.isCycleUndirected(neighbor, visited, node):
                    return True
            elif parent != neighbor:
                return True

        return False

    def isCyclic(self):
        visited = [False for i in range(self.v)]
        for i in range(self.v):
            if not visited[i]:
                if self.isCycleUndirected(i, visited, -1):
                    return True


if __name__ == '__main__':
    g = Graph(5)
    g.addEdge(1, 0)
    g.addEdge(0, 2)
    g.addEdge(2, 4)
    g.addEdge(0, 3)
    g.addEdge(3, 4)

    if g.isCyclic():
        print("Graph contains cycle")
    else:
        print("Graph does not contain cycle ")
