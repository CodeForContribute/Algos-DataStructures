class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def insert(root, node):
    if not root:
        return node
    if root.data < node.data:
        root.right = insert(root.right, node)
    if root.data > node.data:
        root.left = insert(root.left, node)
    return root


def inorder(root):
    if not root:
        return
    inorder(root.left)
    print(root.data,end=" ")
    inorder(root.right)


def preorder(root):
    if not root:
        return
    print(root.data,end=" ")
    preorder(root.left)
    preorder(root.right)


def PostOrder(root):
    if not root:
        return
    PostOrder(root.right)
    PostOrder(root.left)
    print(root.data,end=" ")


if __name__ == '__main__':
    r = Node(50)
    insert(r, Node(30))
    insert(r, Node(20))
    insert(r, Node(40))
    insert(r, Node(70))
    insert(r, Node(60))
    insert(r, Node(80))
    print("\nInorder Traversal BST")
    inorder(r)
    print("\nPreOrder Traversal BST")
    preorder(r)
    print("\nPostorder Traversal BST")
    PostOrder(r)

