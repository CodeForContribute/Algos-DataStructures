class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Time complexity : O(h) where h is height of given Binary Search Tree
def closestElement(root, target):
    if not root:
        return None
    if not target:
        return
    min_diff, min_diff_key = 999999999999, [-1]
    closestElementUtil(root, target, min_diff, min_diff_key)
    return min_diff_key[0]


def closestElementUtil(root, target, min_dif, min_diff_key):
    if not root:
        return
    if root.data == target:
        min_diff_key[0] = target
        return
    if min_dif > abs(root.data - target):
        min_dif = abs(root.data - target)
        min_diff_key[0] = root.data
    if target < root.data:
        closestElementUtil(root.left, target, min_dif, min_diff_key)
    else:
        closestElementUtil(root.right, target, min_dif, min_diff_key)


if __name__ == '__main__':
    root = Node(9)
    root.left = Node(4)
    root.right = Node(17)
    root.left.left = Node(3)
    root.left.right = Node(6)
    root.left.right.left = Node(5)
    root.left.right.right = Node(7)
    root.right.right = Node(22)
    root.right.right.left = Node(20)
    k = 18
    print(closestElement(root, k))
