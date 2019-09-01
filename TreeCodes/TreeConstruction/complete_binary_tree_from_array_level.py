class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def buildTree(arr, root, i, n):
    if i < n:
        temp = Node(arr[i])
        root = temp
        root.left = buildTree(arr, root, 2*i+1, n)
        root.right = buildTree(arr, root, 2*i+2, n)
        return root


def Inorder(root):
    if not root:
        return
    Inorder(root.left)
    print(root.data,end=" ")
    Inorder(root.right)


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6, 6, 6, 6]
    n = len(arr)
    root = None
    root = buildTree(arr, root,0,n)
    Inorder(root)