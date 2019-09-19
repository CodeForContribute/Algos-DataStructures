class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def checkInternalNode1Child(pre,n):
    if not pre:
        return False
    if n <= 0:
        return False
    for i in range(n):
        next_diff = pre[i]-pre[i+1]
        last_diff = pre[i] - pre[n-1]
        if next_diff * last_diff < 0:
            return False
        return True

if __name__ == '__main__':
    pre = [8, 3, 5, 7, 6]
    size = len(pre)

    if checkInternalNode1Child(pre, size) is True:
        print("Yes")
    else:
        print("No")

