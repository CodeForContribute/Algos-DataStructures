class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def isBinaryTreeRec(root):
    if not root:
        return True
    if not root.left and not root.right:
        return True
    # if (root.left and not root.right) or (not root.left and root.right):
    #     return False
    if root.left and root.right:
        return isBinaryTreeRec(root.left) and isBinaryTreeRec(root.right)
    return False

if __name__ == '__main__':
    root = Node(10)
    root.left = Node(20)
    root.right = Node(30)

    root.left.left = Node(40)
    root.left.right = Node(50)
    root.right.left = Node(60)
    root.right.right = Node(70)

    if isBinaryTreeRec(root):
        print("Yes")
    else:
        print("No") 