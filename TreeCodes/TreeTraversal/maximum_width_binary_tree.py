class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


############ Using Level Order Traversal ###############
######### Time Complexity:O(n^2) #############
def height(root):
    if not root:
        return 0
    lheight = height(root.left)
    rheight = height(root.right)
    if lheight > rheight:
        return lheight+1
    else:
        return rheight+1

def getWidth(root, level):
    if not root:
        return 0
    if level == 1:
        return 1
    elif level > 1:
        return getWidth(root.left, level-1) + getWidth(root.right, level-1)

def getMaxwidth(root):
    max_width = 0
    for level in range(1,height(root)):
        width = getWidth(root,level)
        if width > max_width:
            max_width = width
    return max_width
#################### Using Level Order Traversal ##########
######Time Complexity:O(n) ###########

def getMaxWidthQueue(root):
    if not root:
        return 0
    queue = list()
    max_width = 0
    queue.append(root)
    while queue:
        count = len(queue)
        max_width = max(count,max_width)
        while count:
            temp = queue.pop(0)
            if temp.left:
                queue.append(temp.left)
            if temp.right:
                queue.append(temp.right)
            count -= 1
    return max_width


if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.right = Node(8)
    root.right.right.left = Node(6)
    root.right.right.right = Node(7)
    print(getMaxwidth(root))
    print("\n")
    print(getMaxWidthQueue(root))