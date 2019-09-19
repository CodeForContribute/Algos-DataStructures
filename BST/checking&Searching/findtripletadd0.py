class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

############ Expected Time Complexity:O(n^2)
############ Expected Space Complexity:O(log(n))

def convertBSTDLL(root, head, tail):
    if not root:
        return
    if root.left:
        convertBSTDLL(root.left, head, tail)
    root.left = tail
    if tail:
        tail.right = root
    else:
        head = root
    tail = root
    if root.right:
        convertBSTDLL(root.right, head, tail)

def ispresentInDLL(head, tail, sum):
    while head != tail:
        current = head.data + tail.data
        if current == sum:
            return True
        elif current > sum:
            tail = tail.left
        else:
            head = head.right
    return False

def findTripletAddto0(root):
    if not root:
        return False
    head = None
    tail = None
    convertBSTDLL(root, head, tail)
    while head.right != tail and head.data < 0:
        if ispresentInDLL(head.right,tail, -1*head.data):
            return True
        else:
            head = head.right
    return False

def insert(root, data):
    if not root:
        return Node(data)
    if data < root.data:
        root.left = insert(root.left,data)
    if data > root.data:
        root.right = insert(root.right, data)
    return root

if __name__ == '__main__':
    root = None
    root = insert(root, 6)
    root = insert(root, -13)
    root = insert(root, 14)
    root = insert(root, -8)
    root = insert(root, 15)
    root = insert(root, 13)
    root = insert(root, 7)
    if findTripletAddto0(root):
        print("\nPresent")
    else:
        print("Not Present")



