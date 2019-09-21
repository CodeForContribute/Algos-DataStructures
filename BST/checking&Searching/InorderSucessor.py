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


def InorderSuccessor(root, target, Suc):
    if not root:
        return
    while root:
        if root.data == target:
            if root.right:
                Suc[0] = root.right
                while Suc[0].left:
                    Suc[0] = Suc[0].left
            return
        elif root.data > target:
            Suc[0] = root
            root = root.left
        else:
            root = root.right


if __name__ == '__main__':
    key = 80  # Key to be searched in BST

    # Let us create following BST
    #             50
    #         / \
    #         / \
    #         30     70
    #         / \     / \
    #     / \ / \
    #     20 40 60 80

    root = None
    root = insert(root, 50)
    insert(root, 30)
    insert(root, 20)
    insert(root, 40)
    insert(root, 70)
    insert(root, 60)
    insert(root, 80)
    Suc = [None]
    InorderSuccessor(root, key, Suc)
    if Suc[0]:
        print("Successor is:", Suc[0].data)
    else:
        print("Successor is: -1")
