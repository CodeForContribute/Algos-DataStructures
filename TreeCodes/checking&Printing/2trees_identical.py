class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def areIdentical(root1, root2):
    if not root1 and not root2:
        return True
    if not root2 or not root1:
        return False
    q1 = list()
    q2 = list()
    q1.append(root1)
    q2.append(root2)
    while len(q1) and len(q2):
        temp1 = q1.pop(0)
        temp2 = q2.pop(0)
        if temp1.data != temp2.data:
            return False
        if temp1.left and temp2.left:
            q1.append(temp1.left)
            q2.append(temp2.left)
        elif temp1.left or temp2.left:
            return False
        if temp1.right and temp2.right:
            q1.append(temp1.right)
            q2.append(temp2.right)
        elif temp1.right or temp2.right:
            return False
    return True

if __name__ == '__main__':
    root1 = Node(1)
    root1.left = Node(2)
    root1.right = Node(3)
    root1.left.left = Node(4)
    root1.left.right = Node(5)

    root2 = Node(1)
    root2.left = Node(2)
    root2.right = Node(3)
    root2.left.left = Node(4)
    root2.left.right = Node(5)

    if areIdentical(root1, root2):
        print("Yes")
    else:
        print("No")

