class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def insert(root, data):
    if not root:
        return Node(data)
    if root.data > data:
        root.left = insert(root.left, data)
    if root.data < data:
        root.right = insert(root.right, data)
    return root
############ Time Complexity:O(n) ####################################################
def seqExists(root, seq, n):
    if not root:
        return
    index = [0]
    seqExistsUtil(root, seq, index)
    if index[0] == n:
        return True
    else:
        return False


def seqExistsUtil(root, seq, index):
    if not root:
        return
    seqExistsUtil(root.left, seq, index)
    if index[0] < n:
        if root.data == seq[index[0]]:
            index[0] += 1
        seqExistsUtil(root.right, seq, index)
#############################################################################################################
if __name__ == '__main__':
    root = None
    root = insert(root, 8)
    root = insert(root, 10)
    root = insert(root, 3)
    root = insert(root, 6)
    root = insert(root, 1)
    root = insert(root, 4)
    root = insert(root, 7)
    root = insert(root, 14)
    root = insert(root, 13)

    seq = [4, 6, 8,12]
    n = len(seq)
    if seqExists(root, seq, n):
        print("Yes")
    else:
        print("No")
