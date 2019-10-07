from collections import defaultdict


class Graph:
    def __init__(self, v):
        self.v = v
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def topologicalSort(self):
        in_degree = [0] * self.v
        for node in self.graph:
            for neighbor in self.graph[node]:
                in_degree[neighbor] += 1
        q = []
        for node in range(self.v):
            if in_degree[node] == 0:
                q.append(node)
        count = 0
        top_order = []
        while len(q):
            u = q.pop(0)
            top_order.append(u)
            for v in self.graph[u]:
                in_degree[v] -= 1
                if in_degree[v] == 0:
                    q.append(v)
            count += 1
        if count != self.v:
            print("Cycle exists in the Graph")
        else:
            print(top_order)


if __name__ == '__main__':
    g = Graph(6)
    g.addEdge(5, 2)
    g.addEdge(5, 0)
    g.addEdge(4, 0)
    g.addEdge(4, 1)
    g.addEdge(2, 3)
    g.addEdge(3, 1)

    print("Following is a Topological Sort of the given graph")
    g.topologicalSort()
