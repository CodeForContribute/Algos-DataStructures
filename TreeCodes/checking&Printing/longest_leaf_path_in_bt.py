class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def height(root, ans,k, lh, rh, flag):
    if not root:
        return 0
    lheight = height(root.left)
    rheight = height(root.right)
    if lheight > rheight:
        return lheight+1
    else:
        return rheight+1


def diameter(root):
    if not root:
        return
    import sys
    ans = -sys.maxsize
    lh = 0 # to store the left subtree height
    rh = 0 # to store the right subtree height
    flag = False# flag helping in printing left and right subtree
    k  = None
    height_tree  = height(root, ans, k, lh, rh,flag)
    