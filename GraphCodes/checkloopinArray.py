def isCyclerecursion(i, graph, visited, recur):
    visited[i] = True
    recur[i] = True
    for v in graph[i]:
        if not visited[v]:
            if isCyclerecursion(v, graph, visited, recur):
                return True
        elif visited[v] and recur[v]:
            return True
    recur[i] = False
    return False


def isCycle(arr, n):
    if not arr:
        return
    if n < 0:
        return
    graph = [[] for row in range(n)]
    for i in range(n):
        if i != (i + arr[i] + n) % n:
            graph[i].append((i + arr[i] + n) % n)
    print(graph)
    visited = [False for i in range(n)]
    recur = [False for i in range(n)]
    for i in range(n):
        if not visited[i]:
            if isCyclerecursion(i, graph, visited, recur):
                return True
    return False


if __name__ == '__main__':

    arr = [1, 2]
    n = len(arr)
    if isCycle(arr, n):
        print("Yes")
    else:
        print("No")
