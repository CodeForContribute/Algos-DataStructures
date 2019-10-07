from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, graph, u, v):
        graph[u].append(v)
        graph[v].append(u)

    def BFS(self, graph, src, dest, v, pred, distance):
        q = []
        visited = [False] * v
        q.append(src)
        distance[src] = 0
        visited[src] = True
        while len(q):
            u = q.pop(0)
            for i in graph[u]:
                if not visited[i]:
                    visited[i] = True
                    distance[i] = distance[u] + 1
                    pred[i] = u
                    q.append(i)
                    if i == dest:
                        return True

    def printShortestPath(self, graph, src, dest, v):
        """
        Time Complexity : O(V + E)
        Auxiliary Space : O(V)
        :param graph:
        :param src:
        :param dest:
        :param v:
        :return: distance, Path from src->dest
        """
        distance = [float("inf")] * v
        pred = [-1] * v
        if self.BFS(graph, src, dest, v, pred, distance) is False:
            print("Given source and destination are not connected")
            return
        path = []
        crawl = dest
        path.append(crawl)
        while pred[crawl] != -1:
            path.append(pred[crawl])
            crawl = pred[crawl]
        print(path)
        print(distance)


if __name__ == '__main__':
    v = 8
    graph = Graph()
    graph.addEdge(graph.graph, 0, 1)
    graph.addEdge(graph.graph, 0, 3)
    graph.addEdge(graph.graph, 1, 2)
    graph.addEdge(graph.graph, 3, 4)
    graph.addEdge(graph.graph, 3, 7)
    graph.addEdge(graph.graph, 4, 5)
    graph.addEdge(graph.graph, 4, 6)
    graph.addEdge(graph.graph, 4, 7)
    graph.addEdge(graph.graph, 5, 6)
    graph.addEdge(graph.graph, 6, 7)
    source = 0
    dest = 6
    graph.printShortestPath(graph.graph, source, dest, v)
