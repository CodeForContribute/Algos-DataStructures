class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

#
def maxDepthSum(root, sum, level,max_level):
    if not root:
        return
    if level > max_level[0]:
        sum[0] = root.data
        max_level[0] = level
    elif level == max_level[0]:
        sum[0] += root.data
    maxDepthSum(root.left,sum, level+1, max_level)
    maxDepthSum(root.right,sum,level+1, max_level)

def getMaxDepth(root):
    if not root:
        return 0
    return 1+max(getMaxDepth(root.left), getMaxDepth(root.right))

def sumMaxLevel(root):
    max_depth = getMaxDepth(root)
    return sumMaxLevelUtil(root, max_depth)

def sumMaxLevelUtil(root, max_depth):
    if not root:
        return 0
    if max_depth == 1:
        return root.data
    return sumMaxLevelUtil(root.left, max_depth-1)+sumMaxLevelUtil(root.right, max_depth-1)

if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    # print(getMaxDepth(root))
    # print(sumMaxLevel(root))
    sum = [0]
    import sys
    max_level = [-sys.maxsize]
    level = 0
    maxDepthSum(root,sum,level,max_level)
    print(sum[0])
