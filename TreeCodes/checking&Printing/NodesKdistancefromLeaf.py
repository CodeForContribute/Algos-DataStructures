class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def kDistanceFromLeaf(node, k):
    path = [None]*100
    visited = [False]*100
    kDistantFromLeafUtil(node, path, visited, 0, k)

def kDistantFromLeafUtil(node, path, visited, path_len, k):
    if not node:
        return
    path[path_len] = node.data
    visited[path_len] = False
    path_len += 1

    if not node.left and not node.right and path_len-k-1 >= 0 and visited[path_len-k-1] is False:
        print(path[path_len-k-1],end=" ")
        visited[path_len-k-1] = True
        return
    kDistantFromLeafUtil(node.left, path, visited, path_len, k)
    kDistantFromLeafUtil(node.right, path, visited, path_len, k)
    
if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    root.right.left.right = Node(8)

    print("Nodes at distance 2 are:", end=" ")
    kDistanceFromLeaf(root, 2)