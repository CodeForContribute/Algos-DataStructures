class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


######################### Using 2 times Traversal ##################################################################
def findPath(root, path, k):
    if not root:
        return False
    path.append(root.data)
    if root.data == k:
        return True
    if (root.left and findPath(root.left, path, k)) or (root.right and findPath(root.right, path, k)):
        return True
    path.pop()
    return False


def findLCA(root, n1, n2):
    path1 = []
    path2 = []
    if not findPath(root, path1, n1) or not findPath(root, path2, n2):
        return -1
    i = 0
    while i < len(path1) and i < len(path2):
        if path1[i] != path2[i]:
            break
        i += 1
    return path1[i - 1]


##################### Using Single Traversal ################################################3
def findlca(root, n1, n2):
    if not root:
        return None
    if root.data == n1 or root.data == n2:
        return root.data
    left_lca = findlca(root.left, n1, n2)
    right_lca = findlca(root.right, n1, n2)
    if left_lca and right_lca:
        return root
    return left_lca if left_lca else right_lca


#################################################################################3

def findLca(root, n1, n2):
    v1 = [False]
    v2 = [False]
    lca = findLcaUtil(root, n1, n2, v1, v2)
    if (v1[0] and v2[0]) or (v1[0] and find(lca, n2)) or (find(lca, n1) and v2[0]):
        return lca
    return None


def find(root, key):
    if not root:
        return False
    if root.data == key or find(root.left, key) or find(root.right, key):
        return True
    return False


def findLcaUtil(root, n1, n2, v1, v2):
    if not root:
        return
    if root.data == n1:
        v1[0] = True
        return root
    if root.data == n2:
        v2[0] = True
        return root
    lca_left = findLcaUtil(root.left, n1, n2, v1, v2)
    lca_right = findLcaUtil(root.right, n1, n2, v1, v2)
    if lca_left and lca_right:
        return root
    return lca_right if lca_right else lca_left


if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)

    lca = findLca(root, 4, 5)

    if lca is not None:
        print("LCA(4, 5) = ", lca.data)
    else:
        print("Keys are not present")

    lca = findLca(root, 4, 10)

    if lca is not None:
        print("LCA(4,10) = ", lca.data)
    else:
        print("Keys are not present")
