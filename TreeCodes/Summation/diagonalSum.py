class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def diagonalSumUtil(root, vd, diagonalsum):
    if not root:
        return
    if vd not in diagonalsum:
        diagonalsum[vd] = 0
    diagonalsum[vd] += root.data
    diagonalSumUtil(root.left, vd + 1, diagonalsum)
    diagonalSumUtil(root.right, vd, diagonalsum)


def diagonalSum(root):
    if not root:
        return
    diagonalsum = dict()
    diagonalSumUtil(root, 0, diagonalsum)
    for it in diagonalsum:
        print(diagonalsum[it], end=" ")

if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(9)
    root.left.right = Node(6)
    root.right.left = Node(4)
    root.right.right = Node(5)
    root.right.left.right = Node(7)
    root.right.left.left = Node(12)
    root.left.right.left = Node(11)
    root.left.left.right = Node(10)
    diagonalSum(root)