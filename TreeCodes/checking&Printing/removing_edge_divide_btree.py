class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


########################## Time Complexity : O(n^2) ######################
def count(root):
    if not root:
        return 0
    return 1 + count(root.left) + count(root.right)


def checkRec(root, n):
    if not root:
        return False
    if count(root) == n - count(root):
        return True
    return checkRec(root.left, n) or checkRec(root.right, n)


def check(root):
    n = count(root)
    return checkRec(root, n)


########################## Efficient Approach Time Complexity : O(n) ######################
def checkBootomUp(root):
    n = count(root)
    res = [False]
    checkRecBootomUp(root, n, res)
    return res


def checkRecBootomUp(root, n, res):
    if not root:
        return 0
    c = checkRecBootomUp(root.left,n,res) + checkRecBootomUp(root.right, n, res) + 1
    if c == n-c:
        res[0] = True
    return c


if __name__ == '__main__':
    root = Node(5)
    root.left = Node(1)
    root.right = Node(6)
    root.left.left = Node(3)
    root.right.left = Node(7)
    root.right.right = Node(4)
    if check(root):
        print("YES")
    else:
        print("NO")
    if checkBootomUp(root):
        print("Yes BottomUp")
    else:
        print("No Bottom up")
