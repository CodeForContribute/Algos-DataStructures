class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def insert(root, data):
    if not root:
        return Node(data)
    if root.data < data:
        root.right = insert(root.right, data)
    if root.data > data:
        root.left = insert(root.left, data)
    return root


def storeInorder(root, inorder):
    if not root:
        return
    storeInorder(root.left, inorder)
    inorder.append(root.data)
    storeInorder(root.right, inorder)


# Time Complexity is O(n)
# Aux Space : O(n)->Using array
def findPairSum(root, Sum):
    if not root:
        return
    inorder = list()
    storeInorder(root, inorder)
    i = 0
    j = len(inorder) - 1
    while i < j:
        if inorder[i] + inorder[j] == Sum:
            print(inorder[i], inorder[j])
            i += 1
            j -= 1
        elif inorder[i] + inorder[j] < Sum:
            i += 1
        else:
            j -= 1


# Another solution Using set
def findPairsumUsingSet(root, Sum):
    if not root:
        return
    s = set()
    if not findPairsumUsingSetUtil(root, Sum, s):
        print("Pair not Found!")


def findPairsumUsingSetUtil(root, Sum, s):
    if not root:
        return
    if findPairsumUsingSetUtil(root.left, Sum, s):
        return True
    if s and Sum - root.data in s:
        print(Sum - root.data, root.data)
        return True
    else:
        s.add(root.data)
    return findPairsumUsingSetUtil(root.right, Sum, s)


if __name__ == '__main__':
    if __name__ == '__main__':
        root = None
        root = insert(root, 15)
        root = insert(root, 10)
        root = insert(root, 20)
        root = insert(root, 8)
        root = insert(root, 12)
        root = insert(root, 16)
        root = insert(root, 25)
        root = insert(root, 10)
        summ = 33
        findPairSum(root, summ)
        findPairsumUsingSet(root, summ)
