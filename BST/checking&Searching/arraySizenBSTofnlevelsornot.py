class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def isBSTofNLevels(arr, n):
    if not arr:
        return
    if n <= 0:
        return
    import sys
    min_val = -sys.maxsize
    max_val = sys.maxsize
    flag = True
    for i in range(1, n):
        if arr[i] > arr[i - 1] and min_val < arr[i] < max_val:
            min_val = arr[i - 1]
        elif arr[i] < arr[i - 1] and min_val < arr[i] < max_val:
            max_val = arr[i - 1]
        else:
            flag = False
            break
    return flag


if __name__ == '__main__':
    arr = [500, 200, 90, 250, 1000]
    n = len(arr)
    print(isBSTofNLevels(arr, n))
