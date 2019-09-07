class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None


def MaxLevelSum(root):
    if not root:
        return
    sum = 0
    level = 0
    arr = [0]*100
    Queue = list()
    Queue.append(root)
    while len(Queue):
        size = len(Queue)
        for i in range(size):
            temp = Queue.pop(0)
            arr[level] += temp.data
            if temp.left:
                Queue.append(temp.left)
            if temp.right:
                Queue.append(temp.right)
        level += 1

    dp = [0]*level
    dp[0] = arr[0]
    for i in range(1,level):
        dp[i] = max(dp[i-1],arr[i])
    print(dp[level-1])

if __name__ == '__main__':
    root = Node(4)
    root.left = Node(2)
    root.right = Node(-5)
    root.left.left = Node(-1)
    root.left.right = Node(3)
    root.right.right = Node(-2)
    root.right.right.left = Node(6)
    # root.right.right.right = Node(7)
    MaxLevelSum(root)
