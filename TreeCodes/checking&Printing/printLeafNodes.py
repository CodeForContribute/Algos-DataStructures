class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def printLeafNodes(root):
    if not root:
        return
    if not root.left and not root.right:
        print(root.data,end=" ")
        return
    if root.left:
        printLeafNodes(root.left)
    if root.right:
        printLeafNodes(root.right)


if __name__ == '__main__':
    root = Node(10)
    root.left = Node(8)
    root.right = Node(2)
    # root.left.left = Node(3)
    root.right.right = Node(90)
    printLeafNodes(root)
