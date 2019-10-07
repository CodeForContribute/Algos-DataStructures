from collections import defaultdict


class Graph:
    def __init__(self, v):
        self.v = v
        self.graph = defaultdict(list)
        self.indegree = [0] * v

    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.indegree[v] += 1

    def allToplogicalSort(self):
        visited = [False] * self.v
        result = []
        self.allTopologicalSortUtil(result, visited)

    def allTopologicalSortUtil(self, result, visited):
        flag = False
        for node in range(self.v):
            if self.indegree[node] == 0 and not visited[node]:
                for neighbor in self.graph[node]:
                    self.indegree[neighbor] -= 1
                result.append(node)
                visited[node] = True
                self.allTopologicalSortUtil(result, visited)
                visited[node] = False
                result.pop()
                for neighbor in self.graph[node]:
                    self.indegree[neighbor] += 1
                flag = True
        if not flag:
            print(result)


if __name__ == '__main__':
    g = Graph(6)
    g.addEdge(5, 2)
    g.addEdge(5, 0)
    g.addEdge(4, 0)
    g.addEdge(4, 1)
    g.addEdge(2, 3)
    g.addEdge(3, 1)
    g.allToplogicalSort()
