class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def height(root, ans,k, lh, rh, flag):
    if not root:
        return 0
    lheight = height(root.left,ans, k,lh,rh, flag)
    rheight = height(root.right, ans, k, lh, rh, flag)
    if ans < 1+ lheight+ rheight:
        ans[0] = 1+lheight+rheight
        k[0] = root
        lh[0] = lheight
        rh[0] = rheight
    return 1 + max(lheight, rheight)

def diameter(root):
    if not root:
        return
    import sys
    ans = -sys.maxsize
    lh = [0]
    rh = [0]
    flag = [0]
    k = None
    height_tree = height(root, ans,k, lh, rh, flag)
    lPath = [None]*100
    path_len = 0
    printPathsRecur(k.left, lPath, path_len, lh, flag)
    print(k.data,end=" ")
    rpath = [None]*100
    flag = 1
    printPathsRecur(k.right, rpath, path_len, rh, flag)

def printPathsRecur(node, path,path_len, max, flag):
    if not node:
        return
    