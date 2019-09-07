class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def printPaths(root):
    path = []
    printPathRec(root, path, 0)


def printPathRec(root, path, path_len):
    if not root:
        return
    if len(path) > path_len:
        path[path_len] = root.data
    else:
        path.append(root.data)
    path_len += 1
    if not root.left and not root.right:
        printArray(path, path_len)
    else:
        printPathRec(root.left, path, path_len)
        printPathRec(root.right, path, path_len)


def printArray(path, path_len):
    for i in path[:path_len]:
        print(i, end=" ")
    print()
