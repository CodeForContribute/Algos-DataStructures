class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Time Complexity : O(n)
# Auxiliary Space : O(1)
def printBSTInrange(root, low, high):
    if low > high:
        return
    if not root:
        return
    current = root
    while current:
        if not current.left:
            if low <= current.data <= high:
                print(current.data, end=" ")
            current = current.right
        else:
            pre = current.left
            while pre.right and pre.right != current:
                pre = pre.right
            if not pre.right:
                pre.right = current
                current = current.left
            else:
                pre.right = None
                if low <= current.data <= high:
                    print(current.data, end=" ")
                current = current.right


if __name__ == '__main__':
    # Constructed binary tree is
    #        4
    #      / \
    #     2      7
    #    / \ / \
    #   1  3 6 10
    root = Node(4)
    root.left = Node(2)
    root.right = Node(7)
    root.left.left = Node(1)
    root.left.right = Node(3)
    root.right.left = Node(6)
    root.right.right = Node(10)

    printBSTInrange(root, 4, 12)
