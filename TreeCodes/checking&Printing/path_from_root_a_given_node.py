class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def printPathRoot2Node(root, node_data):
    queue = dict()
    printPathRoot2Node_Util(root, node_data, 0, queue)


def printPathRoot2Node_Util(root, node_data, level, queue):
    if not root:
        return None
    if node_data == root.data:
        queue[level] = node_data
        for key in queue:
            print(queue[key] ,end=" ")
        return
    queue[level] = root.data
    left = printPathRoot2Node_Util(root.left, node_data, level + 1, queue)
    if not left:
        right = printPathRoot2Node_Util(root.right, node_data, level + 1, queue)

    # if left or right:
    if left or right:
        return left if left else right
    if not left and not right:
        return None


if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)

    x = 7
    printPathRoot2Node(root, x)
