class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def findDepth(node):
    d = 0
    while node:
        d += 1
        node = node.left
    return d

def isPerfectRec(root, d, level=0):
    if not root:
        return True
    if root.left is None and root.right is None:
        return d == level+1
    if not root.left or not root.right:
        return False
    return isPerfectRec(root.left,d, level+1) and isPerfectRec(root.right, d, level+1)

def isPerfect(root):
    d = findDepth(root)
    return isPerfectRec(root, d)

if __name__ == '__main__':
    root = Node(10)
    root.left = Node(20)
    root.right = Node(30)

    root.left.left = Node(40)
    root.left.right = Node(50)
    root.right.left = Node(60)
    root.right.right = Node(70)

    if isPerfect(root):
        print("Yes")
    else:
        print("No")