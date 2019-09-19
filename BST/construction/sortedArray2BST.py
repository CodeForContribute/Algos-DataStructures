class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None



def array2BST(arr):
    if not arr:
        return None
    mid = (len(arr))//2
    root = Node(arr[mid])
    root.left = array2BST(arr[:mid])
    root.right = array2BST(arr[mid+1:])
    return root

def preOrder(root):
    if not root:
        return
    print(root.data,end=" ")
    preOrder(root.left)
    preOrder(root.right)



if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6, 7]
    root = array2BST(arr)
    print("PreOrder Traversal of constructed BST ",)
    preOrder(root)
