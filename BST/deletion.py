class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def inorder(root):
    if not root:
        return
    inorder(root.left)
    print(root.data,end=" ")
    inorder(root.right)


def insert(root, node):
    if not root:
        return node
    if root.data > node.data:
        root.left = insert(root.left, node)
    else:
        root.right = insert(root.right, node)
    return root


def search(root, data):
    if not root:
        return root
    if root.data == data:
        return root
    if root.data < data:
        return search(root.left, data)
    else:
        return search(root.right, data)


def findMinVal(root):
    current = root
    while current.left:
        current = current.left
    return current


def delete(root, data):
    if not root:
        return root
    if root.data > data:
        root.left = delete(root.left, data)
    elif root.data < data:
        root.right = delete(root.right, data)
    else:
        if not root.left:
            temp = root.right
            root = None
            return temp
        elif not root.right:
            temp = root.left
            root = None
            return temp
        temp = findMinVal(root.right)
        root.data = temp.data
        # temp = None
        # return temp
        root.right = delete(root.right, temp.data)
    return root

############# Optimised ###################################
def deleteNodes(root, k):
    if not root:
        return root
    if root.data > k:
        root.left = deleteNodes(root.left, k)
        return root
    elif root.data < k:
        root.right = deleteNodes(root.right, k)
        return root
    if not root.left:
        temp = root.right
        del root
        return temp
    elif not root.right:
        temp = root.left
        del root
        return temp
    else:
        sucparent = root.right
        suc = root.right
        while suc.left:
            sucparent = suc
            suc = suc.left

    sucparent.left = suc.right
    root.data = suc.data
    del suc
    return root


if __name__ == '__main__':
    root = None
    root = insert(root, Node(50))
    root = insert(root, Node(30))
    root = insert(root, Node(20))
    root = insert(root, Node(40))
    root = insert(root, Node(70))
    root = insert(root, Node(60))
    root = insert(root, Node(80))

    print("Inorder traversal of the given tree")
    inorder(root)
    print("\nDelete 20" )
    root = delete(root, 20)
    print("Inorder traversal of the modified tree")
    inorder(root)
    print("\nDelete 30")
    delete(root, 30)
    print("Inorder traversal of the modified tree")
    inorder(root)
    print("\nDelete 50")
    deleteNodes(root, 50)
    print("Inorder traversal of the modified tree")
    inorder(root)
