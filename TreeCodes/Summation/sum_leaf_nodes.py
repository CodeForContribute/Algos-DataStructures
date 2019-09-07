class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def sumLeafNodes(root,sum):
    if not root:
        return
    if not root.left and not root.right:
        sum[0] += root.data
    sumLeafNodes(root.left,sum)
    sumLeafNodes(root.right,sum)


def sumLeafNodesQueue(root):
    Queue = list()
    Queue.append(root)
    sum = 0
    while len(Queue):
        temp = Queue.pop(0)
        if not temp.left and not temp.right:
            sum += temp.data
        if temp.left:
            Queue.append(temp.left)
        if temp.right:
            Queue.append(temp.right)

    return sum

if __name__=='__main__':
    root = Node(1)
    root.left = Node(2)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right = Node(3)
    root.right.right = Node(7)
    root.right.left = Node(6)
    root.right.left.right = Node(8)
    print(sumLeafNodesQueue(root))
    total = [0]
    sumLeafNodes(root, total)
# Printing the calculated sum
    print(total[0])