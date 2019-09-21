class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def iterativeInsert(root, data):
    if not data:
        return
    if not root:
        root = Node(data)
        return root
    current = root
    while current:
        if current.data > data:
            if current.left:
                current = current.left
            else:
                current.left = Node(data)
                break
        if current.data < data:
            if current.right:
                current = current.right
            else:
                current.right = Node(data)
                break


def iterativesearch(root, data):
    if not root:
        return
    if not data:
        return
    current = root
    while current:
        if data == current.data:
            return True
        elif current.data < data:
            current = current.right
        elif current.data > data:
            current = current.left
    return False


def inorder(root):
    if not root:
        return
    inorder(root.left)
    print(root.data, end=" ")
    inorder(root.right)


if __name__ == '__main__':
    root = None
    root = iterativeInsert(root, 50)
    iterativeInsert(root, 30)
    iterativeInsert(root, 20)
    iterativeInsert(root, 40)
    iterativeInsert(root, 70)
    iterativeInsert(root, 60)
    iterativeInsert(root, 80)
    inorder(root)
    print("\n")
    if iterativesearch(root, 20):
        print("Yes")
    else:
        print("No")
