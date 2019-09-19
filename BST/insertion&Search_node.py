class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def search(root, data):
    if not root:
        return root
    if root.data == data:
        return root
    if root.data < data:
        return search(root.left, data)
    else:
        return search(root.right, data)

def insert(root, node):
    if not root:
        return node
    if node.data < root.data:
        root.left = insert(root.left, node)
    elif node.data > root.data:
        root.right = insert(root.right, node)
    return root

# def insert(root, node):
#     if not root:
#         root = node
#     if root.data < node.data:
#         if not root.right:
#             root.right = node
#         else:
#             insert(root.right,node)
#     else:
#         if not root.left:
#             root.left = node
#         else:
#             insert(root.left, node)


def inorder(root):
    if not root:
        return
    inorder(root.left)
    print(root.data,end=" ")
    inorder(root.right)


if __name__ == '__main__':
    r = Node(50)
    insert(r, Node(30))
    insert(r, Node(20))
    insert(r, Node(40))
    insert(r, Node(70))
    insert(r, Node(60))
    insert(r, Node(80))
    inorder(r)
