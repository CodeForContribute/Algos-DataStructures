class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def Inorder(root):
    if not root:
        return
    Inorder(root.left)
    print(root.data, end=" ")
    Inorder(root.right)


def constructBtreeBST(root):
    if not root:
        return
    sum = [0]
    return constructBtreeBSTUtil(root, sum)


def constructBtreeBSTUtil(root, sum):
    if not root:
        return
    constructBtreeBSTUtil(root.right, sum)
    sum[0] += root.data
    root.data = sum[0]
    constructBtreeBSTUtil(root.left, sum)
    # if not root:
    #     return 0
    # sum[0]  += constructBtreeBSTUtil(root.right, sum)
    # root.data += sum[0]
    # sum[0] = root.data
    # sum[0] += constructBtreeBSTUtil(root.left,sum)
    # return sum[0]


if __name__ == '__main__':
    root = Node(5)
    root.left = Node(2)
    root.right = Node(13)

    print("Inorder traversal of the given tree")
    Inorder(root)

    constructBtreeBST(root)
    print()
    print("Inorder traversal of the modified tree")
    Inorder(root)
