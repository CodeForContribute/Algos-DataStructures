class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def removeBSTskeys(root, low, high):
    # if not root:
    #     return
    if low > high:
        return
    if not root:
        return None
    root.left = removeBSTskeys(root.left, low, high)
    root.right = removeBSTskeys(root.right, low, high)
    if root.data < low:
        rightChild = root.right
        del root
        return rightChild
    if root.data > high:
        lchild = root.left
        del root
        return lchild
    return root


def insert(root, key):
    if root is None:
        return Node(key)
    if root.data > key:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    return root


# Utility function to traverse the binary
# tree after conversion
def inorderTraversal(root):
    if root:
        inorderTraversal(root.left)
        print(root.data, end=" ")
        inorderTraversal(root.right)

    # Driver Code


if __name__ == '__main__':
    root = None
    root = insert(root, 6)
    root = insert(root, -13)
    root = insert(root, 14)
    root = insert(root, -8)
    root = insert(root, 15)
    root = insert(root, 13)
    root = insert(root, 7)
    print("Inorder traversal of the given tree is:",
          end=" ")
    inorderTraversal(root)

    root = removeBSTskeys(root, -10, 13)
    print()
    print("Inorder traversal of the modified tree is:",
          end=" ")
    inorderTraversal(root)
