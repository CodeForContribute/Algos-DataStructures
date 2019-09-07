class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def printNodesNoSiblings(root):
    if not root:
        return
    if root.left and root.right:
        printNodesNoSiblings(root.left)
        printNodesNoSiblings(root.right)
    elif root.right:
        print(root.right.data,end=" ")
        printNodesNoSiblings(root.right)
    elif root.left:
        print(root.left.data,end=" ")
        printNodesNoSiblings(root.left)

if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.right = Node(4)
    root.right.left = Node(5)
    root.right.left.left = Node(6)
    printNodesNoSiblings(root)
