class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.nextRight = None

######### Below solution does work only for complete binary tree
def connect(root):
    if not root:
        return
    root.nextRight = None
    connectRecur(root)

def connectRecur(root):
    if not root:
        return
    if root.left:
        root.left.nextRight = root.right
    if root.right:
        if root.nextRight:
            root.right.nextRight = root.nextRight.left
        else:
            root.right.nextRight = None
    connectRecur(root.left)
    connectRecur(root.right)

############################################################################
## solution valid for all the trees
#1.Using Recursion
def connect_all_tree(root):
    root.nextRight = None
    connectRecur_all_tree(root)

def connectRecur_all_tree(root):
    if not root:
        return
    if root.nextRight:
        connectRecur_all_tree(root.nextRight)
    if root.left:
        if root.right:
            root.left.nextRight = root.right
            root.right.nextRight = getNextRight(root)
        else:
            root.left.nextRight = getNextRight(root)
        connectRecur_all_tree(root.left)
    elif root.right:
        root.right.nextRight = getNextRight(root)
        connectRecur_all_tree(root.right)
    else:
        connectRecur_all_tree(getNextRight(root))

def getNextRight(root):
    temp = root.nextRight
    while temp:
        if temp.left:
            return temp.left
        if temp.right:
            return temp.right
        temp = temp.nextRight
    return None
    
if __name__ == '__main__':
    # Constructed binary tree is
    #         10
    #     / \
    #     8     2
    # /
    # 3
    root = Node(10)
    root.left = Node(8)
    root.right = Node(2)
    root.left.left = Node(3)

    # Populates nextRight pointer in all nodes
    connect(root)

    # Let us check the values of nextRight pointers
    print("Following are populated nextRight",
          "pointers in the tree (-1 is printed",
          "if there is no nextRight)")
    print("nextRight of", root.data, "is ", end="")
    if root.nextRight:
        print(root.nextRight.data)
    else:
        print(-1)
    print("nextRight of", root.left.data, "is ", end="")
    if root.left.nextRight:
        print(root.left.nextRight.data)
    else:
        print(-1)
    print("nextRight of", root.right.data, "is ", end="")
    if root.right.nextRight:
        print(root.right.nextRight.data)
    else:
        print(-1)
    print("nextRight of", root.left.left.data, "is ", end="")
    if root.left.left.nextRight:
        print(root.left.left.nextRight.data)
    else:
        print(-1)
