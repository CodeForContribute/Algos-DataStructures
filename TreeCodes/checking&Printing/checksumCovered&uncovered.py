class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def sum(root):
    if not root:
        return 0
    return root.data + sum(root.left)+sum(root.right)

def uncoveredSumLeft(node):
    if node.left is None and node.right is None:
        return node.data
    if node.left is not None:
        return node.data + uncoveredSumLeft(node.left)
    else:
        return node.data + uncoveredSumLeft(node.right)


def unCoveredSumRight(node):
    if node.right is None and node.left is None:
        return node.data
    if node.right is not None:
        return node.data + unCoveredSumRight(node.right)
    else:
        return node.data + unCoveredSumRight(node.left)

def UncoverSum(root):
    leftboundry = 0
    rightboundry = 0
    if root.left is not None:
        leftboundry = uncoveredSumLeft(root.left)
    if root.right is not None:
        rightboundry = unCoveredSumRight(root.right)

    return root.data + leftboundry + rightboundry

def isSumTree(root):
    UncoveredSum = UncoverSum(root)
    sumTree = sum(root)
    return UncoveredSum == sumTree-UncoveredSum


if __name__ == '__main__':
    root = Node(8)
    root.left = Node(3)

    root.left.left = Node(1)
    root.left.right = Node(6)
    root.left.right.left = Node(4)
    root.left.right.right = Node(7)

    root.right = Node(10)
    root.right.right = Node(14)
    root.right.right.left = Node(13)

    if isSumTree(root):
        print("Sum of covered and uncovered is same")
    else:
        print("Sum of covered and uncovered is not same")