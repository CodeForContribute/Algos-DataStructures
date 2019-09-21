class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def insert(root, data):
    if not root:
        return Node(data)
    if root.data > data:
        root.left = insert(root.left, data)
    if root.data < data:
        root.right = insert(root.right, data)
    return root


def predAndSucGvnKey(root, key):
    if not root:
        return
    predAndSucGvnKey.pre = None
    predAndSucGvnKey.suc = None
    if root.data == key:
        if root.left:
            temp = root.left
            while temp.right:
                temp = temp.right
            predAndSucGvnKey.pre = temp

        if root.right:
            temp = root.right
            while temp.left:
                temp = temp.left
            predAndSucGvnKey.suc = temp
        return
    if root.data > key:
        predAndSucGvnKey.suc = root
        predAndSucGvnKey(root.left, key)
    else:
        predAndSucGvnKey.pre = root
        predAndSucGvnKey(root.right, key)
