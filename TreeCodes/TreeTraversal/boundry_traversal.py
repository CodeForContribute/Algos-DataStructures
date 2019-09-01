class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def print_leaves(root):
    if root:
        print_leaves(root.left)
        if root.left is None and root.right is None:
            print(root.data)
        print_leaves(root.right)

def boundryLeft(root):
    if root:
        if root.left:
            print(root.data,end=" ")
            boundryLeft(root.left)
        elif root.right:
            print(root.data, end=" ")
            boundryLeft(root.right)

def boundryRight(root):
    if root:
        if root.right:
            boundryRight(root.right)
            print(root.data)
        elif root.left:
            boundryRight(root.left)
            print(root.data)

def BoundryTraversalTree(root):
    if not root:
        return
    if root:
        print(root.data, end=" ")
        boundryLeft(root.left)
        print_leaves(root.left)
        print_leaves(root.right)
        boundryRight(root.right)

if __name__ == '__main__':
    root = Node(20)
    root.left = Node(8)
    root.left.left = Node(4)
    root.left.right = Node(12)
    root.left.right.left = Node(10)
    root.left.right.right = Node(14)
    root.right = Node(22)
    root.right.right = Node(25)
    BoundryTraversalTree(root)