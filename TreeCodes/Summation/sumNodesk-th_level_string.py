class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def sumKthLevel(root, k):
    if k < 0:
        return
    sum = 0
    level = -1
    l = len(root)
    for i in range(l):
        if root[i] == '(':
            level += 1
        elif root[i] == ')':
            level -= 1
        else:
            if level == k:
                sum += (ord(root[i]) - ord('0'))

    return sum

if __name__ == '__main__':
    if __name__ == '__main__':
        tree = "(0(5(6()())(4()(9()())))(7(1()())(3()())))"
        k = 2
        print(sumKthLevel(tree, k))