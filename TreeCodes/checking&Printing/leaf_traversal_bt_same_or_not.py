class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def isLeaf(root):
    if not root:
        return
    return (root.left is None) and (root.right is None)


def isSameLeafTraversal(root1, root2):
    if not root1 or not root2:
        return False
    stack1 = list()
    stack2 = list()
    stack1.append(root1)
    stack2.append(root2)
    while len(stack1) or len(stack2):
        if len(stack1) == 0 or len(stack2) == 0:
            return False
        temp1 = stack1.pop()
        while temp1 is not None and not isLeaf(temp1):
            if temp1.right:
                stack1.append(temp1.right)
            if temp1.left:
                stack1.append(temp1.left)
            temp1 = stack1.pop()

        temp2 = stack2.pop()
        while temp2 is not None and not isLeaf(temp2):
            if temp2.right:
                stack2.append(temp2.right)
            if temp2.left:
                stack2.append(temp2.left)
            temp2 = stack2.pop()

        if not temp2 or not temp1:
            return False
        if temp1 and temp2:
            if temp1.data != temp2.data:
                return False
    return True


if __name__ == '__main__':
    root1 = Node(1)
    root1.left = Node(2)
    root1.right = Node(3)
    root1.left.left = Node(4)
    root1.right.left = Node(6)
    root1.right.right = Node(7)

    root2 = Node(0)
    root2.left = Node(1)
    root2.right = Node(5)
    root2.left.right = Node(4)
    root2.right.left = Node(6)
    root2.right.right = Node(7)

    if isSameLeafTraversal(root1, root2):
        print("Same")
    else:
        print("Not Same")
