class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


################# Incomplete #############
def insert(root, data, suc):
    if not root:
        root = Node(data)
    if root.data > data:
        suc[0] = root
        insert(root.left, data, suc)
    elif root.data < data:
        insert(root.right, data, suc)


def replacewithleastGreater(arr, n):
    root = None
    for i in range(n - 1, 0, -1):
        suc = [None]
        insert(root, arr[i], suc)
        if suc[0]:
            arr[i] = suc[0].data
        else:
            arr[i] = -1


if __name__ == '__main__':
    arr = [8, 58, 71, 18]
    n = len(arr)
    replacewithleastGreater(arr, n)
    print(arr)
