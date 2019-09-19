class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def insert(root, data):
    if not root:
        return Node(data)
    if root.data  < data:
        root.right= insert(root.right, data)
    if root.data > data:
        root.left = insert(root.left, data)
    return root

# Time Complexity:O(h)
def findMaxForN(root, n):
    if not root:
        return -1
    if root.data == n:
        return n
    elif root.data < n:
        k = findMaxForN(root.right, n)
        if k == -1:
            return root.data
        else:
            return k
    elif root.data > n:
        return findMaxForN(root.left, n)

if __name__ == '__main__':
    N = 4

    # creating following BST
    #
    #             5
    #            / \
    #            2  12
    #           / \ / \
    #           1 3 9 21
    #                 / \
    #                19 25
    root = None
    root = insert(root, 25)
    insert(root, 2)
    insert(root, 1)
    insert(root, 3)
    insert(root, 12)
    insert(root, 9)
    insert(root, 21)
    insert(root, 19)
    insert(root, 25)
    print(findMaxForN(root, N))