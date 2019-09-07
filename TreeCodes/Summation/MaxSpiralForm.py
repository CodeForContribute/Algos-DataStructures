class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def MaxSumSpiralForm(root):
    if not root:
        return 0
    stack1 = list()
    stack2 = list()
    arr = list()
    stack1.append(root)
    while len(stack1) or len(stack2):
        while len(stack1):
            temp = stack1.pop()
            arr.append(temp.data)
            if temp.left:
                stack2.append(temp.left)
            if temp.right:
                stack2.append(temp.right)
        while len(stack2):
            temp2 = stack2.pop()
            arr.append(temp2.data)
            if temp2.left:
                stack1.append(temp2.left)
            if temp2.right:
                stack1.append(temp2.right)

    return maxSum(arr, len(arr))

def maxSum(arr, n):
    import sys
    max_ending_here = -sys.maxsize
    max_so_far = -sys.maxsize

    for i in range(n):
        if max_ending_here < 0:
            max_ending_here = arr[i]
        else:
            max_ending_here += arr[i]
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far

if __name__ == '__main__':
    root = Node(-2)
    root.left = Node(-3)
    root.right = Node(4)
    root.left.left = Node(5)
    root.left.right = Node(1)
    root.right.left = Node(-2)
    root.right.right = Node(-1)
    root.left.left.left = Node(-3)
    root.right.right.right = Node(2)
    print(MaxSumSpiralForm(root))