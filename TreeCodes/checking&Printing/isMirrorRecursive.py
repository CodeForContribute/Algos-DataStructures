class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def areMirrors(root1, root2):
    if not root1 and not root2:
        return True
    if not root1 or not root2:
        return False
    return root1.data == root2.data and areMirrors(root1.left, root2.right) and areMirrors(root1.right, root2.left)

if __name__ == '__main__':
    root1 = Node(1)  # 1
    root1.left = Node(3)  # / \
    root1.right = Node(2)  # 3    2
    root1.right.left = Node(5)  # / \
    root1.right.right = Node(4)  # 5      4

    # 2nd binary tree formation
    root2 = Node(1)  # 1
    root2.left = Node(2)  # / \
    root2.right = Node(3)  # 2     3
    root2.left.left = Node(4)  # / \
    root2.left.right = Node(5)  # 4  5

    print(areMirrors(root1, root2))