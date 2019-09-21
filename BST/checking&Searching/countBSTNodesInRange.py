class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def CountBSTNodes(root, low, high, count, result):
    if not root:
        return
    if low > high:
        return 0
    CountBSTNodes(root.left, low, high, count, result)
    if low <= root.data <= high:
        count[0] += 1
        result.append(root.data)
    CountBSTNodes(root.right, low, high, count, result)


if __name__ == '__main__':
    root = Node(10)
    root.left = Node(5)
    root.right = Node(50)
    root.left.left = Node(1)
    root.right.left = Node(40)
    root.right.right = Node(100)

    # Let us constructed BST shown in above example  
    #     10  
    #     / \  
    # 5     50  
    # /     / \  
    # 1     40 100  
    l = 5
    h = 45
    count = [0]
    result = []
    CountBSTNodes(root, l, h, count, result)
    print(count[0])
    print(result)
