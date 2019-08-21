class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def in_order_traversal_without_recusrion(root):
    if root is None:
        return
    stack = []
    current = root
    while True:
        if current is not None:
            stack.append(current)
            current = current.left
        elif len(stack):
            current = stack.pop()
            print(current.data, end=" ")
            current = current.right
        else:
            break


def pre_order_traversal_without_recursion(root):
    if root is None:
        return
    stack = []
    current = root
    while True:
        if current is not None:
            print(current.data, end=" ")
            if current.right is not None:
                stack.append(current.right)
            current = current.left
        elif stack:
            current = stack.pop()
        else:
            break

#
# def post_order_traversal_without_recursion(root):
#     if root is None:
#         return
#     stack = []
#     current = root
#     while True:
#         if current is not None:
#             stack.append(current)
#             # stack.append(current.right)
#             current = current.left
#         elif stack:
#             current = stack.pop()
#             if current is not None:
#                 print(current.data, end=" ")
#             if current.right is not None:
#                 print(current.right.data, end=" ")
#             current = stack.pop()
#         else:
#             break
            # current = current.right
            # if current.right is not None:
            #     stack.append(current.right)


if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    in_order_traversal_without_recusrion(root)
    print("\n")
    pre_order_traversal_without_recursion(root)
    print("\n")
    # post_order_traversal_without_recursion(root)
