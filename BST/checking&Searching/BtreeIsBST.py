class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

## Simple and wrong
def isBtreeBST(root):
    if not root:
        return True
    if root.left and root.left.data > root.data:
        return False
    if root.right and root.right.data < root.data:
        return False
    if not isBtreeBST(root.left) or not isBtreeBST(root.right):
        return False
    return True

#Correct but not efficient
def isBST(root):
    if not root:
        return True
    if root.left and maxValue(root.left) > root.data:
        return False
    if root.right and minValue(root.right) < root.data:
        return False
    if not isBST(root.left) or not isBST(root.right):
        return False
    return True

def maxValue(root):
    if not root:
        return
    current = root
    while current.right:
        current = current.right
    return current.data

def minValue(root):
    if not root:
        return
    current = root
    while current.left:
        current = current.left
    return current.data

#### Correct & Efficient
# import sys
# INT_MIN = -sys.maxsize
# INT_MAX = sys.maxsize
#
# def isBSTUtil(root, min, max):
#     if not root:
#         return True
#     if root.data < min or root.data > max:
#         return False
#     return isBSTUtil(root.left, min, root.data - 1) and isBSTUtil(root.right, root.data + 1, max)
#
# def BST(root):
#     # if not root:
#     #     return
#     return isBSTUtil(root, INT_MIN, INT_MIN)

def isBSTBtree(root, l = None, r = None):
    if not root:
        return True
    if l and root.data <= l.data:
        return False
    if r and root.data >= r.data:
        return False
    return isBSTBtree(root.left, l, root) and isBSTBtree(root.right, root, r)
# Using Level Order Traversal
def inorderTraversal(root):
    if not root:
        return
    inorder  = []
    stack = []
    stack.append(root)
    root = stack.pop()
    while len(stack) or root:
        while root:
            stack.append(root)
            root = root.left
        root = stack.pop()
        inorder.append(root.data)
        root = root.right
    return inorder



if __name__ == '__main__':
    root = Node(3)
    root.left = Node(2)
    root.right = Node(5)
    # root.right.left = Node(1)
    # root.right.right = Node(4)
    # root.right.left.left = Node(40)
    print(isBSTBtree(root))
    a = (inorderTraversal(root))
