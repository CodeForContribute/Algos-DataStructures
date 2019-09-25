class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def Inorder(root):
    if not root:
        return
    Inorder(root.left)
    print(root.data, end=" ")
    Inorder(root.right)


def buildTree(inorder, preorder, start, end):
    if start > end:
        return None
    root = Node(preorder[buildTree.preIndex])
    buildTree.preIndex += 1
    if start == end:
        return root
    index = Search(inorder, start, end, root.data)
    root.left = buildTree(inOrder, preorder, start, index - 1)
    root.right = buildTree(inOrder, preorder, index + 1, end)
    return root


def Search(inorder, start, end, data):
    for i in range(start, end + 1):
        if inorder[i] == data:
            return i


######### Optimised Version ######################################
def buildTreeOptimised(Inorder, PreOrder, start, end, hash_map):
    if start > end:
        return None
    root = Node(PreOrder[buildTreeOptimised.preIndex])
    buildTreeOptimised.preIndex += 1
    if start == end:
        return root
    index = hash_map[preOrder[buildTreeOptimised.preIndex]]
    root.left = buildTreeOptimised(Inorder, PreOrder, start, index - 1, hash_map)
    root.right = buildTreeOptimised(Inorder, PreOrder, index + 1, end, hash_map)
    return root


def buildTreeWrapper(Inorder, Preorder, length):
    hash_map = dict()
    for i in range(length):
        hash_map[Inorder[i]] = i
    return buildTreeOptimised(Inorder, Preorder, 0, length - 1, hash_map)


if __name__ == '__main__':
    inOrder = ['D', 'B', 'E', 'A', 'F', 'C']
    preOrder = ['A', 'B', 'D', 'E', 'C', 'F']
    buildTree.preIndex = 0
    buildTreeOptimised.preIndex = 0
    # root = buildTree(inOrder, preOrder,0, len(inOrder)-1)
    root = buildTreeWrapper(inOrder, preOrder, len(inOrder))
    Inorder(root)
