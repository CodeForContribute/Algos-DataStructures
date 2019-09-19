class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None


def LCA(n1, n2):
    if not n1 or not n2:
        return
    hash_map = dict()
    while n1:
        hash_map[n1] = True
        n1 = n1.parent

    while n2:
        if n2 in hash_map:
            return n2.data
        n2 = n2.parent

    return None

def depth(node):
    d = -1
    while node:
        d += 1
        node = node.parent
    return d

def LCA_node(n1, n2):
    d1 = depth(n1)
    d2 = depth(n2)
    diff = d1-d2
    if diff < 0:
        n1, n2 = n2, n1
        diff = -diff
    while diff:
        n1 = n1.parent
        diff -= 1
    while n1 and n2:
        if n1 == n2:
            return n1.data
        n1 = n1.parent
        n2 = n2.parent
    return None

if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.left.parent = root
    root.right = Node(3)
    root.right.parent = root

    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    root.left.left.parent = root.left
    root.left.right.parent = root.left
    root.right.left.parent = root.right
    root.right.right.parent = root.right

    n1 = root.right.left
    n2 = root.right.right

    lca = LCA(n1, n2)
    print(lca)
    lca1 = LCA_node(n1, n2)
    print(lca1)

