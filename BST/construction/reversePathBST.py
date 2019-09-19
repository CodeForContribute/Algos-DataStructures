class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def inorder(root):
    if not root:
        return
    inorder(root.left)
    print(root.data, end=" ")
    inorder(root.right)


def reversePath(root, k):
    if not root:
        return
    q1 = list()
    reversePathUtil(root, k, q1)


def reversePathUtil(root, k, q1):
    if not root:
        return
    if root.data == k:
        q1.append(root.data)
        root.data = q1.pop(0)
        return
    elif root.data > k:
        q1.append(root.data)
        reversePathUtil(root.left, k, q1)
        root.data = q1.pop(0)
    elif root.data < k:
        q1.append(root.data)
        reversePathUtil(root.right, k, q1)
        root.data = q1.pop(0)
    return


def insert(root, data):
    if not root:
        return Node(data)
    if root.data < data:
        root.right = insert(root.right, data)
    if root.data > data:
        root.left = insert(root.left, data)

    return root


if __name__ == '__main__':
    k = 80
    root = None
    root = insert(root, 50)
    insert(root, 30)
    insert(root, 20)
    insert(root, 40)
    insert(root, 70)
    insert(root, 60)
    insert(root, 80)

    print("Before Reverse :")
    print("inoder traversal of the BST")
    inorder(root)
    print("\n after reversing the path")
    reversePath(root, k)
    inorder(root)
