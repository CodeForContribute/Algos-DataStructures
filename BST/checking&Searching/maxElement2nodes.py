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


# Time complexity : O(h) where h is height of BST
def MaxElement(root, n1, n2):
    p = root
    while (n1 < p.data and n2 < p.data) or (n1 > p.data and n2 > p.data):
        if n1 < p.data and n2 < p.data:
            p = p.left
        elif n1 > p.data and n2 > p.data:
            p = p.right
        return max(maxelPath(p, n1), maxelPath(p, n2))


def maxelPath(root, n):
    p = root
    mx = -999999999
    while p.data != n:
        if p.data > n:
            mx = max(mx, p.data)
            p = p.left
        else:
            mx = max(mx, p.data)
            p = p.right
    return max(mx, n)


if __name__ == '__main__':
    arr = [18, 36, 9, 6, 12, 10, 1, 8]
    a, b = 1, 10
    n = len(arr)

    # Creating the root of Binary Search Tree
    root = Node(arr[0])

    # Inserting Nodes in Binary Search Tree
    for i in range(1, n):
        insert(root, arr[i])

    print(MaxElement(root, a, b))
