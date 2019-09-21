class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def insert(root, data):
    if not root:
        return Node(data)
    if root.data < data:
        root.right = insert(root.right, data)
    if root.data > data:
        root.left = insert(root.left, data)
    return root


# Time Complexity: O(n) where n is number of nodes in the given BST.
def addGreaterElement(root):
    if not root:
        return
    sum = [0]
    addGreaterElementUtil(root, sum)


def addGreaterElementUtil(root, sum):
    if not root:
        return
    addGreaterElementUtil(root.right, sum)
    sum[0] += root.data
    root.data = sum[0]
    addGreaterElementUtil(root.left, sum)


def inorder(root):
    if not root:
        return
    inorder(root.left)
    print(root.data, end=" ")
    inorder(root.right)


if __name__ == '__main__':
    # Let us create following BST
    #         50
    #        / \
    #       30   70
    #       / \  / \
    #      20 40 60 80
    root = None
    root = insert(root, 50)
    insert(root, 30)
    insert(root, 20)
    insert(root, 40)
    insert(root, 70)
    insert(root, 60)
    insert(root, 80)
    addGreaterElement(root)
    inorder(root)
