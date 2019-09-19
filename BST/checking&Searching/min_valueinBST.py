class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def insert(root, data):
    if not root:
        return Node(data)
    else:
        if data < root.data:
            root.left = insert(root.left, data)
        else:
            root.right = insert(root.right, data)
        return root

def minValueBST(root):
    # if not root:
    #     return
    current = root
    while current.left:
        current = current.left
    print(current.data,end=" ")


def maxValBST(root):
    if not root:
        return
    current = root
    while current.right:
        current = current.right
    print(current.data,end=" ")

if __name__ == '__main__':
    root = None
    root = insert(root, 4)
    insert(root, 2)
    insert(root, 1)
    insert(root, 3)
    insert(root, 6)
    insert(root, 5)
    # print("\nMinimum value in BST is %d" % (minValueBST(root)))
    minValueBST(root)
    maxValBST(root)