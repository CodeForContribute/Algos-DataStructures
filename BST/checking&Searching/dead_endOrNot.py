class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def insert(root, data):
    if not root:
        return Node(data)
    if root.data > data:
        root.left = insert(root.left, data)
    if root.data < data:
        root.right = insert(root.right, data)
    return root


def isDeadEnd(root, min_val, max_val):
    if not root:
        return False
    if min_val == max_val:
        return True
    return isDeadEnd(root.left, min_val, root.data - 1) or isDeadEnd(root.right, root.data + 1, max_val)


if __name__ == '__main__':
    import sys

    INT_MIN = -sys.maxsize
    INT_MAX = sys.maxsize
    root = None
    root = insert(root, 8)
    root = insert(root, 5)
    root = insert(root, 2)
    root = insert(root, 3)
    root = insert(root, 7)
    root = insert(root, 11)
    root = insert(root, 4)
    if isDeadEnd(root, 1, 9999999999) is True:
        print("Yes")
    else:
        print("No")
