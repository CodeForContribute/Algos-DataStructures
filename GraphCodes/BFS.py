from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    # Time Complexity : O(V+E) where V->number of vertcies & E-number of Edges
    def BFS(self, s):
        visited = [False]*len(self.graph)
        q = list()
        q.append(s)
        visited[s] = True
        while len(q):
            s = q.pop(0)
            print(s, end=" ")
            for i in self.graph[s]:
                if visited[i] is False:
                    q.append(i)
                    visited[i] = True

if __name__ == '__main__':
    g = Graph()
    g.addEdge(0, 1)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 3)
    print("Following is the BFS")
    g.BFS(0)

