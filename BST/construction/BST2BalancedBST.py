import sys
import math

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def storeInorder(root, inorder):
    if not root:
        return
    storeInorder(root.left, inorder)
    inorder.append(root)
    storeInorder(root.right, inorder)

def BST2BalancedBSTUtil(inorder, start, end):
    if start > end:
        return None
    mid = (start + end)//2
    root = inorder[mid]
    root.left = BST2BalancedBSTUtil(inorder, start, mid-1)
    root.right = BST2BalancedBSTUtil(inorder, mid+1, end)
    return root


def BST2BalancedBST(root):
    if not root:
        return
    inorder = list()
    storeInorder(root, inorder)
    return  BST2BalancedBSTUtil(inorder, 0, len(inorder)-1)



def preOrder(root):
    if not root:
        return
    print(root.data,end=" ")
    preOrder(root.left)
    preOrder(root.right)



if __name__ == '__main__':
    root = Node(10)
    root.left = Node(8)
    root.left.left = Node(7)
    root.left.left.left = Node(6)
    root.left.left.left.left = Node(5)
    root = BST2BalancedBST(root)
    print("Preorder traversal of balanced BST is :")
    preOrder(root)


