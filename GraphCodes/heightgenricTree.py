from collections import defaultdict


def addEdge(graph, u, v):
    graph[u].append(v)
    graph[v].append(u)


####################################### Time Complexity:O(n)##################################
def buildTree(graph, arr, n):
    root_index = 0
    for i in range(n):
        if arr[i] == -1:
            root_index = i
        else:
            graph[i].append(arr[i])
            graph[arr[i]].append(i)
    return root_index


def BFS(graph, root_index):
    max_level_reached = 0
    q = []
    visited = dict()
    q.append([root_index, 0])
    while len(q):
        p = q.pop(0)
        visited[p[0]] = True
        max_level_reached = max(max_level_reached, p[1])
        for i in range(len(graph[p[0]])):
            if graph[p[0]][i] not in visited:
                q.append([graph[p[0]][i], p[1] + 1])

    return max_level_reached


################################################################################################

def fillHeight(parent, node, visited, height):
    if parent[node] == -1:
        visited[node] = 1
        return 0
    if visited[node]:
        return height[node]
    visited[node] = 1
    height[node] = 1 + fillHeight(parent, parent[node], visited, height)
    return height[node]


def findHeight(parent, n, height):
    ma = 0
    visited = [0 for i in range(n)]
    for i in range(n):
        if not visited[i]:
            height[i] = fillHeight(parent, i, visited, height)
        ma = max(ma, height[i])
    return ma


########################Time Complexity:O(n)##########################################################
if __name__ == '__main__':
    parent = [-1, 0, 1, 2, 3]
    n = len(parent)
    graph = defaultdict(list)
    root_index = buildTree(graph, parent, n)
    print(BFS(graph, root_index))
    #######################################
    # Second Method:
    height = [0 for i in range(n)]
    ma = findHeight(parent, n, height)
    print(ma)
    print(height)
