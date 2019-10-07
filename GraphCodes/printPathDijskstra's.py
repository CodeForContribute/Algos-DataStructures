class Graph:
    def __init__(self):
        self.res = []

    def min_distance(self, distance, queue):
        min_val = float("inf")
        min_index = -1
        for i in range(len(distance)):
            if distance[i] < min_val and i in queue:
                min_val = distance[i]
                min_index = i
        return min_index

    def printPath(self, parent, j):
        if parent[j] == -1:
            print("\t\t\t\t\t\t ", j)
            return
        self.printPath(parent, parent[j])
        print("\t\t\t\t\t\t ", j)

    def printSolution(self, distance, parent):
        src = 0
        print("Vertex\t\t Distance from Source \t\t Path")
        for i in range(1, len(distance)):
            print("\n%d --> %d \t\t%d \t\t\t\t\t" % (src, i, distance[i]))
            self.printPath(parent, i)

    def dijkstra(self, graph, src):
        row = len(graph)
        col = len(graph[0])
        distance = [float("inf")] * row
        parent = [-1] * row
        distance[src] = 0
        parent[src] = -1
        queue = []
        for i in range(row):
            queue.append(i)
        while len(queue):
            u = self.min_distance(distance, queue)
            queue.remove(u)
            for j in range(col):
                if graph[u][j] and j in queue:
                    if distance[j] > graph[u][j] + distance[u]:
                        distance[j] = graph[u][j] + distance[u]
                        parent[j] = u
        self.printSolution(distance, parent)


if __name__ == '__main__':
    g = Graph()

    graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
             [4, 0, 8, 0, 0, 0, 0, 11, 0],
             [0, 8, 0, 7, 0, 4, 0, 0, 2],
             [0, 0, 7, 0, 9, 14, 0, 0, 0],
             [0, 0, 0, 9, 0, 10, 0, 0, 0],
             [0, 0, 4, 14, 10, 0, 2, 0, 0],
             [0, 0, 0, 0, 0, 2, 0, 1, 6],
             [8, 11, 0, 0, 0, 0, 1, 0, 7],
             [0, 0, 2, 0, 0, 0, 6, 7, 0]
             ]

    # Print the solution
    g.dijkstra(graph, 0)
