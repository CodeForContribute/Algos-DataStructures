class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


INT_MIN = -2147483648
INT_MAX = 2147483647


# Time Complexity : O(n)
def largestBST(root):
    if not root:
        return 0, INT_MIN, INT_MAX, 0, True
    if not root.left and not root.right:
        return 1, root.data, root.data, 1, True
    l = largestBST(root.left)
    r = largestBST(root.right)
    ret = [0, 0, 0, 0, 0]
    ret[0] = (1 + l[0] + r[0])
    if l[4] and r[4] and l[1] < root.data < r[2]:
        ret[2] = min(l[2], min(r[2], root.data))
        ret[1] = max(r[1], max(l[1], root.data))
        ret[3] = ret[0]
        ret[4] = True
        return ret
    ret[3] = max(l[3], r[3])
    ret[4] = False

    return ret


if __name__ == '__main__':
    """Let us construct the following Tree 
        60  
        / \  
        65 70  
    /  
    50 """
    root = Node(60)
    root.left = Node(65)
    root.right = Node(70)
    root.left.left = Node(50)
    print("Size of the largest BST is",
          largestBST(root)[3])
