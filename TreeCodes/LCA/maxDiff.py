import sys


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def maxDiff(root):
    res = [-sys.maxsize]
    maxDiffUtil(root, res)
    return res[0]

def maxDiffUtil(root, res):
    if not root:
        return sys.maxsize
    if not root.left and not root.right:
        return root.data
    val = min(maxDiffUtil(root.left, res), maxDiffUtil(root.right, res))
    res[0] = max(val, root.data-val)
    return min(val, res[0])

if __name__ == '__main__':
    root = Node(8)
    root.left = Node(3)

    root.left.left = Node(1)
    root.left.right = Node(6)
    root.left.right.left = Node(4)
    root.left.right.right = Node(7)

    root.right = Node(10)
    root.right.right = Node(14)
    root.right.right.left = Node(13)
    print("Maximum difference between a node and",
          "its ancestor is :", maxDiff(root))
