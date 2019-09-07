###################### code to be cleared ##############################
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def getLevel(root, node, level):
    if not root:
        return 0
    if root.data == node:
        return level
    downlevel = getLevel(root.left, node, level + 1)
    if downlevel:
        return downlevel
    return getLevel(root.right, node, level + 1)


def printGivenLevel(root, node, level):
    if not root or level < 2:
        return
    if level == 2:
        if root.left and root.right:
            if root.left.data == node or root.right.data == node:
                return
        if root.left:
            print(root.left.data, end=" ")
        if root.right:
            print(root.right.data, end=" ")
    elif level > 2:
        printGivenLevel(root.left, node, level - 1)
        printGivenLevel(root.right, node, level - 1)


def printCousins(root, node):
    level = getLevel(root, node, 1)
    printGivenLevel(root, node, level)

if __name__ == '__main__': 
    root = Node(1)  
    root.left = Node(2)  
    root.right = Node(3)  
    root.left.left = Node(4)  
    root.left.right = Node(5)  
    root.left.right.right = Node(15)  
    root.right.left = Node(6)  
    root.right.right = Node(7)  
    root.right.left.right = Node(8)
    printCousins(root, 15)