from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    # Method1: Using recursion
    def DFS(self):
        v = len(self.graph)
        visited = [False]*v
        for i in range(v):
            if visited[i] is False:
                self.DFSUtil(i, visited)

    def DFSUtil(self, v, visited):
        visited[v] = True
        print(v, end=" ")
        for i in self.graph[v]:
            if visited[i] is False:
                self.DFSUtil(i, visited)

    def print_graph(self):
        v = len(self.graph)
        for i in range(v):
            print("{}->{}".format(i, self.graph[i]))


if __name__ == '__main__':
    g = Graph()
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    g.add_edge(2, 3)
    g.add_edge(3, 3)
    g.print_graph()
    print("Following is Depth First Traversal:")
    g.DFS()


