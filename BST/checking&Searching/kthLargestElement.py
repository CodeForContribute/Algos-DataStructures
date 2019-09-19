class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def insert(root, data):
    if not root:
        return Node(data)
    if root.data < data:
        root.right= insert(root.right, data)
    if root.data > data:
        root.left = insert(root.left, data)
    return root
#################Time Complexity:O(h+k) ################################################
def kthLargestElement(root, k):
    if not root:
        return None
    if k <= 0:
        return None
    c = [0]
    kthLargestElementUtil(root, c, k)


def kthLargestElementUtil(root, c, k):
    if not root or c[0] >= k:
        return
    kthLargestElementUtil(root.right, c, k)
    c[0] += 1
    if c[0] == k:
        print(root.data,end=" ")
        return
    kthLargestElementUtil(root.left, c, k)

##################################################################################################################
## Using reverse Morris Traversal ####################################################


def kthLargestElementConstantSpace(root, k):
    if not root:
        return
    if k <= 0:
        return
    count = 0
    current = root
    while current:
        if not current.right:
            count += 1
            if count == k:
                klargest = current
            current = current.left
        else:
            suc = current.right
            while suc.left and suc.left != current:
                suc = suc.left
            if not suc.left:
                suc.left = current
                current = current.right
            else:
                suc.left = None
                count += 1
                if count == k:
                    klargest = current
                current = current.left
    return klargest





if __name__ == '__main__':
    root = None
    root = insert(root, 50)
    insert(root, 30)
    insert(root, 20)
    insert(root, 40)
    insert(root, 70)
    insert(root, 60)
    insert(root, 80)
    kthLargestElement(root, 5)