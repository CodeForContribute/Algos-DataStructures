class Node:
    def __init__(self, data):
        self.data = data
        self.left  = None
        self.right = None

def leftMost(node):
    while node is not None and node.left is not None:
        node = node.left
    return node

def rightMost(node):
    while node is not None and node.right is not None:
         node = node.right
    return node

def findInorderRecursive(root, x):
    if x is None:
        return
    if not root:
        return
    if root == x or findInorderRecursive(root.left, x) or findInorderRecursive(root.right, x):
        if findInorderRecursive(root.right, x):
            temp = findInorderRecursive(root.right, x)
        else:
            temp = findInorderRecursive(root.left, x)
        if temp:
            if root.left == temp:
                print("Inorder Successor of",x.data, end="")
                print(" is", root.data)
                return None
        return root
    return None

def inorderSuccesor(root, x ):
    if not root:
        return
    if not x:
        return
    # Case1: If right child is not None
    if x.right is not None:
        in_order_sucessor = leftMost(x.right)
        print("Inorder Successor of", x.data,
              "is", end=" ")
        print(in_order_sucessor.data)
    # Case2: if right child is None:
    if x.right is None:
        right_most = rightMost(root)
        # case3: If x is the right most node
        if right_most is x:
            print("No Inorder sucessor of {}".format(x.data))
        else:
            findInorderRecursive(root, x)



if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.right = Node(6)

    # Case 1  
    inorderSuccesor(root, root.right)

    # case 2  
    inorderSuccesor(root, root.left.left)

    # case 3  
    inorderSuccesor(root, root.right.right)

    inorderSuccesor(root, root.left.right)