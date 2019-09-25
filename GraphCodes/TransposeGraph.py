def addEdge(graph, u, v):
    graph[u].append(v)


##############################################################################################################
def transposedGraph(adj, transpose, v):
    for i in range(v):
        for j in range(len(adj[i])):
            addEdge(transpose, adj[i][j], i)


def displayGraph(transpose, v):
    for i in range(v):
        for j in range(len(transpose[i])):
            print(i, "---->", transpose[i][j], end=" ")
        print()


###############################################################################################################
if __name__ == '__main__':
    v = 5
    adj = [[] for i in range(v)]
    addEdge(adj, 0, 1)
    addEdge(adj, 0, 4)
    addEdge(adj, 0, 3)
    addEdge(adj, 2, 0)
    addEdge(adj, 3, 2)
    addEdge(adj, 4, 1)
    addEdge(adj, 4, 3)
    displayGraph(adj, v)
    transpose = [[] for i in range(v)]
    transposedGraph(adj, transpose, v)
    print("\n")
    displayGraph(transpose, v)
