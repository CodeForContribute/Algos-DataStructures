class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def leavesSameLevelOrNot(root):
    if not root:
        return True
    q = list()
    q.append(root)
    import sys
    result = sys.maxsize
    level = 0
    while len(q):
        size = len(q)
        level += 1
        while size > 0 and len(q):
            temp = q.pop(0)
            if temp.left:
                q.append(temp.left)
                if not temp.left.left and not temp.left.right:
                    if result == sys.maxsize:
                        result = level
                    elif result != level:
                        return False
            if temp.right:
                q.append(temp.right)
                if not temp.right.left and not temp.right.right:
                    if result == sys.maxsize:
                        result = level
                    elif result != level:
                        return False
            size -= 1
    return True

if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.right = Node(4)
    root.right.left = Node(5)
    root.right.right = Node(6)

    result = leavesSameLevelOrNot(root)
    if result:
        print("All leaf nodes are at same level")
    else:
        print("Leaf nodes not at same level")