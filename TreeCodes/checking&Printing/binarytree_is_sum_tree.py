class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
################################ Time complexity : O(n^2) in worst case ###################
def Sum(node):
    if not node:
        return 0
    return Sum(node.left)+Sum(node.right)+node.data

def isSumTree(node):
    if node is None or (node.left is None and node.right is None):
        return True
    leftSum = Sum(node.left)
    rightSum = Sum(node.right)
    if node.data == leftSum + rightSum and (isSumTree(node.left) and isSumTree(node.right)):
        return True
    return False
########################################################################################################
########### Time Complexity : O(n) ###############################################################
def isLeaf(node):
    if not node:
        return False
    if node.left is None and node.right is None:
        return True
    return False

def isSumTreelessTime(node):
    if not node or isLeaf(node):
        return True
    if isSumTreelessTime(node.left) and isSumTreelessTime(node.right):
        if node.left is None:
            left_sum = 0
        elif isLeaf(node.left):
            left_sum = node.left.data
        else:
            left_sum = 2*node.left.data
        if node.right is None:
            right_sum = 0
        elif isLeaf(node.right):
            right_sum = node.right.data
        else:
            right_sum = 2*node.right.data
        return node.data == left_sum + right_sum
    return False


if __name__ == '__main__':
    root = Node(26)
    root.left = Node(10)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(6)
    root.right.right = Node(3)
    if isSumTree(root):
        print("The given tree satisfies the",
              " sum  Tree property ")
    else:
        print("The given tree does not satisfy",
              "the sum Tree property ")