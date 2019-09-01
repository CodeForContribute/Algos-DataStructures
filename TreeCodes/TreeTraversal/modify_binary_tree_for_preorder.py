class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def modify_tree(root):
    right = root.right
    rightmost = root
    if root.left:
        rightmost = modify_tree(root.left)
        root.right = root.left
        root.left = None
    if right:
        return rightmost
    rightmost.right = right
    rightmost = modify_tree(right)
    return rightmost