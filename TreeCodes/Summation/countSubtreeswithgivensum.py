class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

###### Using 2 functions recusions ####################
def countSubtrees(root, x):
    if not root:
        return 0
    count = [0]
    countSubtreesUtil(root, count, x)
    return count[0]

def countSubtreesUtil(root, count, x):
    if not root:
        return 0
    ls = countSubtreesUtil(root.left, count, x)
    rs = countSubtreesUtil(root.right, count, x)
    sum = ls + rs + root.data
    if sum  == x:
        count[0] += 1
    return sum

def countSubtreeUtil(root, x):
    count = [0]
    node = [root]
    ls = [0]
    rs = [0]
    if not root:
        return 0
    ls[0] += countSubtreeUtil(node[0].left, x)
    rs[0] += countSubtreeUtil(node[0].right, x)
    if ls[0] + rs[0] + node[0].data == x:
        count[0] += 1
    if node[0] != root:
        return ls[0] + node[0].data + rs[0]
    else:
        return count[0]

if __name__ == '__main__':
    if __name__ == '__main__':
        # binary tree creation      
        #         5  
        #         / \  
        #     -10     3  
        #     / \ / \  
        #     9 8 -4 7  
        root = Node(5)
        root.left = Node(-10)
        root.right = Node(3)
        root.left.left = Node(9)
        root.left.right = Node(8)
        root.right.left = Node(-4)
        root.right.right = Node(7)

        x = 7

        print("Count =",countSubtrees(root, x))
        print("Count =",countSubtreeUtil(root, x))

