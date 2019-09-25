def addEdge(graph, u, v):
    graph[u].append(v)
    graph[v].append(u)


def printLevelNode(graph, v, node):
    level = [None] * v
    visited = [False] * v
    q = list()
    q.append(node)
    visited[node] = True
    level[node] = 0
    while len(q):
        p = q.pop(0)
        for i in range(len(graph[p])):
            if not visited[graph[p][i]]:
                q.append(graph[p][i])
                visited[graph[p][i]] = True
                level[graph[p][i]] = level[p] + 1

    for i in range(v):
        print(" ", i, '--->', level[i])


if __name__ == '__main__':
    # adjacency graph for tree
    V = 8
    graph = [[] for i in range(V)]
    graph[0].append(1)
    graph[0].append(2)
    graph[1].append(3)
    graph[1].append(4)
    graph[1].append(5)
    graph[2].append(5)
    graph[2].append(6)
    graph[6].append(7)
    # call levels function with source as 0
    printLevelNode(graph, V, 1)
