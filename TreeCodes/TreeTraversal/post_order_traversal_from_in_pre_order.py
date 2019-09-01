class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

#######################################################################################################################
def post_order(inorder, preorder, n):
    if preorder[0] in inorder:
        root = inorder.index(preorder[0])
    if root != 0:
        post_order(inorder[:root], preorder[1:root + 1], len(inorder[:root]))
    if root != n - 1:
        post_order(inorder[root + 1:], preorder[root + 1:], len(inorder[root + 1:]))
    print(preorder[0], end=" ")

#######################################################################################################################
if __name__ == '__main__':
    inorder = [4, 2, 5, 1, 3, 6]
    preorder = [1, 2, 4, 5, 3, 6]
    n = len(inorder)
    post_order(inorder, preorder, n)
