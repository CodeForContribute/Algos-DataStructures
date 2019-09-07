class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def printBinaryTreeVerticalOrder(root):
    if not root:
        return
    Q = list()
    hash_map = dict()# create a map to store nodes at a particular
    # horizontal distance
    hd_node = dict()# To store the horizontal distance of nodes from root
    Q.append(root)
    hd_node[root] = 0
    hash_map[0] = [root.data]
    while len(Q):
        temp = Q.pop(0)
        if temp.left:
            Q.append(temp.left)
            hd_node[temp.left] = hd_node[temp]-1
            hd = hd_node[temp.left]
            if not hash_map.get(hd):
                hash_map[hd] = []
            hash_map[hd].append(temp.left.data)
        if temp.right:
            Q.append(temp.right)
            hd_node[temp.right] = hd_node[temp] + 1
            hd = hd_node[temp.right]
            if not hash_map.get(hd):
                hash_map[hd] = []
            hash_map[hd].append(temp.right.data)
    import collections
    sorted_m =collections.OrderedDict(sorted(hash_map.items()))
    # print(sorted_m)
    for i in sorted_m.values():
        for j in i:
            print(j,end=" ")
        print()


if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    root.right.left.right = Node(8)
    root.right.right.left = Node(10)
    root.right.right.right = Node(9)
    root.right.right.left.right = Node(11)
    root.right.right.left.right.right = Node(12)
    print("Vertical order traversal is ")
    printBinaryTreeVerticalOrder(root)