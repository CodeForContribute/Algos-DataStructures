class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def sumNodesPerfectBinaryTree(root,l):
    if not root:
        return
    import math
    leafNodesCount = math.pow(2, l-1)
    sumLastLevel = (leafNodesCount * (leafNodesCount + 1))//2
    sum = sumLastLevel*l
    return sum

if __name__ == '__main__':
    l = 3
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    print(sumNodesPerfectBinaryTree(root, l))
