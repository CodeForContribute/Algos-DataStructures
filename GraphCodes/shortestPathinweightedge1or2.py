from collections import defaultdict


class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.V_org = vertices
        self.graph = defaultdict(list)

    def addEdge(self, u, v, w):
        if w == 1:
            self.graph[u].append(v)
        else:
            self.graph[u].append(self.V)
            self.graph[self.V].append(v)
            self.V += 1

    def printPath(self, parent, j):
        path_len = 1
        if parent[j] == -1 and j < self.V_org:
            print(j)
            return 0
        length = self.printPath(parent, parent[j])
        path_len = path_len + length
        if j < self.V_org:
            print(j)
        return path_len

    def findShortestPath(self, src, dest):
        """
        Expected time complexity is O(V+E).
        A Simple Solution is to use Dijkstra’s shortest path algorithm,
        we can get a shortest path in O(E + VLogV) time.
        How to do it in O(V+E) time?
        The idea is to use BFS.
          One important observation about BFS is, the path used in BFS always has least number of edges between
          any two vertices. So if all edges are of same weight, we can use BFS to find the shortest path.
          For this problem, we can modify the graph and split all edges of weight 2 into two edges of weight 1 each.
          In the modified graph, we can use BFS to find the shortest path.
        How many new intermediate vertices are needed?
          We need to add a new intermediate vertex for every source
          vertex. The reason is simple, if we add a intermediate vertex x between u and v and if we add same vertex
          between y and z, then new paths u to z and y to v are added to graph which might have note been
          there in original graph. Therefore in a graph with V vertices, we need V extra vertices.
        :param src:
        :param dest:
        :return: shortestDistance
        """
        visited = [False] * self.V
        parent = [-1] * self.V
        q = list()
        q.append(src)
        visited[src] = True
        while len(q):
            u = q.pop(0)
            if u == dest:
                return self.printPath(parent, u)
            for i in self.graph[u]:
                if not visited[i]:
                    q.append(i)
                    visited[i] = True
                    parent[i] = u


if __name__ == '__main__':
    g = Graph(4)
    g.addEdge(0, 1, 2)
    g.addEdge(0, 2, 2)
    g.addEdge(1, 2, 1)
    g.addEdge(1, 3, 1)
    g.addEdge(2, 0, 1)
    g.addEdge(2, 3, 2)
    g.addEdge(3, 3, 2)

    src = 0
    dest = 3
    print("Shortest Path between %d and %d is  " % (src, dest)),
    l = g.findShortestPath(src, dest)
    print("\nShortest Distance between %d and %d is %d " % (src, dest, l)),
