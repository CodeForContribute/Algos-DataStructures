class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def existPath(root, arr, n, index):
    if not root:
        return n == 0
    if not root.left and not root.right and root.data == arr[index] and index == n - 1:
        return True
    return index < n and root.data == arr[index] and (existPath(root.left, arr, n, index + 1) or existPath(root.right,
                                                                                                          arr, n,
                                                                                                          index + 1))


if __name__ == '__main__':

    # arr[] -. sequence of root to leaf path  
    arr = [5, 8, 6, 7]
    n = len(arr)
    root = Node(5)
    root.left = Node(3)
    root.right = Node(8)
    root.left.left = Node(2)
    root.left.right = Node(4)
    root.left.left.left = Node(1)
    root.right.left = Node(6)
    root.right.left.right = Node(7)

    if existPath(root, arr, n, 0):
        print("Path Exists")
    else:
        print("Path does not Exist") 