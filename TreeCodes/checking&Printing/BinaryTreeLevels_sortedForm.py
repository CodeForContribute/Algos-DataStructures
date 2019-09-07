class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def BinaryTreeLevelsSorted(root):
    if not root:
        return
    Q = list()
    s = set()
    Q.append(root)
    Q.append(None)
    while len(Q):
        temp = Q.pop(0)
        if temp is None:
            if not len(Q):
                break
            for i in s:
                print(i, end=" ")
            print("\n")
            Q.append(None)
            s = set()
        else:
            s.add(temp.data)
            if temp.left:
                Q.append(temp.left)
            if temp.right:
                Q.append(temp.right)

if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    root.right.left.right = Node(8)
    root.right.right.left = Node(10)
    root.right.right.right = Node(9)
    root.right.right.left.right = Node(11)
    root.right.right.left.right.right = Node(12)
    BinaryTreeLevelsSorted(root)
