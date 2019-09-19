class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def transformTree(root):
    sum = [0]
    transformTreeUtil(root, sum)


def transformTreeUtil(root, sum):
    if not root:
        return
    transformTreeUtil(root.right, sum)
    sum[0] = sum[0] + root.data
    root.data = sum[0] - root.data
    transformTreeUtil(root.left, sum)


def printInorder(root):
    if not root:
        return
    printInorder(root.left)
    print(root.data, end=" ")
    printInorder(root.right)


if __name__ == '__main__':
    root = Node(11)
    root.left = Node(2)
    root.right = Node(29)
    root.left.left = Node(1)
    root.left.right = Node(7)
    root.right.left = Node(15)
    root.right.right = Node(40)
    root.right.right.left = Node(35)
    print("Inorder Traversal of given tree\n")
    printInorder(root)
    transformTree(root)
    print("\n\nInorder Traversal of transformed tree\n")
    printInorder(root) 

