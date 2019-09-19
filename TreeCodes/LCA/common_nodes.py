class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None



def commonNodes(root, n1, n2):
    if n1 < 0 or n2 < 0:
        return
    if not root:
        return
    lca = findLca(root, n1, n2)
    if lca:
        printAncessotrs(root, lca.data)


def findLca(root, n1, n2):
    if not root:
        return None
    if n1<0 or n2 < 0:
        return
    if root.data == n1 or root.data == n2:
        return root
    lca_left = findLca(root.left, n1, n2)
    lca_right = findLca(root.right, n1, n2)
    if lca_left and lca_right:
        return root
    return lca_left if lca_left else lca_right

def printAncessotrs(root, target):
    if not root:
        return False
    if not target:
        return False
    if root.data == target:
        print(root.data,end=" ")
        return True
    if printAncessotrs(root.left, target) or printAncessotrs(root.right, target):
        print(root.data,end=" ")
        return True
    return False


if __name__ == '__main__':

    # Let us create binary tree given  
    # in the above example  
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    root.left.left.left = Node(8)
    root.right.left.left = Node(9)
    root.right.left.right = Node(10)
    commonNodes(root, 9, 7)
    # if commonNodes(root, 9, 7) is False:
    #     print("No Common nodes")