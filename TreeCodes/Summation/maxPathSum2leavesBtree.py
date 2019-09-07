class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def maxPathSum(root,res):
    if not root:
        return 0
    if not root.left and not root.right:
        return root.data
    ls = maxPathSum(root.left,res)
    rs = maxPathSum(root.right,res)
    if root.left and root.right:
        res[0] = max(res[0],ls+rs+root.data)
        return max(ls, rs) + root.data
    if not root.left:
        return ls+root.data
    else:
        return rs + root.data

def maxPathSumUtil(root):
    import sys
    res = [-sys.maxsize]
    maxPathSum(root, res)
    return res[0]

if __name__ == '__main__':
    root = Node(15)
    root.left = Node(5)
    root.right = Node(6)
    root.left.left = Node(-8)
    root.left.right = Node(1)
    root.left.left.left = Node(2)
    root.left.left.right = Node(6)
    root.right.left = Node(3)
    root.right.right = Node(9)
    root.right.right.right = Node(0)
    root.right.right.right.left = Node(4)
    root.right.right.right.right = Node(-1)
    root.right.right.right.right.left = Node(10)

    print("Max pathSum of the given binary tree is", maxPathSumUtil(root))