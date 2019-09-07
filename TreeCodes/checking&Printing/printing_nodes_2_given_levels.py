class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def printNodes(root, low, high):
    Q = []
    marker = None
    level = 1
    Q.append(root)
    Q.append(marker)
    while len(Q):
        temp = Q.pop(0)
        if temp is None:
            level += 1
            if len(Q) == 0 or level > high:
                break
            Q.append(None)
            print("\n")
            continue

        if level >= low:
            print(temp.data,end=" ")

        if temp.left and temp.right:
            Q.append(temp.left)
            Q.append(temp.right)

if __name__ == '__main__':
    root = Node(20)
    root.left = Node(8)
    root.right = Node(22)
    root.left.left = Node(4)
    root.left.right = Node(12)
    root.left.right.left = Node(10)
    root.left.right.right = Node(14)

    print("Level Order Traversal between given two levels is",)
    printNodes(root, 2, 3)