from collections import defaultdict


class Graph:
    def __init__(self, v):
        self.v = v
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)
        # self.graph[v].append(u)

    def countPaths(self, source, destination):
        visited = [False for i in range(self.v)]
        pathCount = [0]
        result = []
        self.CountPathsUtil(source, destination, visited, pathCount, result)
        return pathCount[0]

    #
    def CountPathsUtil(self, source, destination, visited, pathCount, result):
        visited[source] = True
        if source == destination:
            result.append(destination)
            # print(destination,end=" ")
            pathCount[0] += 1
        else:
            i = 0
            # print(source)
            while i < len(self.graph[source]):
                if not visited[self.graph[source][i]]:
                    self.CountPathsUtil(self.graph[source][i], destination, visited, pathCount, result)
                # print("\n")
                result.append(self.graph[source][i])
                # print(self.graph[source][i],end=" ")
                i += 1
        visited[source] = False
        print(result)


if __name__ == '__main__':
    # Create a graph given in the
    # above diagram
    g = Graph(4)
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(0, 3)
    g.addEdge(2, 0)
    g.addEdge(2, 1)
    g.addEdge(1, 3)

    s = 2
    d = 3
    print(g.countPaths(s, d))
