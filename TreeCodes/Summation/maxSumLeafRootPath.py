class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def maxSumLeafRootPAth(root):
    if not root:
        return 0
    target_leaf_ref = [None]
    import sys
    max_sum = [-sys.maxsize]
    getTargetLeaf(root, max_sum, 0, target_leaf_ref)
    printPath(root, target_leaf_ref)
    return max_sum[0]

def getTargetLeaf(root, max_sum, current_sum, target_leaf_ref):
    if not root:
        return
    current_sum += root.data
    if not root.left and not root.right:
        if current_sum > max_sum[0]:
            max_sum[0] = current_sum
            target_leaf_ref[0] = root
    getTargetLeaf(root.left, max_sum, current_sum, target_leaf_ref)
    getTargetLeaf(root.right, max_sum, current_sum,target_leaf_ref)


def printPath(root, target_leaf_ref):
    if not root:
        return False
    if root == target_leaf_ref[0] or printPath(root.left, target_leaf_ref) or printPath(root.right, target_leaf_ref):
        print(root.data,end=" ")
        return True
    return False

if __name__ == '__main__':
    root = Node(10)
    root.left = Node(-2)
    root.right = Node(7)
    root.left.left = Node(8)
    root.left.right = Node(-4)
    sum = maxSumLeafRootPAth(root)
    print("\n")
    print(sum)

