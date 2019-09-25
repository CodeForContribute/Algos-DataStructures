def addEdge(graph, u, v):
    graph[u].append(v)
    graph[v].append(u)


############### BFS CLR Book #######################################################################
def BFSFull(graph, vertices):
    Color = ["white" for i in range(vertices)]
    distance = [0 for i in range(vertices)]
    parent = [-1 for i in range(vertices)]
    for i in range(vertices):
        if Color[i] == "white":
            BFSSingleSource(graph, i)


def BFSSingleSource(graph, v):
    q = list()
    q.append(v)
    distance[v] = 0
    Color[v] = "green"
    parent[v] = -1
    while len(q):
        p = q.pop(0)
        print(p, end=" ")
        i = 0
        while i < len(graph[p]):
            if Color[p][i] == "white":
                Color[p][i] = "green"
                distance[graph[p][i]] = distance[p] + 1
                parent[graph[p][i]] = p
                q.append(graph[p][i])
            i += 1
        Color[p] = "Dark Green"


###########################################################################################################
if __name__ == '__main__':
    n = 7
    Color = [None for i in range(n)]
    distance = [None for i in range(n)]
    parent = [None for i in range(n)]
    g = [[] for i in range(n)]

    addEdge(g, 0, 1)
    addEdge(g, 0, 2)
    addEdge(g, 1, 3)
    addEdge(g, 1, 4)
    addEdge(g, 2, 5)
    addEdge(g, 2, 6)

    BFSFull(g, n)
    print("\n")
    print(Color)
    print(distance)
    print(parent)
