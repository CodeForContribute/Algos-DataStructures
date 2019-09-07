class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


############# Recursive ##################
def printNodesKDistance(root, k):
    if not root:
        return
    if k < 0:
        return
    if k == 0:
        print(root.data, end=" ")
    else:
        printNodesKDistance(root.left, k - 1)
        printNodesKDistance(root.right, k - 1)


################ Iterative #################
def printNodesKthDistance(root, k):
    if not root:
        return
    if k < 0:
        return
    Q = list()
    level = 1
    flag = False
    Q.append(root)
    Q.append(None)
    while len(Q):
        temp = Q.pop(0)
        if temp and level == k:
            print(temp.data, end=" ")
            flag = True

        if temp is None:
            if len(Q):
                Q.append(None)
            level += 1
            if level > k:
                break
        else:
            if temp.left:
                Q.append(temp.left)
            if temp.right:
                Q.append(temp.right)

    return flag


if __name__ == '__main__':
    root = Node(20)
    root.left = Node(10)
    root.right = Node(30)
    root.left.left = Node(5)
    root.left.right = Node(15)
    root.left.right.left = Node(12)
    root.right.left = Node(25)
    root.right.right = Node(40)

    print("data at level 1 : ", end="")
    ret = printNodesKthDistance(root, 1)
    if not ret:
        print("Number exceeds total",
              "number of levels")
    print("\n")
    print("data at level 2 : ", end="")
    ret = printNodesKthDistance(root, 2)
    if not ret:
        print("Number exceeds total",
              "number of levels")
    print("\n")
    print("data at level 3 : ", end="")
    ret = printNodesKthDistance(root, 3)
    # print("\n")
    if not ret:
        print("Number exceeds total",
              "number of levels")
    print("\n")
    print("data at level 6 : ", end="")
    ret = printNodesKthDistance(root, 6)
    if not ret:
        print("Number exceeds total number of levels")

if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(8)

    printNodesKDistance(root, 2)
