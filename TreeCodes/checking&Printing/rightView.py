class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def rightViewUtil(root, level, max_level):
    if not root:
        return
    if max_level[0] < level:
        print(root.data,end=" ")
        max_level[0] = level
    rightViewUtil(root.right, level+1, max_level)
    rightViewUtil(root.left, level+1, max_level)


def rightView(root):
    max_level = [0]
    rightViewUtil(root, 1, max_level)

if __name__ == '__main__':
    root = Node(12)
    root.left = Node(10)
    root.right = Node(20)
    root.right.left = Node(25)
    root.right.right = Node(40)
    rightView(root)