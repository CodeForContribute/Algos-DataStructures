class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def isArrayPreOrderTraversal(pre, n):
    if n == 0:
        return True
    stack = []
    import sys
    root = -sys.maxsize
    for i in range(n):
        if pre[i] < root:
            return False
        while len(stack) and stack[-1] < pre[i]:
            temp = stack.pop()
            root = temp
        stack.append(pre[i])
    return True

if __name__ == '__main__':
    pre1 = [40, 30, 35, 80, 100]
    print("true" if isArrayPreOrderTraversal(pre1,len(pre1)) == True else "false")
    pre2 = [40, 30, 35, 20, 80, 100]
    print("true" if isArrayPreOrderTraversal(pre2,len(pre2)) == True else "false")