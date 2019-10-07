from collections import defaultdict


class Graph:
    def __init__(self, v):
        self.v = v
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)
        # self.graph[v].append(u)

    def findParent(self, parent, node):
        if parent[node] == -1:
            return node
        if parent[node] != -1:
            return self.findParent(parent, parent[node])

    def union(self, parent, i, j):
        x_set = self.findParent(parent, i)
        y_set = self.findParent(parent, j)
        parent[x_set] = y_set

    def isCycle(self):
        """
          implementation of union() and find() is naive and takes O(n) time in worst case.
          These methods can be improved to O(Logn) using Union by Rank or Height.
        :return:
        """
        parent = [-1] * self.v
        for i in self.graph:
            for j in self.graph[i]:
                x = self.findParent(parent, i)
                y = self.findParent(parent, j)
                if x == y:
                    return True
                self.union(parent, i, j)
        # return False


if __name__ == '__main__':
    g = Graph(3)
    g.addEdge(0, 1)
    g.addEdge(1, 2)
    g.addEdge(2, 0)

    if g.isCycle():
        print("Graph contains cycle")
    else:
        print("Graph does not contain cycle ")
