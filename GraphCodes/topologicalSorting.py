# Python program to print topological sorting of a DAG
from collections import defaultdict


class Graph:
    """
    Topological Sorting is mainly used for scheduling jobs from the given dependencies among jobs. In computer science, applications of this type arise in instruction scheduling, ordering of formula cell evaluation when recomputing formula values in spreadsheets, logic synthesis, determining the order of compilation tasks to perform in makefiles, data serialization,
     and resolving symbol dependencies in linkers
    """

    def __init__(self, vertices):
        self.v = vertices
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def topologicalSorting(self):
        """
        Time Complexity: The algorithm is simply DFS with an extra stack. So time complexity is the same as DFS which is O(V+E).
        :return:
        """
        stack = []
        visited = [False] * self.v
        for node in range(self.v):
            if not visited[node]:
                self.topologicalSortUtil(node, visited, stack)
        while len(stack):
            temp = stack.pop()
            print(temp, end=" ")

    def topologicalSortUtil(self, node, visited, stack):
        visited[node] = True
        for adj in self.graph[node]:
            if not visited[adj]:
                self.topologicalSortUtil(adj, visited, stack)
        stack.append(node)


if __name__ == '__main__':
    g = Graph(6)
    g.addEdge(5, 2)
    g.addEdge(5, 0)
    g.addEdge(4, 0)
    g.addEdge(4, 1)
    g.addEdge(2, 3)
    g.addEdge(3, 1)
    print("Following is a Topological Sort of the given graph")
    g.topologicalSorting()
