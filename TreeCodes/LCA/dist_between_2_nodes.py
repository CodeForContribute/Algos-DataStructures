class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def findDistance(root, n1, n2):
    if n1 < 0 and n2 <0 :
        return
    lca = findLca(root,n1,n2)
    d1 = findLevel(lca, n1, 0)
    d2 = findLevel(lca, n2, 0)
    return d1 + d2


def findLca(root, n1, n2):
    if not root:
        return
    if root.data == n1 or root.data == n2:
        return root
    lca_left = findLca(root.left, n1, n2)
    lca_right = findLca(root.right, n1, n2)
    if lca_left and lca_right:
        return root
    return lca_right if lca_right else lca_left


def findLevel(root, k, level):
    if not root:
        return -1
    if root.data == k:
        return level
    left = findLevel(root.left,k, level+1)
    if left == -1:
        return findLevel(root.right, k, level+1)
    return left

if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    root.right.left.right = Node(8)

    print("Dist(4,5) = ", findDistance(root, 4, 5))
    print("Dist(4,6) = ", findDistance(root, 4, 6))
    print("Dist(3,4) = ", findDistance(root, 3, 4))
    print("Dist(2,4) = ", findDistance(root, 2, 4))
    print("Dist(8,5) = ", findDistance(root, 8, 5))