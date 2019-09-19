class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def constructBtree2BST(root):
    if not root:
        return
    