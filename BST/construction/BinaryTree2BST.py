class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def storeInorder(root, inorder):
    """
    Time complexity:O(n)
    :param root:
    :param inorder:
    :return:
    """
    if not root:
        return
    storeInorder(root.left, inorder)
    inorder.append(root.data)
    storeInorder(root.right, inorder)

def countNodes(root):
    """
    Time Complexity:O(n)
    :param root:
    :return:
    """
    if not root:
        return 0
    return countNodes(root.left)+countNodes(root.right)+1

def inorder2BST(inorder, root):
    """
    Time Complexity:O(n)
    :param inorder:
    :param root:
    :return:
    """
    if not root:
        return
    inorder2BST(inorder, root.left)
    root.data = inorder[0]
    inorder.pop(0)
    inorder2BST(inorder, root.right)

def BinaryTree2BST(root):
    """
    Time Complexity:O(n+n+n+nlog(n)) ~ O(nlogn)
    :param root:
    :return:
    """
    if not root:
        return
    n = countNodes(root)
    inorder = []*n
    storeInorder(root, inorder)
    inorder.sort()
    inorder2BST(inorder, root)

def inorder(root):
    if not root:
        return
    inorder(root.left)
    print(root.data,end=" ")
    inorder(root.right)


if __name__ == '__main__':
    root = Node(10)
    root.left = Node(30)
    root.right = Node(15)
    root.left.left = Node(20)
    root.right.right = Node(5)

    # Convert binary tree to BST
    BinaryTree2BST(root)

    print("Following is the inorder traversal of the converted BST")
    inorder(root)




