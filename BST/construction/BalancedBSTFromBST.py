class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def BalacedBSTFromBST(root):
    inorder = list()
    BalacedBSTFromBSTUtil(root, inorder)
    return BuildTree(root, inorder)


## This step will take O(n) for storing inorder traversal
def BalacedBSTFromBSTUtil(root, inorder):
    if not root:
        return
    BalacedBSTFromBSTUtil(root.left, inorder)
    inorder.append(root.data)
    BalacedBSTFromBSTUtil(root.right, inorder)


## This step will also take o(n) steps to construct the Tree
def BuildTree(root, inorder):
    n = len(inorder)
    return BuildTreeUtil(inorder, 0, n - 1)


def BuildTreeUtil(inorder, start, end):
    if start > end:
        return None
    mid = start + (end - start) // 2
    node = Node(inorder[mid])
    node.left = BuildTreeUtil(inorder, start, mid - 1)
    node.right = BuildTreeUtil(inorder, mid + 1, end)
    return node


def preorder(root):
    if not root:
        return
    print(root.data, end=" ")
    preorder(root.left)
    preorder(root.right)


if __name__ == '__main__':
    root = Node(10)
    root.left = Node(8)
    root.left.left = Node(7)
    root.left.left.left = Node(6)
    root.left.left.left.left = Node(5)
    root = BalacedBSTFromBST(root)
    print("Preorder traversal of balanced BST is :")
    preorder(root)
