###################################In Complete #####################################################################
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def modified_level_order_traversal(root):
    if root is None:
        return
    if root.left is None and root.right is None:
        print(root.data, end=" ")
        return
    right_to_left = False
    count = 0
    stack = list()
    queue = list()
    queue.append(root)
    while len(queue):
        count += 1
        while len(queue):
            temp = queue.pop(0)
            if right_to_left is False:
                print(temp.data, end=" ")
            else:
                stack.append(temp)
            if temp.left is not None:
                queue.append(temp.left)
            if temp.right is not None:
                queue.append(temp.right)
        # print("\n")

        if right_to_left is True:
            while len(stack):
                item = stack.pop()
                print(item.data, end=" ")
        # print("\n")

        if count == 2:
            right_to_left = ~right_to_left
            count = 0
        print("\n")

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
    root.left.right.left = Node(3)
    root.left.right.right = Node(1)
    root.right.left.left = Node(4)
    root.right.left.right = Node(2)
    root.right.right.left = Node(7)
    root.right.right.right = Node(2)
    root.left.right.left.left = Node(16)
    root.left.right.left.right = Node(17)
    root.right.left.right.left = Node(18)
    root.right.right.left.right = Node(19)
    print("Level order traversal of binary tree is -")
    modified_level_order_traversal(root)

