class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def isInorder(arr, n):
    if n == 0 or n == 1:
        return True
    for i in range(1, n):
        if arr[i - 1] > arr[i]:
            return False
    return True


if __name__ == '__main__':
    arr = [19, 23, 25, 30, 45]
    n = len(arr)

    if isInorder(arr, n):
        print("Yes")
    else:
        print("No")
