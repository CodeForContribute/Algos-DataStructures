class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def sumNodesOnlongestPathRoot(root):
    # if not root:
    #     return 0
    import sys
    max_sum = [-sys.maxsize]
    max_len = [0]
    sumNodesOnlongestPathRootUtil(root, 0, 0, max_len, max_sum)
    return max_sum[0]


def sumNodesOnlongestPathRootUtil(root, sum, len, max_len, max_sum):
    if not root:
        if max_len[0] < len:
            max_len[0] = len
            max_sum[0] = sum
        elif max_len[0] == len and max_sum[0] < sum:
            max_sum[0] = sum
        return
    sumNodesOnlongestPathRootUtil(root.left, sum + root.data, len + 1, max_len, max_sum)
    sumNodesOnlongestPathRootUtil(root.right, sum + root.data, len + 1, max_len, max_sum)


if __name__ == '__main__':
    root = Node(4)  # 4      
    root.left = Node(2)  # / \      
    root.right = Node(5)  # 2 5      
    root.left.left = Node(7)  # / \ / \      
    root.left.right = Node(1)  # 7 1 2 3  
    root.right.left = Node(2)  # /          
    root.right.right = Node(3)  # 6          
    root.left.right.left = Node(6)

    print("Sum = ", sumNodesOnlongestPathRoot(root))
