class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None


def isSumProperty(node):
    left_data = 0
    right_data = 0
    if node is None or (node.left is None and node.right is None):
        return True
    else:
        if node.left is not None:
            left_data = node.left.data
        if node.right is not None:
            right_data = node.right.data
        if (left_data + right_data == node.data) and isSumProperty(node.left) and isSumProperty(node.right):
            return True
        else:
            return False

if __name__ == '__main__':
    root = Node(10)
    root.left = Node(8)
    root.right = Node(2)
    root.left.left = Node(3)
    root.left.right = Node(5)
    root.right.right = Node(2)
    if isSumProperty(root):
        print("The given tree satisfies the",
              "children sum property ")
    else:
        print("The given tree does not satisfy",
              "the children sum property ")