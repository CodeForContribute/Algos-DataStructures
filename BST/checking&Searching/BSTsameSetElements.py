class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def insertIntoSet(root, s):
    if not root:
        return
    insertIntoSet(root.left,s)
    s.add(root.data)
    insertIntoSet(root.right, s)

def isTwoBstsElements(root1, root2):
    if not root1 and not root2:
        return True
    if not root1 or not root2:
        return False
    s1 = set()
    s2 = set()
    insertIntoSet(root1, s1)
    insertIntoSet(root2, s2)
    return s1 == s2

if __name__ == '__main__':
    root1 = Node(15)
    root1.left = Node(10)
    root1.right = Node(20)
    root1.left.left = Node(5)
    root1.left.right = Node(12)
    root1.right.right = Node(25)

    root2 = Node(15)
    root2.left = Node(12)
    root2.right = Node(20)
    root2.left.left = Node(5)
    root2.left.left.right = Node(10)
    root2.right.right = Node(25)
    if isTwoBstsElements(root1, root2):
        print("Yes")
    else:
        print("No")


