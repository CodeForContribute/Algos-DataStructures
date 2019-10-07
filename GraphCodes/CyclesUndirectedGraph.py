from collections import defaultdict


class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    # me Complexity of this method is same as time complexity of DFS traversal which is O(V+E)
    def isCycleIndirected(self, v, visited, recStack):
        visited[v] = True
        recStack[v] = True
        for neighbor in self.graph[v]:
            if visited[neighbor] and recStack[neighbor]:
                return True
            if self.isCycleIndirected(neighbor, visited, recStack):
                return True

    def isCycle(self):
        visited = [False for i in range(self.vertices)]
        recStack = [False for i in range(self.vertices)]
        for i in range(self.vertices):
            if not visited[i]:
                if self.isCycleIndirected(i, visited, recStack):
                    return True
        return False


if __name__ == '__main__':
    g = Graph(8)
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 5)
    g.addEdge(2, 3)
    g.addEdge(3, 7)
    if g.isCycle() == 1:
        print("Graph has a cycle")
    else:
        print("Graph has no cycle")
