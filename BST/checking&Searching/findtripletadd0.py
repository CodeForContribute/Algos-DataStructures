class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def insert(root, data):
    if not root:
        return Node(data)
    if data < root.data:
        root.left = insert(root.left, data)
    if data > root.data:
        root.right = insert(root.right, data)
    return root

############ Expected Time Complexity:O(n^2)
############ Expected Space Complexity:O(log(n))
def ConvertBSTDLL(root, head, tail):
    if not root:
        return
    if root.left:
        ConvertBSTDLL(root.left, head, tail)
    root.left = tail[0]
    if tail[0]:
        tail[0].right = root
    else:
        head[0] = root
    tail[0] = root
    if root.right:
        ConvertBSTDLL(root.right, head, tail)


def isPresentInDLL(head, tail, Sum):
    while head[0] != tail[0]:
        current = head[0].data + tail[0].data
        if current == Sum:
            print(current, Sum)
            return True
        elif current > Sum:
            tail[0] = tail[0].left
        else:
            head[0] = head[0].right
    return False

def findTripletAddto0(root):
    if not root:
        return False
    head = [None]
    tail = [None]
    # Sum = 0
    ConvertBSTDLL(root, head, tail)
    while head[0].right != tail[0] and head[0].data < 0:
        if isPresentInDLL(head, tail, -1 * head[0].data):
            return True
        else:
            head[0] = head[0].right

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



