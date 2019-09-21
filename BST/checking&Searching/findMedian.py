class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def inorder(root):
    if not root:
        return
    inorder(root.left)
    print(root.data, end=" ")
    inorder(root.right)


def insert(root, data):
    if not root:
        return Node(data)
    if root.data < data:
        root.right = insert(root.right, data)
    if root.data > data:
        root.left = insert(root.left, data)
    return root


######## Amazon & Google ######################
# Find median of BST in O(n) time and O(1) space
# Given a Binary Search Tree, find median of it.
#
# If no. of nodes are even: then median = ((n/2th node + (n+1)/2th node) /2
# If no. of nodes are odd : then median = (n+1)/2th node.
def CountNodes(root):
    if not root:
        return 0
    count = 0
    current = root
    while current:
        if not current.left:
            count += 1
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
                count += 1
                current = current.right
    return count


def findMedian(root):
    if not root:
        return 0
    count = CountNodes(root)
    currentCount = 0
    current = root
    while current:
        if not current.left:
            currentCount += 1
            if count % 2 != 0 and currentCount == (count + 1) // 2:
                return current.data
            elif count % 2 == 0 and currentCount == (count // 2) + 1:
                return (prev.data + current.data) // 2
            prev = current
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
                prev = pre
                currentCount += 1
                if count % 2 != 0 and currentCount == (count + 1) // 2:
                    return current.data
                elif count % 2 == 0 and currentCount == (count // 2) + 1:
                    return (prev.data + current.data) // 2
                prev = current
                current = current.right


if __name__ == '__main__':
    """ Constructed binary tree is 
        50 
        / \ 
    30 70 
    / \ / \ 
    20 40 60 80 """

    root = Node(50)
    insert(root, 30)
    insert(root, 20)
    insert(root, 40)
    insert(root, 70)
    insert(root, 60)
    insert(root, 80)
    print("Median of BST is ", findMedian(root))
