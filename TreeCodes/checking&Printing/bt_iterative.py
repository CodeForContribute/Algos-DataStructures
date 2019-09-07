class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def isBinaryTreeIterative(root):
    queue = list()
    queue.append(root)
    while len(queue):
        temp = queue.pop(0)
        if not temp.left and not temp.right:
            continue
        if not temp.left or not temp.right:
            return False

        if temp.left:
            queue.append(temp.left)
        if temp.right:
            queue.append(temp.right)

    return True


if __name__ == '__main__':
    root = Node(10)
    root.left = Node(20)
    root.right = Node(30)

    root.left.left = Node(40)
    # root.left.right = Node(50)
    root.right.left = Node(60)
    root.right.right = Node(70)

    if isBinaryTreeIterative(root):
        print("Yes")
    else:
        print("No")
