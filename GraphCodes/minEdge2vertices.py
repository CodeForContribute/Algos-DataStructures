def addEdge(graph, u, v):
    graph[u].append(v)
    graph[v].append(u)


def minEdges(graph, src, dest, v):
    visited = [False for i in range(v)]
    distance = [0 for j in range(v)]
    q = []
    distance[src] = 0
    q.append(src)
    visited[src] = True
    while len(q):
        p = q.pop(0)
        for i in range(len(graph[p])):
            if not visited[graph[p][i]]:
                visited[graph[p][i]] = True
                distance[graph[p][i]] = distance[p] + 1
                q.append(graph[p][i])
    return distance[dest]


if __name__ == '__main__':
    n = 9
    edges = [[] for i in range(n)]
    addEdge(edges, 0, 1)
    addEdge(edges, 0, 7)
    addEdge(edges, 1, 7)
    addEdge(edges, 1, 2)
    addEdge(edges, 2, 3)
    addEdge(edges, 2, 5)
    addEdge(edges, 2, 8)
    addEdge(edges, 3, 4)
    addEdge(edges, 3, 5)
    addEdge(edges, 4, 5)
    addEdge(edges, 5, 6)
    addEdge(edges, 6, 7)
    addEdge(edges, 7, 8)
    u = 0
    v = 5
    print(minEdges(edges, u, v, n))
