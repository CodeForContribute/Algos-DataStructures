class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def DiagonalTraversal(root):
    if not root:
        return
    diagonal_print_map = dict()
    diagonalPrintUtil(root, 0, diagonal_print_map)


def diagonalPrintUtil(root,d, diagonal_print_map):
    pass