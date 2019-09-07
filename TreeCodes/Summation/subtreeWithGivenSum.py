class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def subtreeGivenSumUtil(root, cur_sum, sum):
    if not root:
        cur_sum[0] = 0
        return False

    ls = [0]
    rs = [0]
    x = subtreeGivenSumUtil(root.left, ls, sum)
    y = subtreeGivenSumUtil(root.right, rs, sum)
    cur_sum[0] = ls[0] + rs[0]+root.data
    return (x or y) or (cur_sum[0] == sum)




def subtreeGivenSum(root, sum):
    current_sum = [0]
    subtreeGivenSumUtil(root, current_sum, sum)


if __name__ == '__main__':
    if __name__ == '__main__':

        root = Node(8)
        root.left = Node(5)
        root.right = Node(4)
        root.left.left = Node(9)
        root.left.right = Node(7)
        root.left.right.left = Node(1)
        root.left.right.right = Node(12)
        root.left.right.right.right = Node(2)
        root.right.right = Node(11)
        root.right.right.left = Node(3)
        sum = 22

        if subtreeGivenSum(root, sum):
            print("Yes")
        else:
            print("No")
