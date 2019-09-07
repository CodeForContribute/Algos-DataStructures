class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def printNodesDistKgivenNode(root, target, k):
    if not root:
        return -1
    if root == target:
        printkDistanceNodeDown(root, k)
        return 0
    dl = printNodesDistKgivenNode(root.left, target, k)
    if dl != -1:
        if dl + 1 == k:
            print(root.data, end=" ")
        else:
            printkDistanceNodeDown(root.right, k - dl - 2)
        return dl + 1
    dr = printNodesDistKgivenNode(root.right, target, k)
    if dr != -1:
        if dr + 1 == k:
            print(root.data, end=" ")
        else:
            printkDistanceNodeDown(root.left, k - dr - 2)
        return 1 + dr
    return -1


def printkDistanceNodeDown(root, k):
    if not root or k < 0:
        return
    if k == 0:
        print(root.data, end=" ")
    printkDistanceNodeDown(root.left, k - 1)
    printkDistanceNodeDown(root.right, k - 1)
