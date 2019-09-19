class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None



def constructBST12N(start, end):
    listTree = []
    if start > end:
        listTree.append(None)
        return listTree
    for i in range(start, end+1):
        leftSubtree = constructBST12N(start, i-1)
        rightSubtree = constructBST12N(i+1, end)
        for j in range(len(leftSubtree)):
            left = leftSubtree[j]
            for k in range(len(rightSubtree)):
                right = rightSubtree[k]
                node = Node(i)
                node.left = left
                node.right = right
                listTree.append(node)
    return listTree



def preOrder(root):
    if not root:
        return
    print(root.data,end=" ")
    preOrder(root.left)
    preOrder(root.right)