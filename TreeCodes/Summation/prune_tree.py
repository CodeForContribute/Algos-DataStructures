class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def inorder(root):
    if not root:
        return
    inorder(root.left)
    print(root.data,end=" ")
    inorder(root.right)

def pruneUtil(root,sum):
    if not root:
        return None
    root.left = pruneUtil(root.left, sum-root.data)
    root.right = pruneUtil(root.right,sum-root.data)
    if not root.left and not root.right:
        if sum-root.data>0:
            return None
    return root

if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    root.left.left.left = Node(8)
    root.left.left.right = Node(9)
    root.left.right.left = Node(12)
    root.right.right.left = Node(10)
    root.right.right.left.right = Node(11)
    root.left.left.right.left = Node(13)
    root.left.left.right.right = Node(14)
    root.left.left.right.right.left = Node(15)

    print("Tree before truncation")
    inorder(root)
    pruneUtil(root, 45)
    print("\nTree after truncation")
    inorder(root)