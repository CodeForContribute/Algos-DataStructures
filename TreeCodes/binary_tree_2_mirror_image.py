class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None


def mirror(root):
    if root is None:
        return
    else:
        mirror(root.left)
        mirror(root.right)
        root.left, root.right = root.right, root.left


def in_order_tree(root):
    if root is None:
        return
    in_order_tree(root.left)
    print(root.data, end=" ")
    in_order_tree(root.right)


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    """ Print inorder traversal of 
        the input tree """
    print("Inorder traversal of the",
          "constructed tree is")
    in_order_tree(root)

    """ Convert tree to its mirror """
    mirror(root)

    """ Print inorder traversal of  
        the mirror tree """
    print("\nInorder traversal of",
          "the mirror treeis ")
    in_order_tree(root)
