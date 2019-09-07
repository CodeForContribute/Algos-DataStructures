class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

################# Time Complexity : O(N) ##################################################
def level(root, node, lev):
    if not root:
        return 0
    if root == node:
        return lev
    l = level(root.left, node, lev + 1)
    if l != 0:
        return l
    return level(root.right, node, lev + 1)


def isSibling(root, node1, node2):
    if not root:
        return False
    return ((root.left == node1 and root.right == node2) or (root.left == node2 and root.right == node1)) \
           or isSibling(root.left, node1, node2) or isSibling(root.right, node1, node2)


def isCousin(root, a, b):
    if level(root, a, 1) == level(root, b, 1) and not isSibling(root, a, b):
        return True
    else:
        return False

if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.left.right.right = Node(15)
    root.right.left = Node(6)
    root.right.right = Node(7)
    root.right.left.right = Node(8)

    node1 = root.left.right
    node2 = root.right.right

    print("Yes" if isCousin(root, node1, node2) == 1 else "No")
