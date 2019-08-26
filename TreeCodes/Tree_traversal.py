class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

#######################################################################################################################
def in_order_tree(root):
    if root is None:
        return
    in_order_tree(root.left)
    print(root.data, end=" ")
    in_order_tree(root.right)

#######################################################################################################################
def pre_order_tree(root):
    if root is None:
        return
    print(root.data, end=" ")
    pre_order_tree(root.left)
    pre_order_tree(root.right)

#######################################################################################################################
def post_order_tree(root):
    if root is None:
        return
    post_order_tree(root.left)
    post_order_tree(root.right)
    print(root.data, end=" ")
#######################################################################################################################

if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    print("Preorder traversal of binary tree is")
    pre_order_tree(root)

    print("\nInorder traversal of binary tree is")
    in_order_tree(root)

    print("\nPostorder traversal of binary tree is")
    post_order_tree(root)

