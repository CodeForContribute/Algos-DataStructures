class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


############## O(n^2) #####################################
# def incrementPreIndex():
#     constructBSTPreUtil.preIndex += 1
#
#
# def getPreIndex():
#     return constructBSTPreUtil.preIndex


# def constructBSTPreUtil(pre, preIndex, high, size):
#     if preIndex[0] >= size :
#         return None
#     root = Node(pre[preIndex[0]])
#     preIndex[0] += 1
#     if preIndex[0] == high:
#         return root
#     for i in range(preIndex[0], high + 1):
#         if pre[i] > root.data:
#             break
#     root.left = constructBSTPreUtil(root.left, preIndex,  i - 1, size)
#     root.right = constructBSTPreUtil(root.right, i , high, size)
#     return root
#
#
# def constructBSTPre(pre):
#     size = len(pre)
#     preIndex = [0]
#     return constructBSTPreUtil(pre, preIndex, size - 1, size)


####################### Optimised:O(n) ######################################
######################## Recursive Solution #################################
import sys
INT_MIN = -sys.maxsize
INT_MAX = sys.maxsize

def getPreIndex():
    return constructBSTUtil.preIndex

def increamentPreIndex():
    constructBSTUtil.preIndex += 1

def constructBSTUtil(pre, target, mini, maxi, size):
    if getPreIndex() >= size:
        return None
    root = None
    if mini < target < maxi:
        root = Node(target)
        increamentPreIndex()
        if getPreIndex() < size:
            root.left = constructBSTUtil(pre, pre[getPreIndex()],mini, target, size)
            root.right = constructBSTUtil(pre, pre[getPreIndex()], target, maxi, size)
    return root


def constructBSTPre(pre):
    constructBSTUtil.preIndex = 0
    size = len(pre)
    return constructBSTUtil(pre, pre[0],INT_MIN, INT_MAX, size)

############################# Iterative Solution ##############################################################
def constructBSTIterative(pre, size):
    stack = []
    root = Node(pre[0])
    stack.append(root)
    for i in range(1, size):
        temp = None
        while len(stack) and pre[i] > stack[-1].data:
            temp = stack.pop()

        if temp:
            temp.right = Node(pre[i])
            stack.append(temp.right)
        else:
            node = stack[-1].left = Node(pre[i])
            stack.append(node)
    return root


def preOrder(root):
    if not root:
        return
    print(root.data, end=" ")
    preOrder(root.left)
    preOrder(root.right)


if __name__ == '__main__':
    pre = [10, 5, 1, 7, 40, 50]
    root = constructBSTIterative(pre, len(pre))
    preOrder(root)
