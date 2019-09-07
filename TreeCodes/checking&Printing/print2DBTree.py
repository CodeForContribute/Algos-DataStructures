COUNT = [10]
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def print2DUtil(root, space):
    if not root:
        return
    space += COUNT[0]
    print2DUtil(root.right, space)
    print()
    for i in range(COUNT[0], space):
        print(end=" ")
    print(root.data)
    print2DUtil(root.left, space)

def print2D(root):
    print2DUtil(root, 0)


if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)

    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)

    root.left.left.left = Node(8)
    root.left.left.right = Node(9)
    root.left.right.left = Node(10)
    root.left.right.right = Node(11)
    root.right.left.left = Node(12)
    root.right.left.right = Node(13)
    root.right.right.left = Node(14)
    root.right.right.right = Node(15)

    print2D(root) 