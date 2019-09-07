class Node:
    def __init__(self, data):
        self.data  = data
        self.left = None
        self.right = None

def ancesstorsNodes(root,target, stack):
    if not root:
        return False
    if root.data == target:
        return True
    if ancesstorsNodes(root.left, target, stack) or ancesstorsNodes(root.right, target, stack):
        # print(root.data)
        stack.append(root.data)
        return True
    return False

if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.left.left.left = Node(7)
    stack = list()
    ancesstorsNodes(root,7, stack)
    while len(stack):
        print(stack.pop(),end=" ")