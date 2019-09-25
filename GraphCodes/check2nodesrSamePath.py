# Time complexity is :O(n) for pre-processing and O(1) for query
def dfs(graph, vertex):
    global intime, Outtime, MAX, timer, visited
    visited[vertex] = True
    timer += 1
    intime[vertex] = timer
    i = 0
    while i < len(graph[vertex]):
        if not visited[graph[vertex][i]]:
            dfs(graph, graph[vertex][i])
        i += 1
    timer += 1
    Outtime[vertex] = timer


# Time Complexity:O(1)
def Query(u, v):
    global intime, Outtime, visited, MAX, timer, visited
    return (intime[u] < intime[v] and Outtime[u] > Outtime[v]) or (intime[v] < intime[u] and Outtime[v] > Outtime[u])


if __name__ == '__main__':
    MAX = 100001
    visited = [False for i in range(MAX)]
    intime = [0 for i in range(MAX)]
    Outtime = [0 for j in range(MAX)]
    timer = 0
    n = 9
    graph = [[] for i in range(n + 1)]
    graph[1].append(2)
    graph[1].append(3)
    graph[3].append(6)
    graph[2].append(4)
    graph[2].append(5)
    graph[5].append(7)
    graph[5].append(8)
    graph[5].append(9)

    # Start dfs (here root node is 1)
    dfs(graph, 1)
    print(Query(3, 6))
    print(Query(5, 9))
    print(Query(1, 6))
    print(Query(5, 4))
