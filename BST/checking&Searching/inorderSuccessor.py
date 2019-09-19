class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def minVal(root):
    if not root:
        return
    current = root
    while current.left:
        current = current.left
    return current.data

def inorderSuccessor(root, node):
    if node.right:
        return minVal(node.right)

    suc = None
    while root:
        if node.data < root.data:
            suc = root
            root = root.left
        elif node.data > root.data:
            root = root.right
        else:
            break
    if suc:
        return suc.data
    return "No suc"


if __name__ == '__main__':
    root = None

    # Creating the tree given in the above diagram  
    root = Node(20)
    root.left = Node(8)
    root.right = Node(22)
    root.left.left = Node(4)
    root.left.right = Node(12)
    root.left.right.left = Node(10)
    root.left.right.right = Node(14)
    succ = inorderSuccessor(root, Node(22))
    print(succ)
