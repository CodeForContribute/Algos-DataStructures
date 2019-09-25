def addEdge(graph, u, v):
    graph[u].append(v)


def printPath(path):
    for i in range(len(path)):
        print(path[i], end=" ")


def isNotVisited(item, path):
    if item in path:
        return True
    return False


def findPaths(graph, src, dest):
    q = []
    path = list()
    path.append(src)
    q.append(path)
    while len(q):
        path = q.pop(0)
        last = path[-1]
        if last == dest:
            printPath(path)
        for i in range(len(graph[last])):
            if isNotVisited(graph[last][i], path):
                # new_path = [None]*len(path)
                path.append(graph[last][i])
                q.append(path)


if __name__ == '__main__':
    v = 4
    graph = [[] for i in range(v)]
    addEdge(graph, 0, 3)
    addEdge(graph, 0, 1)
    addEdge(graph, 0, 2)
    addEdge(graph, 2, 3)
    addEdge(graph, 2, 0)
    addEdge(graph, 2, 1)
    src = 2
    dest = 3
    findPaths(graph, src, dest)
