class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Using 2 Stack
def IterativePostOrderTraversal(root):
    if not root:
        return
    Stack1 = []
    Stack2 = []
    Stack1.append(root)
    while len(Stack1):
        temp = Stack1.pop()
        Stack2.append(temp)
        if temp.left is not None:
            Stack1.append(temp.left)
        if temp.right is not None:
            Stack1.append(temp.right)
    # Print all the nodes from the stack2 that will give hte post order of the tree
    while len(Stack2):
        temp = Stack2.pop()
        print(temp.data,end=" ")

# Using 1 stacks:
def peek(stack):
    if len(stack) > 0:
        return stack[-1]
    else:
        return None
def IterativePostOrderTraversal_1_Stack(root):
    if not root:
        return

    Stack = list()
    while True:
        while root:
            if root.right is not None:
                Stack.append(root.right)
            Stack.append(root)
            root = root.left
        root = Stack.pop()
        if root.right is not None and root.right == peek(Stack):
            Stack.pop()
            Stack.append(root)
            root = root.right
        else:
            print(root.data,end=" ")
            root = None
        if len(Stack) <= 0:
            break

def postorderTraversal(self, A):
    result = []
    d = [A]
    while d:
        node = d.pop()
        if node:
            result.append(node.val)
            d.append(node.left)
            d.append(node.right)
    return result[::-1]

if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    IterativePostOrderTraversal(root)
    print("\n")
    IterativePostOrderTraversal_1_Stack(root)