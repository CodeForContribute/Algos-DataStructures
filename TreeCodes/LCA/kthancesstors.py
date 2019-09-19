class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

temp = None
def kthNode(root,k, target):
    if not root:
        return False
    if k < 0:
        return False
    # if root.data == target:
    #     print(root.data,end=" ")
    #     return True
    # if root.data == target or temp = kthNode(root.left,k, target )or temp = kthNode(root.right, k, target):
    #     if k > 0:
    #         k -= 1
    #     elif k ==0:
    #         print(root.data,end=" ")
    #         return None
    # return root

if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)

    x = 7
    kthNode(root,1, x)