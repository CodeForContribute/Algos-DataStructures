class Node:
    def __init__(self, new_data):
        self.data = new_data
        self.left = None
        self.right = None


class Tree:

    def in_order_traversal(self, node):
        if node is None:
            return
        current = node
        stack = list()
        # done = 0
        while True:
            if current is not None:
                stack.append(current)
                current = current.left
            elif len(stack) > 0:
                current = stack.pop()
                print(current.data, end=" ")
                current = current.right
            else:
                break


if __name__ == '__main__':
    tree = Tree()
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    print("In order Traversal of tree")
    tree.in_order_traversal(root)
