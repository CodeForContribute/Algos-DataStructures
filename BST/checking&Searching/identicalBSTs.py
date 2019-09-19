class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def isIdenticalBSTs(arr1, arr2):
    if not arr1 or not arr2:
        return False
    if len(arr2) != len(arr1):
        return False
    if arr1 and arr2 and len(arr1) == len(arr2):
        n = len(arr1)
        import sys
        INT_MIN = -sys.maxsize
        INT_MAX = sys.maxsize
        return isIdenticalBSTsUtil(arr1, arr2, n, 0, 0, INT_MIN, INT_MAX)


def isIdenticalBSTsUtil(arr1, arr2, n, i1, i2, INT_MIN, INT_MAX):
    pass