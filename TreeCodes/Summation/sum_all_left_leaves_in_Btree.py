class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def isLeaf(root):
    if not root:
        return False
    if not root.left and not root.right:
        return True


#########################################3
def sumLeftLeaves(root):
    res = 0
    if root:
        if isLeaf(root.left):
            res += root.left.data
        else:
            res += sumLeftLeaves(root.left)
        res += sumLeftLeaves(root.right)
    return res


################# LeftLeavesSum ############
def leftLeavesSumUtil(root, isleft, sum):
    if not root:
        return
    if not root.left and not root.right and isleft:
        sum[0] += root.data
    leftLeavesSumUtil(root.left, 1, sum)
    leftLeavesSumUtil(root.right, 0, sum)


def leftLeavesSum(root):
    sum = [0]
    leftLeavesSumUtil(root, 0, sum)
    return sum[0]


################# LeftLeavesSum iterative Approach ############
def leftLeavesSumIterative(root):
    if not root:
        return
    sum = 0
    stack = list()
    stack.append(root)
    while len(stack):
        temp = stack.pop()
        if temp.left:
            stack.append(temp.left)
            if not temp.left.left and not temp.left.right:
                sum += temp.left.data
        if temp.right:
            stack.append(temp.right)
    return sum

def rightLeavesSumIterative(root):
    if not root:
        return
    sum = 0
    stack = list()
    stack.append(root)
    while len(stack):
        temp = stack.pop()
        if temp.left:
            stack.append(temp.left)
        if temp.right:
            stack.append(temp.right)
            if not temp.right.left and not temp.right.right:
                sum += temp.right.data
    return sum


if __name__ == '__main__':
    root = Node(9)
    root.left = Node(8)
    root.right = Node(6)
    # root.right.left = Node(1)
    root.right.right = Node(52)
    # root.right.right.left = Node(50)
    root.left.left = Node(5)
    root.left.right = Node(2)
    # root.left.right.right = Node(12)
    print("Sum of left leaves is", sumLeftLeaves(root))
    print("Sum of left leaves is", leftLeavesSum(root))
    print("Sum of left leaves is", rightLeavesSumIterative(root))

