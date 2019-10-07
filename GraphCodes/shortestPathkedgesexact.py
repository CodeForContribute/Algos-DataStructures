INF = float("inf")


def shortestPath(graph, u, v, k):
    """
    The worst case time complexity of the above function is O(Vk) where V is the number of vertices in the given graph.
     We can simply analyze the time complexity by drawing recursion tree.
    The worst occurs for a complete graph. In worst case, every internal node of recursion tree would have exactly V children.
    """
    V = 4
    if k == 0 and u == v:
        return 0
    if k <= 0:
        return INF
    if k == 1 and graph[u][v] != INF:
        return graph[u][v]
    result = INF
    for i in range(0, V):
        if graph[u][i] != INF and u != i and v != i:
            rec_res = shortestPath(graph, i, v, k - 1)
            if rec_res != INF:
                result = min(result, graph[u][i] + rec_res)
    return result


################# Using DP ############################################################################
def ShortestPath(graph, u, v, k):
    global V, INF
    dp = [[None] * V for i in range(V)]
    for i in range(V):
        for j in range(V):
            dp[i][j] = [None] * (k + 1)


if __name__ == '__main__':
    graph = [[0, 10, 3, 2],
             [INF, 0, INF, 7],
             [INF, INF, 0, 6],
             [INF, INF, INF, 0]]
    u = 0
    v = 3
    k = 2
    print("Weight of the shortest path is",
          shortestPath(graph, u, v, k))
