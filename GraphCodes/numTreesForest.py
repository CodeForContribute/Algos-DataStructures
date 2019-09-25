# Time Complexity:O(V+E)
def addEdge(graph, u, v):
    graph[u].append(v)
    graph[v].append(u)


#####################################################################################################################
def DFSUtil(graph, vertex, visited):
    visited[vertex] = True
    for i in range(len(graph[vertex])):
        if not visited[graph[vertex][i]]:
            DFSUtil(graph, graph[vertex][i], visited)


def countTrees(graph, v):
    visited = [False for i in range(v)]
    # visited[vertex] = True
    res = 0
    for u in range(v):
        if not visited[u]:
            DFSUtil(graph, u, visited)
            res += 1
    return res


######################################################################################################################
if __name__ == '__main__':
    V = 5
    adj = [[] for i in range(V)]
    addEdge(adj, 0, 1)
    addEdge(adj, 0, 2)
    addEdge(adj, 3, 4)
    print(countTrees(adj, V))
