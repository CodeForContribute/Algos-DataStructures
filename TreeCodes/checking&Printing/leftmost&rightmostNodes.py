class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def printLeftMostRightmost(root):
    if not root:
        return
    Q = list()
    Q.append(root)
    while len(Q):
        if len(Q) == 1:
            temp  = Q.pop(0)
            print(temp.data,end=" ")
            if temp.left:
                Q.append(temp.left)
            if temp.right:
                Q.append(temp.right)
        elif len(Q) > 1:
            temp1 = Q.pop(0)
            temp2 = Q.pop()
            print(temp1.data,end=" ")
            print(temp2.data,end=" ")
            Q.clear()
            if temp1.left:
                Q.append(temp1.left)
            if temp1.right:
                Q.append(temp1.right)
            if temp2.left:
                Q.append(temp2.left)
            if temp2.right:
                Q.append(temp2.right)

if __name__ == '__main__':
    root = Node(15)
    root.left = Node(10)
    root.right = Node(20)
    root.left.right = Node(8)
    root.right.left = Node(25)
    printLeftMostRightmost(root)
