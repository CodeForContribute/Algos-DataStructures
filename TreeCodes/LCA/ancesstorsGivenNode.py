class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def ancesstorsNode(root, target):
    if not root:
        return False
    if not target:
        return False
    if root.data == target:
        return True
    if ancesstorsNode(root.left, target) or ancesstorsNode(root.right, target):
        print(root.data,end=" ")
        return True
    return False

if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)

    x = 7
    ancesstorsNode(root, x)