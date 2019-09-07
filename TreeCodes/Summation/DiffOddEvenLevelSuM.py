class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def DiffOddLevelevenLevel(root):
    if not root:
        return 0
    Queue = list()
    Queue.append(root)
    level = 0
    evenSum = 0
    oddSum = 0
    while len(Queue):
        size = len(Queue)
        level += 1
        while size:
            temp = Queue.pop(0)
            if level %2 == 0:
                evenSum += temp.data
            elif level %2 != 0:
                oddSum += temp.data
            if temp.left:
                Queue.append(temp.left)
            if temp.right:
                Queue.append(temp.right)
            size -= 1
    return oddSum-evenSum

if __name__ == '__main__':
    if __name__ == '__main__':
        """  
        Let us create Binary Tree shown 
        in above example """
        root = Node(5)
        root.left = Node(2)
        root.right = Node(6)
        root.left.left = Node(1)
        root.left.right = Node(4)
        root.left.right.left = Node(3)
        root.right.right = Node(8)
        root.right.right.right = Node(9)
        root.right.right.left = Node(7)

        result = DiffOddLevelevenLevel(root)
        print("Diffence between sums is", result)
