class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def insert(root, data):
    if not root:
        return Node(data)
    if root.data < data:
        root.right = insert(root.right, data)
    if root.data > data:
        root.left = insert(root.left, data)
    return root


def inorder(root):
    if not root:
        return
    inorder(root.left)
    print(root.data, end=" ")
    inorder(root.right)


def leafDelete(root):
    if not root:
        return
    if not root.left and not root.right:
        del root
        return None
    root.left = leafDelete(root.left)
    root.right = leafDelete(root.right)
    return root


if __name__ == '__main__':
    root = None
    root = insert(root, 20)
    insert(root, 10)
    insert(root, 5)
    insert(root, 15)
    insert(root, 30)
    insert(root, 25)
    insert(root, 35)
    print("Inorder before Deleting the leaf Node.")
    inorder(root)
    leafDelete(root)
    print()
    print("INorder after Deleting the leaf Node.")
    inorder(root)
