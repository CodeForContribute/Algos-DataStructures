class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class Tree:

    def print_in_order(self, root):
        if root is not None:
            self.print_in_order(root.left)
            print(root.data, end=" ")
            self.print_in_order(root.right)

    def print_post_order(self, root):
        if root is not None:
            self.print_post_order(root.left)
            self.print_post_order(root.right)
            print(root.data, end=" ")

    def print_pre_order(self, root):
        if root is not None:
            print(root.data, end=" ")
            self.print_pre_order(root.left)
            self.print_pre_order(root.right)


if __name__ == '__main__':
    t = Tree()
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    print("PreOrder Traversal of binary tree is:")
    t.print_pre_order(root)
    print("\n")
    print("PostOrder Traversal of binary tree is:")
    t.print_post_order(root)
    print("\n")
    print("InOrder Traversal of binary tree is:")
    t.print_in_order(root)
