class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def hasPathSum(root, s):
    if not root:
        return s == 0
    else:
        ans = 0
        subsum = s - root.data
        if subsum == 0 and not root.left and not root.right:
            return True
        if root.left:
            ans = ans or hasPathSum(root.left, subsum)
        if root.right:
            ans = ans or hasPathSum(root.right, subsum)
        return ans


if __name__ == '__main__':
    s = 21
    root = Node(10)
    root.left = Node(8)
    root.right = Node(2)
    root.left.right = Node(5)
    root.left.left = Node(3)
    root.right.left = Node(2)

    if hasPathSum(root, s):
        print("There is a root-to-leaf path with sum %d" % s)
    else:
        print("There is no root-to-leaf path with sum %d" % s)
