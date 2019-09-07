class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def isMinHeap(level, n):
    i = (n-1)//2
    for j in range(i, -1, -1):
        # if level[j] > level[2*j+1]:
        #     return False
        if (2*j +1) < n:
            if level[j] > level[2*j+1]:
                return False
        if (2 * j + 2) < n:
            if level[j] > level[2 * j + 2]:
                return False
    return True

if __name__ == '__main__':
    level = [10, 15, 14, 25, 30]
    n = len(level)
    if isMinHeap(level, n):
        print("True")
    else:
        print("False")