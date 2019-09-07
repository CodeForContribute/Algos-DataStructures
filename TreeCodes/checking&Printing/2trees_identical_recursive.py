class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right= None


def isSymmetric(root1, root2):
    if not root1 and not root2:
        return True
    # if root1 or root2:
    #     return False
    if root1 and root2:
        return root1.data == root2.data and isSymmetric(root1.left, root2.left) and isSymmetric(root1.right, root2.right)
    return False

if __name__ == '__main__':
    root1 = Node(1)
    root2 = Node(1)
    root1.left = Node(2)
    root1.right = Node(3)
    root1.left.left = Node(4)
    root1.left.right = Node(5)

    root2.left = Node(2)
    root2.right = Node(3)
    root2.left.left = Node(4)
    root2.left.right = Node(5)

    if isSymmetric(root1, root2):
        print("Both trees are identical")
    else:
        print("Trees are not identical")