class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def printLevels(root):
    if not root:
        return
    Q = list()
    Q.append([root, 1])
    while len(Q):
        temp = Q.pop(0)
        print("The level of %d is %d" %(temp[0].data, temp[1]))
        if temp[0].left:
            Q.append([temp[0].left,temp[1] + 1])
        if temp[0].right:
            Q.append([temp[0].right, temp[1] + 1])


if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    printLevels(root)
    # print("\n")