from collections import defaultdict


class Graph:
    """
     Given a Weighted Directed Acyclic Graph (DAG) and a source vertex s in it, find the longest distances from s to all
     other vertices in the given graph.The longest path problem for a general graph is not as easy as the shortest path
     problem because the longest path problem doesn’t have optimal substructure property. In fact, the Longest Path
     problem is NP-Hard for a general graph.However, the longest path problem has a linear time solution for directed
     acyclic graphs.The idea is similar to linear time solution for shortest path in a directed acyclic graph.,
     we use Topological Sorting.
     source-https://www.geeksforgeeks.org/find-longest-path-directed-acyclic-graph/
    """

    def __init__(self, v):
        self.v = v
        self.graph = defaultdict(list)

    def addEdge(self, u, v, w):
        self.graph[u].append([v, w])

    def longestPath(self, source):
        visited = [False for i in range(self.v)]
        stack = []
        distance = [float("-inf") for i in range(self.v)]
        # Find the topological Sorting of the graph
        for i in range(self.v):
            if not visited[i]:
                self.topologicalSortUtil(i, visited, stack)
        print(stack)
        distance[source] = 0
        print(distance)
        while len(stack):
            u = stack.pop()
            for neighbor in range(len(self.graph[u])):
                if distance[self.graph[u][neighbor][0]] < distance[u] + distance[self.graph[u][neighbor][1]]:
                    distance[self.graph[u][neighbor][0]] = distance[u] + distance[self.graph[u][neighbor][1]]

        # print the long distances from the start
        for i in range(len(distance)):
            print(distance[i], end=" ")
        del visited

    def topologicalSortUtil(self, node, visited, stack):
        visited[node] = True
        for neighbor in self.graph[node]:
            if not visited[neighbor[0]]:
                self.topologicalSortUtil(neighbor[0], visited, stack)
        # At last add the node to the stack
        stack.append(node)


if __name__ == '__main__':
    g = Graph(6)
    g.addEdge(0, 1, 5)
    g.addEdge(0, 2, 3)
    g.addEdge(1, 3, 6)
    g.addEdge(1, 2, 2)
    g.addEdge(2, 4, 4)
    g.addEdge(2, 5, 2)
    g.addEdge(2, 3, 7)
    g.addEdge(3, 5, 1)
    g.addEdge(3, 4, -1)
    g.addEdge(4, 5, -2)
    s = 1
    g.longestPath(s)
