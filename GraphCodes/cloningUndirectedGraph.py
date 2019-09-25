from collections import defaultdict


class GraphNode:
    def __init__(self, data):
        self.data = data
        self.neighbors = []


def CloneGraph(src):
    hash_map = dict()
    q = list()
    q.append(src)
    node = GraphNode(src.data)
    hash_map[src] = node
    while len(q):
        p = q.pop(0)
        neighbor = p.neighbors
        n = len(neighbor)
        for i in range(n):
            if neighbor[i] not in hash_map:
                node = GraphNode(neighbor[i].data)
                hash_map[neighbor[i]] = node
                q.append(neighbor[i])
            hash_map[p].neighbors.append(hash_map[neighbor[i]])

    return hash_map[src]


def BFS(src):
    q = []
    visited = defaultdict()
    q.append(src)
    visited[src] = True
    while len(q):
        p = q.pop(0)
        print(p.data, end=" ")
        v = p.neighbors
        n = len(v)
        for i in range(n):
            if v[i] not in visited:
                visited[v[i]] = True
                q.append(v[i])


def buildGraph():
    node1 = GraphNode(1)
    node2 = GraphNode(2)
    node3 = GraphNode(3)
    node4 = GraphNode(4)

    node1.neighbors.append(node2)
    node1.neighbors.append(node4)

    node2.neighbors.append(node1)
    node2.neighbors.append(node3)

    node3.neighbors.append(node2)
    node3.neighbors.append(node4)

    node4.neighbors.append(node1)
    node4.neighbors.append(node3)
    return node1


if __name__ == '__main__':
    src = buildGraph()
    print("BFS Traversal of Original Graph")
    BFS(src)
    print("\n BFS Traversal of Cloned Graph")
    src = CloneGraph(src)
    BFS(src)
