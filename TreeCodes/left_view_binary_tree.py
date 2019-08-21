class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def left_view(root):
    max_level = [0]
    left_view_util(root, 1, max_level)


def left_view_util(root, level, max_level):
    if root is None:
        return
    if max_level[0] < level:
        print(root.data, end=" ")
        max_level[0] = level

    left_view_util(root.left, level + 1, max_level)
    left_view_util(root.right, level+1, max_level)

#
# def left_view_level_order_traversal(root):
#     if root is None:
#         return
#     queue = list()
#     queue.append(root)
#     while len(queue):
#         temp = queue.pop(0)
#         print(temp.data, end=" ")
#         if temp.left is not None:
#             queue.append(temp.left)
#         if temp.right is not None:
#             queue.append(temp.right)
#         if temp.left is None or temp.right is None and len(queue)!= 0:
#             temp = queue.pop(0)
#             if temp.left is not None:
#                 queue.append(temp.left)
#             if temp.right is not None:
#                 queue.append(temp.right)


if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.right = Node(6)
    print("Left View of binary Tree is :")
    left_view(root)
    print("\n")
    print("Left View of binary Tree Using Level Order Traversal is :")
    left_view_level_order_traversal(root)
