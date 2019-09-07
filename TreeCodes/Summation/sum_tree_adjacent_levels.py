class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def maxSumTreeAdjLevels(root):
    Queue = list()
    level = 0
    Queue.append(root)
    arr = [0]*100
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
    if level > 1:
        dp[1] = max(arr[1], arr[0])
        for i in range(2, level):
            dp[i] = max(arr[i]+dp[i-2], dp[i-1])
    return dp[level-1]

if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.right.left = Node(4)
    root.right.left.right = Node(50)
    root.right.left.right.left = Node(6)
    print(maxSumTreeAdjLevels(root))