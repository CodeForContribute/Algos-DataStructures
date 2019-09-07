class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def buildTree(inorder, preorder, instart, inend):
    preIndex = [0]
    if instart > inend:
        return None
    tnode = Node(preorder[preIndex[0]])
    preIndex[0] += 1
    if instart == inend:
        return tnode
    inIndex = search(inorder, instart, inend, tnode.data)
    tnode.left = buildTree(inorder, preorder,instart, inIndex-1)
    tnode.right = buildTree(inorder,preorder, inIndex+1, inend)
    return tnode


def search(inorder,instart, inend, node_data):
    for i in range(instart, inend+1):
        if inorder[i] == node_data:
            return i

def checkPostOrder(root, postorder, index):
    if not root:
        return index
    index = checkPostOrder(root.left, postorder, index)
    index = checkPostOrder(root.right, postorder, index)
    if root.data == postorder[index]:
        index += 1
    else:
        return -1
    return index

if __name__ == '__main__':
    inOrder = [4, 2, 5, 1, 3]
    preOrder = [1, 2, 4, 5, 3]
    postOrder = [4, 5, 2, 3, 1]
    root = buildTree(inOrder, preOrder, 0, len(inOrder))
    index = checkPostOrder(root, postOrder,0)
    if index == len(inOrder):
        print("YES")
    else:
        print("NO")


