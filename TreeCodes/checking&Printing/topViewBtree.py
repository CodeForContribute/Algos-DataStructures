class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.hd = 0

def printNodesTopView(root):
    if not root:
        return
    Q = list()
    hash_map = dict()
    Q.append(root)
    hd = 0
    root.hd = 0
    while len(Q):
        temp = Q.pop(0)
        hd = temp.hd
        if hd not in hash_map:
            hash_map[hd] = temp.data
        if temp.left:
            temp.left.hd = hd-1
            Q.append(temp.left)
        if temp.right:
            temp.right.hd = hd + 1
            Q.append(temp.right)
    print(hash_map)
    for i in sorted(hash_map):
        print(hash_map[i], end=" ")


if __name__ == '__main__':
    """ Create following Binary Tree  
            1  
        / \  
        2 3  
        \  
            4  
            \  
            5  
            \  
                6*"""
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.right = Node(4)
    root.left.right.right = Node(5)
    root.left.right.right.right = Node(6)
    print("Following are nodes in top",
          "view of Binary Tree")
    printNodesTopView(root)