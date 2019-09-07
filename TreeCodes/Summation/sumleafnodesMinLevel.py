class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def sumLeafMinLevel(root):
    if not root:
        return 0
    if not root.left and not root.right:
        return root.data
    Queue = list()
    Queue.append(root)
    flag = 0
    sum =0
    while flag == 0:
        nc = len(Queue)
        while nc > 0:
            temp = Queue.pop(0)
            if not temp.left and not temp.right:
                sum += temp.data
                flag = 1
            else:
                if temp.left:
                    Queue.append(temp.left)
                if temp.right:
                    Queue.append(temp.right)
            nc -= 1
    return sum

if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    root.left.right.left = Node(8)
    root.right.left.right = Node(9)
    print(sumLeafMinLevel(root))