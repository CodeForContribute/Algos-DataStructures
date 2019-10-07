v = 4


def countWalks(graph, u, v, k):
    # Base Condition
    if k == 0 and u == v:
        return 1

    if k <= 0:
        return 0
    if k == 1 and graph[u][v]:
        return 1

    count = 0
    result = []
    for i in range(0, v):
        if graph[u][i]:
            result.append([u, i])
            count += countWalks(graph, i, v, k - 1)
            result.append([i, v])
        print(result)
        result.clear()
        print()

    return count


if __name__ == '__main__':
    graph = [[0, 1, 1, 1, ],
             [0, 0, 0, 1, ],
             [0, 0, 0, 1, ],
             [0, 0, 0, 0]]

    u = 0
    v = 3
    k = 2
    print(countWalks(graph, u, v, k))
