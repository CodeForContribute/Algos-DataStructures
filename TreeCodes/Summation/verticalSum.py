class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class LLNode:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

######## Time Complexity : O(n) ###########
######### Space Complexity: O(n) ################
def verticalSumUtil(root, hd, hash_map):
    if not root:
        return
    verticalSumUtil(root.left, hd-1, hash_map)
    if hd not in hash_map:
        hash_map[hd] = 0
    hash_map[hd] += root.data
    verticalSumUtil(root.right, hd+1, hash_map)

def verticalSum(root):
    if not root:
        return 0
    hash_map = dict()
    verticalSumUtil(root, 0, hash_map)
    for value in hash_map.keys():
        print(hash_map[value])

######## Time Complexity : O(n) ###########
def verticalSumDLLUtil(root, sumNode):
    sumNode.data = sumNode.data + root.data
    if root.left:
        if not sumNode.prev:
            sumNode.prev = LLNode(0)
            sumNode.prev.next = sumNode
        verticalSumDLLUtil(root.left, sumNode.prev)
    if root.right:
        if not sumNode.next:
            sumNode.next = LLNode(0)
            sumNode.next.prev = sumNode
        verticalSumDLLUtil(root.right, sumNode.next)

def verticalSumDLL(root):
    sumNode = LLNode(0)
    verticalSumDLLUtil(root, sumNode)
    while sumNode.prev is not None:
        sumNode = sumNode.prev
    while sumNode:
        print(sumNode.data,end=" ")
        sumNode = sumNode.next

if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    # root.right.left.right = Node(8)
    # root.right.right.right = Node(9)
    verticalSum(root)
    print("\n")
    verticalSumDLL(root)