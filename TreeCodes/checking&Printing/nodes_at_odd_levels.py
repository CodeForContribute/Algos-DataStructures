class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

####### Recursive Method###############
def printOddNodes(root, isodd=True):
    if not root:
        return
    if isodd:
        print(root.data,end=" ")
    printOddNodes(root.left, not isodd)
    printOddNodes(root.right, not isodd)

######## Iterative Method #########33
def printOddNodes_iterative(root):
    if not root:
        return
    queue = list()
    queue.append(root)
    isOdd = True
    while True:
        nodecount = len(queue)
        while nodecount > 0 :
            temp = queue.pop(0)
            if isOdd:
                print(temp.data,end=" ")
            if temp.left:
                queue.append(temp.left)
            if temp.right:
                queue.append(temp.right)
            nodecount -= 1
        isOdd = not isOdd

if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    printOddNodes(root)
    print("\n")
    printOddNodes_iterative(root)