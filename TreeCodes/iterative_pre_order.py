class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def IterativePreOrderTraversal(root):
    if not root:
        return
    Stack = list()
    Stack.append(root)
    while len(Stack):
        temp = Stack.pop()
        print(temp.data, end=" ")
        if temp.right is not None:
            Stack.append(temp.right)
        if temp.left is not None:
            Stack.append(temp.left)

def PreOrderTraversal(root):
    if not root:
        return
    print(root.data, end=" ")
    PreOrderTraversal(root.left)
    PreOrderTraversal(root.right)


if __name__ == '__main__':
    root = Node(10)
    root.left = Node(8)
    root.right = Node(2)
    root.left.left = Node(3)
    root.left.right = Node(5)
    root.right.left = Node(2)
    IterativePreOrderTraversal(root)
    print("\n")
    PreOrderTraversal(root)