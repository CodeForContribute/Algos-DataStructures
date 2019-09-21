class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Time Complexity:O(n)
# Aux space: O(log(n))
def findSumPairs(root, Sum):
    if not root:
        return
    root1 = root
    root2 = root
    stack1 = []
    stack2 = []
    while True:
        while root1:
            stack1.append(root1)
            root1 = root1.left
        while root2:
            stack2.append(root2)
            root2 = root2.right
        if not len(stack1) or not len(stack2):
            # print("Pairs not Found!")
            break
        top1 = stack1[-1]
        top2 = stack2[-1]
        if top1.data + top2.data == Sum:
            return top1.data, top2.data
            stack1.pop()
            stack2.pop()
            root1 = top1.right
            root2 = top2.left
        elif top1.data + top2.data < Sum:
            stack1.pop()
            root1 = top1.right
        else:
            stack2.pop()
            root2 = top2.left
    return "Pairs Not Found!"


if __name__ == '__main__':
    root = Node(15)
    root.left = Node(10)
    root.right = Node(20)
    root.left.left = Node(8)
    root.left.right = Node(12)
    root.right.left = Node(16)
    root.right.right = Node(25)

    target = 41
    print(findSumPairs(root, target))
