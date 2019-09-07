class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def rightLeafSum(root, sum):
    if not root:
        return
    if root.right:
        if not root.right.left and not root.right.right:
            sum[0] += root.right.data
    rightLeafSum(root.left, sum)
    rightLeafSum(root.right, sum)


if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.left.left.right = Node(2)
    root.right = Node(3)
    root.right.right = Node(8)
    root.right.right.left = Node(6)
    root.right.right.right = Node(7)

    # variable to store Sum of right  
    # leaves  
    Sum = [0]
    rightLeafSum(root, Sum)
    print(Sum[0]) 
