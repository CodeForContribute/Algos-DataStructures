class Graph:
    def __init__(self, v):
        self.v = v
        # self.graph = defaultdict(list)
        self.graph = [[] for i in range(self.v)]

    def addEdge(self, u, v, w):
        self.graph[u].append([v, w])
        self.graph[v].append([u, w])

    def findPathMoreThank(self, src, k):
        path = [False] * self.v
        path[src] = True
        return self.findPathMoreThanKUtil(src, k, path)

    # Time Complexity: O(n!)
    def findPathMoreThanKUtil(self, src, k, path):
        if k <= 0:
            return True
        for i in range(len(self.graph[src])):
            v = self.graph[src][i][0]
            w = self.graph[src][i][1]
            if path[v]:
                continue
            if w >= k:
                return True
            path[v] = True
            if self.findPathMoreThanKUtil(v, k - w, path):
                return True
            path[v] = False

        return False


if __name__ == '__main__':

    # create the graph given in above fugure
    V = 9
    g = Graph(V)

    #  making above shown graph
    g.addEdge(0, 1, 4)
    g.addEdge(0, 7, 8)
    g.addEdge(1, 2, 8)
    g.addEdge(1, 7, 11)
    g.addEdge(2, 3, 7)
    g.addEdge(2, 8, 2)
    g.addEdge(2, 5, 4)
    g.addEdge(3, 4, 9)
    g.addEdge(3, 5, 14)
    g.addEdge(4, 5, 10)
    g.addEdge(5, 6, 2)
    g.addEdge(6, 7, 1)
    g.addEdge(6, 8, 6)
    g.addEdge(7, 8, 7)

    src = 0
    k = 62
    if g.findPathMoreThank(src, k):
        print("Yes")
    else:
        print("No")

    k = 60
    if g.findPathMoreThank(src, k):
        print("Yes")
    else:
        print("No")
