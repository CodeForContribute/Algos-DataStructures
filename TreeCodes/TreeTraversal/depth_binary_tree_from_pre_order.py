class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def findDepthRecursion(tree, n, index):
    if index[0] >= n or tree[index[0]] == 'l':
        return 0
    index[0] += 1
    left = findDepthRecursion(tree, n, index)
    index[0] += 1
    right = findDepthRecursion(tree, n, index)
    return max(left, right) + 1


def findDepth(tree, n):
    index = [0]
    return findDepthRecursion(tree, n, index)


if __name__ == '__main__':
    tree = "nlnnlll"
    n = len(tree)

    print(findDepth(tree, n))
