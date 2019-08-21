class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def size_tree(root):
    if root is None:
        return 0
    else:
        return 1 + size_tree(root.left) + size_tree(root.right)


if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    print("Size of the tree is %d" % (size_tree(root)))
