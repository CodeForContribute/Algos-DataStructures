"""
    This solution is not efficient as it takes O(n^2) time complexity in worst case , at least O(w*n)
    where w is the width of binary tree and n is number of nodes in tree
    The efficient solution uses Hash concepts solution can be found under Hash Package with O(n) time Complexity .
"""


class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None


def find_min_max(node, minimum, maximum, hd):
    if node is None:
        return
    if hd < minimum[0]:
        minimum[0] = hd
    elif hd > maximum[0]:
        maximum[0] = hd
    find_min_max(node.left, minimum, maximum, hd - 1)
    find_min_max(node.right, minimum, maximum, hd + 1)


def print_vertical_line(node, line_no, hd):
    if node is None:
        return
    if hd == line_no:
        print(node.data, end=" ")
    print_vertical_line(node.left, line_no, hd - 1)
    print_vertical_line(node.right, line_no, hd + 1)


def vertical_order(root):
    minimum = [0]  # Distance from root node from itself
    maximum = [0]  # Max distance of root node from itself
    find_min_max(root, minimum, maximum, 0)  # it will give min and max distance of nodes from root
    for line_no in range(minimum[0], maximum[0] + 1):
        print_vertical_line(root, line_no, 0)
        print(" ")


if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    root.right.left.right = Node(8)
    root.right.right.right = Node(9)

    print("Vertical order traversal is")
    vertical_order(root)
