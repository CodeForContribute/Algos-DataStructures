class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.nextRight = None


def getNextRight(root):
    temp = root.nextRight
    while temp:
        if temp.left:
            return temp.left
        if temp.right:
            return temp.right
        temp = temp.nextRight
    return None

def connect(root):
    temp = None
    if not root:
        return
    root.nextRight = None
    while root:
        q = root
        while q:
            if q.left:
                if q.right:
                    q.left.nextRight = q.right
                else:
                    q.left.nextRight = getNextRight(q)
            if q.right:
                q.right.nextRight = getNextRight(q)
            q = q.nextRight
        if root.left:
            root = root.left
        elif root.right:
            root = root.right
        else:
            root = getNextRight(root)

if __name__ == '__main__':
    if __name__ == '__main__':

        # Constructed binary tree is  
        #         10  
        #        / \
        #       8   2
        #      /     \
        #     3       90
        root = Node(10)
        root.left = Node(8)
        root.right = Node(2)
        root.left.left = Node(3)
        root.right.right = Node(90)

        # Populates nextRight pointer in all nodes  
        connect(root)

        # Let us check the values of nextRight pointers  
        print("Following are populated nextRight "
              "pointers in the tree (-1 is printed "
              "if there is no nextRight) \n")
        print("nextRight of", root.data,
              "is", end=" ")
        if root.nextRight:
            print(root.nextRight.data)
        else:
            print(-1)
        print("nextRight of", root.left.data,
              "is", end=" ")
        if root.left.nextRight:
            print(root.left.nextRight.data)
        else:
            print(-1)
        print("nextRight of", root.right.data,
              "is", end=" ")
        if root.right.nextRight:
            print(root.right.nextRight.data)
        else:
            print(-1)
        print("nextRight of", root.left.left.data,
              "is", end=" ")
        if root.left.left.nextRight:
            print(root.left.left.nextRight.data)
        else:
            print(-1)
        print("nextRight of", root.right.right.data,
              "is", end=" ")
        if root.right.right.nextRight:
            print(root.right.right.nextRight.data)
        else:
            print(-1) 
                