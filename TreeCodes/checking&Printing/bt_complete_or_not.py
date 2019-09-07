class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def isBinaryTreeComplete(root):
    if not root:
        return True
    queue = list()
    flag = False
    queue.append(root)
    while len(queue):
        temp = queue.pop(0)
        if temp.left:
            if flag:
                return False
            queue.append(temp.left)
        else:
            flag = True

        if temp.right:
            if flag:
                return False
            queue.append(temp.right)
        else:
            flag = False
    return True
