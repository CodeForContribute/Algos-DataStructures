class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def delteLeafNodes(root):
    if not root:
        return
    suc = None
    if root.left:
        root = delteLeafNodes(root)
    if root.right:
        root = delteLeafNodes(root)
    if not root.left and not root.right:
        del root
        root = suc
    return root