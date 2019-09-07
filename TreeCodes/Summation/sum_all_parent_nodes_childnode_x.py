class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def sumParentNodes(root, x):
    sum = [0]
    sumParentNodesUtil(root,sum,x)
    return sum[0]

def sumParentNodesUtil(root,sum,x):
    if not root:
        return
    if (root.left and root.left.data == x) or (root.right and root.right.data == x):
        sum[0] += root.data
    sumParentNodesUtil(root.left, sum, x)
    sumParentNodesUtil(root.right, sum,x)

if __name__ == '__main__':
    root = Node(4)
    root.left = Node(2)
    root.right = Node(5)
    root.left.left = Node(7)
    root.left.right = Node(2)
    root.right.left = Node(5)
    root.right.right = Node(2)
    root.right.left.right = Node(3)
    sum  = sumParentNodes(root, 2)
    print("Sum of all the nodes is:", sum)