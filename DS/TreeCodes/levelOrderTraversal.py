class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def height_tree(self, node):
        if node is None:
            return 0
        else:
            left_height = self.height_tree(node.left)
            right_height = self.height_tree(node.right)
            if left_height > right_height:
                return left_height + 1
            else:
                return right_height + 1

    def print_level_order(self, root_value):
        h = self.height_tree(root_value)
        for i in range(1, h+1):
            self.print_given_level(root_value, i)

    def print_given_level(self, root_value, level):
        if root_value is None:
            return
        if level == 1:
            print(root_value.data, end=" ")
        elif level > 1:
            self.print_given_level(root_value.left, level-1)
            self.print_given_level(root_value.right, level-1)

    @staticmethod
    def iterative_approach_level_order_traversal(root_value):
        if root_value is None:
            return
        queue = list()
        queue.append(root_value)
        while len(queue) > 0:
            print(queue[0].data, end=" ")
            node = queue.pop(0)
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)


if __name__ == '__main__':
    tree = BinaryTree()
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    print("Level order traversal of binary tree is -")
    tree.print_level_order(root)
    print("\n")
    print("Iterative approach for Level Order Traversal")
    tree.iterative_approach_level_order_traversal(root)
