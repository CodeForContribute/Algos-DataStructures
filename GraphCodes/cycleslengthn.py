class Graph:
    def __init__(self, v):
        self.v = v
        self.graph = None

    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    ################## InComplete ###################################################
    def cyclesLength(self, visited, n, node, count):
        if n == 0:
            visited[node] = False
            # if self.graph[node][]
        visited[node] = True
        for neighbor in self.graph[node]:
            if not visited[neighbor]:
                count += 1

    def countCycles(self, n):
        if n < 0:
            return
        visited = [False for i in range(self.v)]
        count = 0
        for i in range(self.v - n - 1):
            count = self.cyclesLength(visited, n - 1, i, count)
            visited[i] = True
        return count // 2


######################################################################################
if __name__ == '__main__':
    g = Graph(5)
    g.graph = [[0, 1, 0, 1, 0],
               [1, 0, 1, 0, 1],
               [0, 1, 0, 1, 0],
               [1, 0, 1, 0, 1],
               [0, 1, 0, 1, 0]]

    n = 4
    print("Total cycles of length ", n, " are ", g.countCycles(n))
