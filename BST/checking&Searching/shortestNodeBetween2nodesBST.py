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


def shortestDistanceBetween2Nodes(root, node1, node2):
    if not root:
        return
    if not node1:
        return
    if not node2:
        return
    return distance(root, node1) + distance(root, node2)


def distance(root, node):
    if not root:
        return
    if not node:
        return
    count = 0
    current = root
    while current:
        if current.data == node:
            # count += 1
            return count
        elif current.data > node:
            current = current.left
            count += 1
        else:
            current = current.right
            count += 1


if __name__ == '__main__':
    root = None
    root = insert(root, 20)
    insert(root, 10)
    insert(root, 5)
    insert(root, 15)
    insert(root, 30)
    insert(root, 25)
    insert(root, 35)
    a, b = 5, 55
    print(shortestDistanceBetween2Nodes(root, 5, 35))
