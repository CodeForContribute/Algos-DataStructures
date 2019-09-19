import sys

INT_MIN = -sys.maxsize
INT_MAX = sys.maxsize


class Node:
    def __init__(self, data, min, max):
        self.data = data
        self.min = min
        self.max = max


def levelOrderTraversalBST(root):
    if not root:
        return
    q = []
    result = []
    q.append(root)
    while len(q):
        nodeCounts = len(q)
        while nodeCounts:
            temp = q.pop(0)
            result.append(root.data)
            if temp.left:
                q.append(temp.left)
            if temp.right:
                q.append(temp.right)
            nodeCounts -= 1
    return result


def isLevelOrderBST(arr, n):
    if n == 0:
        return True
    q = []
    i = 0
    newNode = Node(arr[i], INT_MIN, INT_MAX)
    i += 1
    q.append(newNode)
    while i != n and len(q):
        temp = q.pop(0)
        if i < n and temp.min < arr[i] < temp.data:
            newNode = Node(arr[i], temp.min, temp.data)
            q.append(newNode)
            i += 1
        if i < n and temp.data < arr[i] < temp.max:
            newNode = Node(arr[i], temp.data, temp.max)
            q.append(newNode)
            i += 1
    if i == n:
        return True

    return False


if __name__ == '__main__':
    arr = [7, 4, 12, 3, 6, 8, 1, 5, 10]
    n = len(arr)
    print(isLevelOrderBST(arr, n))
