class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def minVal(root):
    if not root:
        return
    current = root
    while current.left:
        current = current.left
    return current.data


def maxVal(root):
    if not root:
        return
    current = root
    while current.right:
        current = current.right
    return current.data


def CountBSTs(root, low, high, count):
    # if low > high:
    #     return 0
    if not root:
        return
    CountBSTs(root.left, low, high, count)
    if low <= root.data <= high:
        if root.left:
            min_val = minVal(root.left)
        else:
            min_val = root.data
        if root.right:
            max_val = maxVal(root.right)
        else:
            max_val = root.data
        if min_val >= low and max_val <= high and root.data:
            count[0] += 1
        if not root.left and root.right:
            count[0] += 1
    CountBSTs(root.right, low, high, count)


def insert(root, data):
    if not root:
        return Node(data)
    if root.data > data:
        root.left = insert(root.left, data)
    if root.data < data:
        root.right = insert(root.right, data)
    return root


if __name__ == '__main__':
    # 10
    # / \
    # 5  50
    # /  / \
    # 1  40 100
    root = Node(10)
    root.left = Node(5)
    root.right = Node(50)
    root.left.left = Node(1)
    root.right.left = Node(40)
    root.right.right = Node(100)
    low = 40
    high = 100
    count = [0]
    CountBSTs(root, low, high, count)
    print(count[0])
