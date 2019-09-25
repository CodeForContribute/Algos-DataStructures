from collections import defaultdict


class Graph:
    def __init__(self, v):
        self.v = v
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def iterativeDFS(self):
        stack = []
        visited = [False for i in range(self.v)]
        for i in range(self.v):
            if not visited[i]:
                stack.append(i)
                while len(stack):
                    s = stack.pop(0)
                    if not visited[s]:
                        print(s, end=" ")
                        visited[s] = True
                    for node in self.graph[s]:
                        if not visited[node]:
                            stack.append(node)


if __name__ == '__main__':
    g = Graph(5)  # Total 5 vertices in graph  
    g.addEdge(1, 0)
    g.addEdge(0, 2)
    g.addEdge(2, 1)
    g.addEdge(0, 3)
    g.addEdge(4, 4)

    print("Following is Depth First Traversal")
    g.iterativeDFS()
