class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def convertBST2TsumsmallerKeys(root):
    if not root:
        return
    sum = [0]
    convertBST2TsumsmallerKeysUtil(root, sum)

def convertBST2TsumsmallerKeysUtil(root, sum):
    if not root:
        return
    convertBST2TsumsmallerKeysUtil(root.left, sum)
    sum[0] = sum[0] + root.data
    root.data = sum[0]
    convertBST2TsumsmallerKeysUtil(root.right, sum)


def printInorder(root):
    if not root:
        return
    printInorder(root.left)
    print(root.data,end=" ")
    printInorder(root.right)

if __name__ == '__main__':
    root = Node(5)
    root.left = Node(2)
    root.right = Node(13)

    print("Inorder traversal of the given tree")
    printInorder(root)

    convertBST2TsumsmallerKeys(root)
    print()
    print("Inorder traversal of the modified tree")
    printInorder(root)