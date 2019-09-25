class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def ConstructTreeArray(arr):
    if not arr:
        return None
    q = []
    root = Node(arr[ConstructTreeArray.arrIndex])
    q.append(root)
    ConstructTreeArray.arrIndex += 1
    while ConstructTreeArray.arrIndex < len(arr):
        parent = q.pop(0)
        rightChild = None
        leftChild = Node(arr[ConstructTreeArray.arrIndex])
        q.append(leftChild)
        ConstructTreeArray.arrIndex += 1
        if ConstructTreeArray.arrIndex < len(arr):
            rightChild = Node(arr[ConstructTreeArray.arrIndex])
            q.append(rightChild)
            ConstructTreeArray.arrIndex += 1
        parent.left = leftChild
        parent.right = rightChild
    return root


def inorder(root):
    if not root:
        return
    inorder(root.left)
    print(root.data, end=" ")
    inorder(root.right)


if __name__ == '__main__':
    ConstructTreeArray.arrIndex = 0
    arr = [36, 30, 25, 15, 12, 10]
    n = len(arr)
    root = ConstructTreeArray(arr)
    inorder(root)
