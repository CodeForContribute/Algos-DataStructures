class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None



def isSymmetric(root):
    if not root:
        return True
    if not root.left and not root.right:
        return True
    queue = list()
    queue.append(root)
    queue.append(root)
    while len(queue):
        leftNode = queue.pop(0)
        rightNode = queue.pop(0)
        if leftNode.data!= rightNode.data:
            return False
        if leftNode.left and rightNode.right:
            queue.append(leftNode.left)
            queue.append(rightNode.right)
        elif leftNode.left or rightNode.right:
            return False
    return True


if __name__ == '__main__':

    # Let us construct the Tree  
    # shown in the above figure  
    root = Node(1)
    root.left = Node(2)
    root.right = Node(2)
    root.left.left = Node(3)
    root.left.right = Node(4)
    root.right.left = Node(4)
    root.right.right = Node(3)
    if isSymmetric(root):
        print("The given tree is Symmetric")
    else:
        print("The given tree is not symmetric")