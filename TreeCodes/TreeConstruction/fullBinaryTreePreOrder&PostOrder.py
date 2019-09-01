"""
A tree can be constructed from the given traversals only when
one of the traversal is Inorder otherwise we can not create a binary tree.
But we can create a complete binary tree(having 2 child or 0)

"""

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def ConstructBinaryTreePrePostOrder(preOrder, PostOrder):
    pass