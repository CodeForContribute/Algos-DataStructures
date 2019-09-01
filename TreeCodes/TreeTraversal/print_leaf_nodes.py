class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def print_leaf_nodes(root):
    if not root:
        return
    if not root.left and not root.right:
        print(root.data, end=" ")
    if root.right:
        print_leaf_nodes(root.right)
    if root.left:
        print_leaf_nodes(root.left)

def print_leaf_nodes_right_to_left(root):
    if not root:
        return
    stack = list()
    while True:
        if root:
            stack.append(root)
            root = root.right
        else:
            if len(stack) == 0:
                break
            else:
                root = stack.pop()
                if root.left is None:
                    print(root.data, end=" ")
                # temp = stack.pop()
                while stack[-1].left:
                    root = stack.pop()
                    if not len(stack):
                        break
                if len(stack):
                    root = stack.pop().left
                else:
                    root = None







if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    # root.left.right.left = Node(4)
    # root.left.right.right = Node(7)
    root.right.right = Node(7)
    root.right.left = Node(6)
    print_leaf_nodes(root)
