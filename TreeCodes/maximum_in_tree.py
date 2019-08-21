import sys


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def find_max(root):
    if root is None:
        return sys.maxsize
    result = root.data
    lres = find_max(root.left)
    rres = find_max(root.right)
    if lres < result:
        result = lres
    if rres < result:
        result = rres
    return result


if __name__ == '__main__':
    root = Node(2)
    root.left = Node(7)
    root.right = Node(5)
    root.left.right = Node(6)
    root.left.right.left = Node(1)
    root.left.right.right = Node(11)
    root.right.right = Node(9)
    root.right.right.left = Node(4)

    print("Maximum element is",
          find_max(root))
