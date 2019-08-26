class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def MorrisTraversalPreOrder(root):
    cuurent = root
    while cuurent:
        if cuurent.left is None:
            print(cuurent.data, end=" ")
            cuurent = cuurent.right
        else:
            prev = cuurent.left
            while prev.right is not None and prev.right is not cuurent:
                prev = prev.right
            if prev.right is cuurent:
                prev.right = None
                cuurent = cuurent.right
            else:
                print(cuurent.data,end=" ")
                prev.right = cuurent
                cuurent = cuurent.left

def MorrisTraversalInOrder(root):
    cuurent = root
    while cuurent:
        if cuurent.left is None:
            print(cuurent.data, end=" ")
            cuurent = cuurent.right
        else:
            prev = cuurent.left
            while prev.right is not None and prev.right is not cuurent:
                prev = prev.right
            if prev.right is cuurent:
                print(prev.right.data, end=" ")
                prev.right = None
                cuurent = cuurent.right
            else:
                # print(cuurent.data,end=" ")
                prev.right = cuurent
                cuurent = cuurent.left

def InOrder(root):
    if not root:
        return
    InOrder(root.left)
    print(root.data,end=" ")
    InOrder(root.right)


def preOrder(root):
    if not root:
        return
    print(root.data,end=" ")
    preOrder(root.left)
    preOrder(root.right)


if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)

    root.left.left = Node(4)
    root.left.right = Node(5)

    # root.right.left = Node(6)
    # root.right.right = Node(7)
    #
    # root.left.left.left = Node(8)
    # root.left.left.right = Node(9)
    #
    # root.left.right.left = Node(10)
    # root.left.right.right = Node(11)

    MorrisTraversalPreOrder(root)
    print("\n")
    preOrder(root)
    print("\n")
    MorrisTraversalInOrder(root)
    print("\n")
    InOrder(root)