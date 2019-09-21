class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def insert(root, data):
    if not root:
        return Node(data)
    if data < root.data:
        root.left = insert(root.left, data)
    if data > root.data:
        root.right = insert(root.right, data)
    return root


def storeInorder(root, inorder):
    if not root:
        return
    storeInorder(root.left, inorder)
    inorder.append(root.data)
    storeInorder(root.right, inorder)


def findingPairsSum2Bsts(root1, root2, x):
    if not root1 or not root2:
        return None
    inorder1 = list()
    inorder2 = list()
    storeInorder(root1, inorder1)
    storeInorder(root2, inorder2)
    i = 0
    j = len(inorder2) - 1
    while i < len(inorder1) and j >= 0:
        if inorder1[i] + inorder2[j] == x:
            print(inorder1[i], inorder2[j])
            i += 1
            j -= 1
        elif inorder1[i] + inorder2[j] > x:
            j -= 1
        else:
            i += 1


if __name__ == '__main__':
    # first BST
    root1 = None
    root1 = insert(root1, 8)
    root1 = insert(root1, 10)
    root1 = insert(root1, 3)
    root1 = insert(root1, 6)
    root1 = insert(root1, 1)
    root1 = insert(root1, 5)
    root1 = insert(root1, 7)
    root1 = insert(root1, 14)
    root1 = insert(root1, 13)

    # second BST
    root2 = None
    root2 = insert(root2, 5)
    root2 = insert(root2, 18)
    root2 = insert(root2, 2)
    root2 = insert(root2, 1)
    root2 = insert(root2, 3)
    root2 = insert(root2, 4)

    Sum = 10
    findingPairsSum2Bsts(root1, root2, Sum)
