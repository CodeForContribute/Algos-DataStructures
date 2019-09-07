class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def printMiddleLevel(root):
    printMiddleLevelUtil(root, root)


def printMiddleLevelUtil(root1, root2):
    if not root1 or not root2:
        return
    if not root2.left and not root2.right:
        print(root1.data, end=" ")
        return
    printMiddleLevelUtil(root1.left, root2.left.left)
    printMiddleLevelUtil(root1.right, root2.left.left)


if __name__ == '__main__':
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n5 = Node(5)
    n6 = Node(6)
    n7 = Node(7)
    n2.left = n4
    n2.right = n5
    n3.left = n6
    n3.right = n7
    n1.left = n2
    n1.right = n3
    printMiddleLevel(n1)
