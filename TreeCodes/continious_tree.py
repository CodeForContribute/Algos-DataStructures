"""
A tree is Continuous tree if in each root to leaf path, absolute difference between keys of two adjacent is 1. We are given a binary tree, we need to check if tree is continuous or not.

Examples:

Input :              3
                    / \
                   2   4
                  / \   \
                 1   3   5
Output: "Yes"

// 3->2->1 every two adjacent node's absolute difference is 1
// 3->2->3 every two adjacent node's absolute difference is 1
// 3->4->5 every two adjacent node's absolute difference is 1

Input :              7
                    / \
                   5   8
                  / \   \
                 6   4   10
Output: "No"

// 7->5->6 here absolute difference of 7 and 5 is not 1.
// 7->5->4 here absolute difference of 7 and 5 is not 1.
// 7->8->10 here absolute difference of 8 and 10 is not 1.
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def in_order(root):
    if root is None:
        return
    in_order(root.left)
    print(root.data, end=" ")
    in_order(root.right)


def is_continious_tree(root):
    if root is None:
        return True
    if root.left is None and root.right is None:
        return True
    if root.left is None:
        return abs(root.data - root.right.data) == 1 and is_continious_tree(root.right)
    if root.right is None:
        return abs(root.data - root.right.data) == 1 and is_continious_tree(root.left)
    return abs(root.data - root.left.data) == 1 and abs(root.data - root.right.data) and is_continious_tree(root.left) \
           and is_continious_tree(root.right)


if __name__ == '__main__':
    root = Node(3)
    # root.left = Node(2)
    root.right = Node(4)
    root.right.left = Node(1)
    root.right.right = Node(3)
    # root = Node(3)
    print("Inorder Traversal of tree")
    in_order(root)
    print("\n")
    print(is_continious_tree(root))
