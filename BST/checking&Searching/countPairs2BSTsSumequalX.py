class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def insert(root, data):
    if not root:
        return Node(data)
    if root.data > data:
        root.left = insert(root.left, data)
    if root.data < data:
        root.right = insert(root.right, data)
    return root


# Time Complexity: O(n1 + n2)
# Auxiliary Space: O(n1 + n2)

def countPairs(root1, root2, x):
    if not root1 or not root2:
        return 0
    count = 0
    stack1 = []
    stack2 = []
    while True:
        while root1:
            stack1.append(root1)
            root1 = root1.left
        while root2:
            stack2.append(root2)
            root2 = root2.right
        if not len(stack1) or not len(stack2):
            break
        top1 = stack1[-1]
        top2 = stack2[-1]
        if top1.data + top2.data == x:
            count += 1
            stack1.pop()
            stack2.pop()
            root1 = top1.right
            root2 = top2.left
        elif top1.data + top2.data < x:
            stack1.pop()
            root1 = top1.right
        else:
            stack2.pop()
            root2 = top2.left
    return count


if __name__ == '__main__':
    root1 = Node(5)
    root1.left = Node(3)
    root1.right = Node(7)
    root1.left.left = Node(2)
    root1.left.right = Node(4)
    root1.right.left = Node(6)
    root1.right.right = Node(8)

    root2 = Node(10)
    root2.left = Node(6)
    root2.right = Node(15)
    root2.left.left = Node(3)
    root2.left.right = Node(8)
    root2.right.left = Node(11)
    root2.right.right = Node(18)

    x = 16
    print(countPairs(root1, root2, x))
