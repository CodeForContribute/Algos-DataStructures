class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def printTopBottom(current, parent):
    stack =list()
    while current:
        stack.append(current)
        current = parent[current]
    while len(stack):
        current = stack.pop()
        print(current.data,end=" ")
    print("\n")

def printRootToLeafNodes(root):
    if not root:
        return
    nodeStack = list()
    nodeStack.append(root)
    parent = dict()
    parent[root] = None
    while len(nodeStack):
        temp = nodeStack.pop()
        if not temp.left and not temp.right:
            printTopBottom(temp, parent)
        if temp.right:
            parent[temp.right] = temp
            nodeStack.append(temp.right)
        if temp.left:
            parent[temp.left] = temp
            nodeStack.append(temp.left)


if __name__ == '__main__':
    # Constructed binary tree is
    #     10
    # / \
    # 8 2
    # / \ /
    # 3 5 2
    root = Node(10)
    root.left = Node(8)
    root.right = Node(2)
    root.left.left = Node(3)
    root.left.right = Node(5)
    root.right.left = Node(2)
    printRootToLeafNodes(root)
