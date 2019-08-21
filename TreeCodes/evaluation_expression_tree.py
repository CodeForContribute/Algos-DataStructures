class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def evalaute_expression_tree(root):
    if root is None:
        return
    if root.left is None and root.right is None:
        return int(root.data)
    left_sum = evalaute_expression_tree(root.left)
    right_sum = evalaute_expression_tree(root.right)
    if root.data == "+":
        return left_sum + right_sum
    if root.data == "-":
        return left_sum - right_sum
    if root.data == "*":
        return left_sum * right_sum
    if root.data == "/":
        return left_sum / right_sum


if __name__ == '__main__':
    # root = Node(1)
    root = Node('+')
    root.left = Node('*')
    root.left.left = Node('5')
    root.left.right = Node('4')
    root.right = Node('-')
    root.right.left = Node('100')
    root.right.right = Node('/')
    root.right.right.left = Node('20')
    root.right.right.right = Node('2')
    print(evalaute_expression_tree(root))
