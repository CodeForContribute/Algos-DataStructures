class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def printPathUtil(node, s, root_data):
    if not node:
        return
    rem = root_data-node.data
    if rem in s:
        print(node.data,rem,end=" ")
        return True
    s.add(node.data)
    res = printPathUtil(node.left, s, root_data) or printPathUtil(node.right,s, root_data)
    s.remove(node.data)
    return res


def isPathSum(root):
    s = set()
    return printPathUtil(root.left,s,root.data) or printPathUtil(root.right, s, root.data)

if __name__ == '__main__':
    root = Node(8)
    root.left = Node(5)
    root.right = Node(4)
    root.left.left = Node(9)
    root.left.right = Node(7)
    root.left.right.left = Node(1)
    root.left.right.right = Node(12)
    root.left.right.right.right = Node(2)
    root.right.right = Node(11)
    root.right.right.left = Node(3)
    print("Yes") if (isPathSum(root)) else print("No") 
