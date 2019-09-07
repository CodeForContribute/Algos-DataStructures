class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def printRoute(stack ,root):
    if not root:
        return
    stack.append(root.data)
    if not root.left and not root.right:
        print(" ".join([str(i) for i in stack]))
    printRoute(stack, root.left)
    printRoute(stack, root.right)
    stack.pop()

if __name__ == '__main__':
    root = Node(10)
    root.left = Node(8)
    root.right = Node(2)
    root.left.left = Node(3)
    root.left.right = Node(5)
    root.right.left = Node(2)
    stack = list()
    printRoute(stack, root)