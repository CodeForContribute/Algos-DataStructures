class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def inorderTraversal(root, inorder):
    if not root:
        return
    inorderTraversal(root.left, inorder)
    inorder.append(root.data)
    inorderTraversal(root.right, inorder)


def printLevelOrderTraversal(root):
    if not root:
        return
    q = list()
    q.append(root)
    while len(q):
        nodeCounts = len(q)
        while nodeCounts:
            temp = q.pop(0)
            print(temp.data,end=" ")
            if temp.left:
                q.append(temp.left)
            if temp.right:
                q.append(temp.right)
            nodeCounts -= 1
        print()

def constructHeapFromArr(root, inorder, i):
    if not root:
        return
    i[0] += 1
    root.data = inorder[i[0]]
    constructHeapFromArr(root.left, inorder, i)
    constructHeapFromArr(root.right, inorder, i)

def preOrder(root):
    if not root:
        return
    print(root.data,end=" ")
    preOrder(root.left)
    preOrder(root.right)

def convertBSTMinHeap(root):
    inorder = list()
    inorderTraversal(root, inorder)
    i = [-1]
    constructHeapFromArr(root, inorder, i)
    return root

if __name__ == '__main__':
    root = Node(4)
    root.left = Node(2)
    root.right = Node(6)
    root.left.left = Node(1)
    root.left.right = Node(3)
    root.right.left = Node(5)
    root.right.right = Node(7)
    root = convertBSTMinHeap(root)
    # printLevelOrderTraversal(root)
    preOrder(root)