class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def insert(root, data):
    if not root:
        return TNode(data)
    if data < root.data:
        root.left = insert(root.left, data)
    if data > root.data:
        root.right = insert(root.right, data)
    return root


############################## Time complexity: O(n) where n is number of nodes in a tree
def InorderTraversal(root):
    if not root:
        return
    s = []
    inorder = []
    s.append(root)
    root = s.pop()
    while len(s) or root:
        while root:
            s.append(root)
            root = root.left
        root = s.pop()
        inorder.append(root.data)
        root = root.right
    return inorder


def kthSmallest(root, k):
    if not root:
        return
    inorder = InorderTraversal(root)
    return inorder[k - 1]


########################################## Augmented Tree DS  ####################################################
class TNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.lcount = 0
        self.rcount = 0


def insertNode(root, node):
    ptravverse = root
    current_parent = root
    while ptravverse:
        current_parent = ptravverse
        if node.data < ptravverse.data:
            ptravverse.lcount += 1
            ptravverse = ptravverse.left
        else:
            ptravverse = ptravverse.right
    if not root:
        root = node
    elif node.data < root.data:
        current_parent.left = node
    else:
        current_parent.right = node
    return root


##########################Time complexity: O(h) where h is height of tree#################################
def ksmallest_element(root, k):
    if not root:
        return None
    if k <= 0:
        return None
    ret = None
    if root:
        temp = root
        while temp:
            if temp.lcount + 1 == k:
                ret = temp.data
                break
            elif temp.lcount > k:
                k = k - temp.lcount + 1
                temp = temp.right
            else:
                temp = temp.left
    return ret


def insertNodeLargest(root, node):
    temp = root
    current = root
    while temp:
        current = temp
        if node.data < temp.data:
            temp = temp.left
        else:
            temp.rcount += 1
            temp = temp.right
    if not root:
        root = node
    elif node.data < root.data:
        current.left = node
    else:
        current.right = node
    return root


def kthLargestElement(root, k):
    if not root:
        return None
    if k <= 0:
        return None
    ret = None
    if root:
        temp = root
        while temp:
            if temp.rcount + 1 == k:
                ret = temp.data
                break
            elif k > temp.rcount + 1:
                k = k - temp.rcount + 1
                temp = temp.left
            else:
                temp = temp.right
    return ret


def kthSmallestUsingMorris(root, k):
    count = 0
    import sys
    ksmall = -sys.maxsize
    current = root
    while current:
        if not current.left:
            count += 1
            if count == k:
                ksmall = current.data
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
                if count == k:
                    ksmall = current.data
                current = current.right
    return ksmall


#############################################################################################################


if __name__ == '__main__':
    r = Node(50)
    insert(r, 30)
    insert(r, 20)
    insert(r, 40)
    insert(r, 70)
    insert(r, 60)
    insert(r, 80)

    # Print inoder traversal of the BST
    print(kthSmallest(r, 4))
    print(kthSmallestUsingMorris(r, 4))

    root = TNode(50)
    insertNode(root, TNode(30))
    insertNode(root, TNode(20))
    insertNode(root, TNode(40))
    insertNode(root, TNode(70))
    insertNode(root, TNode(60))
    insertNode(root, TNode(80))

    # Print inoder traversal of the BST
    print(ksmallest_element(root, 4))

    root = TNode(50)
    insertNodeLargest(root, TNode(30))
    insertNodeLargest(root, TNode(20))
    insertNodeLargest(root, TNode(40))
    insertNodeLargest(root, TNode(70))
    insertNodeLargest(root, TNode(60))
    insertNodeLargest(root, TNode(80))

    # Print inoder traversal of the BST
    print(kthLargestElement(root, 4))
