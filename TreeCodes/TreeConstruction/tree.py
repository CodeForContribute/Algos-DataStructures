class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def Inorder(self, root):
        if not root:
            return
        self.Inorder(root.left)
        print(root.data, end=" ")
        self.Inorder(root.right)

    def Preorder(self, root):
        if not root:
            return
        print(root.data, end=" ")
        self.Preorder(root.left)
        self.Preorder(root.right)

    def PostOrder(self, root):
        if not root:
            return
        self.PostOrder(root.left)
        self.PostOrder(root.right)
        print(root.data, end=" ")
