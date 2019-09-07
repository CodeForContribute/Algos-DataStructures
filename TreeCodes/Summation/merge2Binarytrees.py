class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def inorder(root):
    if not root:
        return
    inorder(root.left)
    print(root.data,end=" ")
    inorder(root.right)

#REcursive Solution
def Merge2BinaryTrees(root1, root2):
    if not root1 and not root2:
        return
    if not root1:
        return root2
    if not root2:
        return root1
    root1.data += root2.data
    root1.left = Merge2BinaryTrees(root1.left, root2.left)
    root2.right = Merge2BinaryTrees(root1.right, root2.right)
    return root1

#iterative Solution
def Merge2Binarytrees(root1, root2):
    if not root1 and not root2:
        return
    if not root1:
        return root2
    if not root2:
        return root1
    stack = list()
    stack.append(root1)
    stack.append(root2)
    while len(stack):
        temp1 = stack.pop()
        temp2 = stack.pop()
        if temp1 and temp2:
            temp1.data += temp2.data
        temp1.left = temp1.left if temp1.left else Node(0)
        temp2.left = temp2.left if temp2.left else Node(0)
        temp1.right = temp1.right if temp1.right else Node(0)
        temp2.right = temp2.right if temp2.right else Node(0)
        stack.append(temp1.left)
        stack.append(temp2.left)
        stack.append(temp1.right)
        stack.append(temp2.right)
    # return root1

if __name__ == '__main__':
    root1 = Node(1)
    root1.left = Node(2)
    root1.right = Node(3)
    root1.left.left = Node(4)
    root1.left.right = Node(5)
    root1.right.right = Node(6)

    root2 = Node(4)
    root2.left = Node(1)
    root2.right = Node(7)
    root2.left.left = Node(3)
    root2.right.left = Node(2)
    root2.right.right = Node(6)

    # root3 = Merge2BinaryTrees(root1, root2)
    # print("The Merged Binary Tree is:")
    # inorder(root3)
    print("\n")
    root3 = Merge2Binarytrees(root1, root2)
    print("The Merged Binary Tree is:")
    inorder(root3)
