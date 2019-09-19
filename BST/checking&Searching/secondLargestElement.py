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


def secondLargest(root):
    c = [0]
    secondLargestUtil(root, c)


def secondLargestUtil(root, c):
    if not root or c[0] >= 2:
        return
    secondLargestUtil(root.right, c)
    c[0] += 1
    if c[0] == 2:
        print(root.data,end=" ")
        return
    secondLargestUtil(root.left, c)





if __name__ == '__main__':
    root = None
    root = insert(root, 50)
    insert(root, 30)
    insert(root, 20)
    insert(root, 40)
    insert(root, 70)
    insert(root, 60)
    insert(root, 80)
    secondLargest(root)