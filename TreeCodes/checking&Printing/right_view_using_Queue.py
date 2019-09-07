class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def rightViewQueue(root):
    if not root:
        return
    Q = list()
    Q.append(root)
    while len(Q):
        n = len(Q)
        for i in range(1, n+1):
            temp = Q.pop(0)
            if i == n:
                print(temp.data, end=" ")
            if temp.left:
                Q.append(temp.left)
            if temp.right:
                Q.append(temp.right)

if __name__ == '__main__':
    root = Node(10)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(7)
    root.left.right = Node(8)
    root.right.right = Node(15)
    root.right.left = Node(12)
    root.right.right.left = Node(14)
    rightViewQueue(root)