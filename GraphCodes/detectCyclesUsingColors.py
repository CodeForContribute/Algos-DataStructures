from collections import defaultdict


class Graph:
    def __init__(self, v):
        self.v = v
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def isCycleInDirected(self, node, Color, result):
        Color[node] = "grey"
        result.append(str(node) + '->')

        for neighbor in self.graph[node]:
            if Color[neighbor] == "grey":
                # result.append('->')
                result.append(str(neighbor))
                return True

            if Color[neighbor] == "white":
                # result.append('->')
                result.append(neighbor)
                return self.isCycleInDirected(neighbor, Color, result)
                # return True

        Color[node] = 'black'
        result.clear()
        return False

    def isCyclic(self):
        Color = ["white" for i in range(self.v)]
        result = []
        count = 0
        for i in range(self.v):
            if Color[i] == "white":
                if self.isCycleInDirected(i, Color, result):
                    print(result)
                    result.clear()
                    count += 1
        return count


if __name__ == '__main__':
    g = Graph(4)
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    # g.addEdge(2, 1)

    g.addEdge(2, 3)
    g.addEdge(3, 3)
    count = g.isCyclic()
    print(count)
