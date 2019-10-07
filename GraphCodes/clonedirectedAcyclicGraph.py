class Node:
    def __init__(self, data, graph=None):
        self.data = data
        self.graph = graph


# Creating the DAG by appending adjacent edges to the vertex happens in O(1) time. Cloning of the graph takes O(E+V) time.
def printGraph(node, visited):
    if node.graph is not None:
        for neighbor in node.graph:
            if not visited[node.data]:
                print("edge %s-%s:%s-%s" % (hex(id(node)), hex(id(neighbor)), node.data, neighbor.data))
                if not visited[neighbor.data]:
                    printGraph(neighbor, visited)
                    visited[neighbor.data] = True


def cloneGraph(oldSource, newSource, visited):
    clone = None
    if not visited[oldSource.data] and oldSource.graph is not None:
        for old in oldSource.graph:
            if clone is None or (clone is not None and clone.data != old.data):
                clone = Node(old.data, [])
            newSource.graph.append(clone)
            cloneGraph(old, clone, visited)
            visited[old.data] = True
    return newSource


if __name__ == '__main__':
    n0, n1, n2 = Node(0, []), Node(1, []), Node(2, [])
    n3, n4 = Node(3, []), Node(4)
    n0.graph.append(n1)
    n0.graph.append(n2)
    n1.graph.append(n2)
    n1.graph.append(n3)
    n1.graph.append(n4)
    n2.graph.append(n3)
    n3.graph.append(n4)
    visited = [False] * 5
    print("Graph Before Cloning:-")
    printGraph(n0, visited)

    visited = [False] * 5
    print("\nCloning Process Starts")
    clonedGraphHead = cloneGraph(n0, Node(n0.data, []), visited)
    print("Cloning Process Completes.")

    visited = [False] * 5
    print("\nGraph After Cloning:-")
    printGraph(clonedGraphHead, visited)
