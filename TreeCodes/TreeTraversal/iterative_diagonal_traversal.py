class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def diagonalPrint(root):
    if not root:
        return
    queue = list()
    queue.append(root)
    queue.append(None)
    while len(queue):
        temp = queue.pop(0)
        if temp is None:
            if len(queue) == 0:
                return
            print("\n")
            queue.append(None)
        else:
            while temp:
                print(temp.data, end=" ")
                if temp.left is not None:
                    queue.append(temp.left)
                temp = temp.right

if __name__ == '__main__':
    root = Node(8)
    root.left = Node(3)
    root.right = Node(10)
    root.left.left = Node(1)
    root.left.right = Node(6)
    root.right.right = Node(14)
    root.right.right.left = Node(13)
    root.left.right.left = Node(4)
    root.left.right.right = Node(7)
    diagonalPrint(root)