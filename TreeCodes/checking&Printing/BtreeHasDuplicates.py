class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def checkDuplicates(root):
    if not root:
        return
    s = set()
    return checkDuplicatesUtil(root, s)

def checkDuplicatesUtil(root, s):
    if not root:
        return False

    if root.data in s:
        return True
    s.add(root.data)
    return checkDuplicatesUtil(root.left, s) or checkDuplicatesUtil(root.right, s)

if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(2)
    root.left.left = Node(3)
    if checkDuplicates(root):
        print("Yes")
    else:
        print("No") 
