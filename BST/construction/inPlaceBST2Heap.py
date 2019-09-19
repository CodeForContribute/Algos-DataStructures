class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class LLNode:
    def __init__(self, data):
        self.data = data
        self.next = None
############ Time Complexity:O(n) ##############################################################
############ Space Complexity:O(1) ###############################################################
def printLevelOrderTraversal(root):
    if not root:
        return
    q = list()
    q.append(root)
    while len(q):
        nodeCount = len(q)
        while nodeCount:
            temp = q.pop(0)
            print(temp.data,end=" ")
            if temp.left:
                q.append(temp.left)
            if temp.right:
                q.append(temp.right)
            nodeCount -= 1
        print("\n")

def BSTtoSortedLL(root, head):
    # Base Condition
    if not root:
        return
    BSTtoSortedLL(root.right, head)#First traversing right to make sorted LL
    root.right = head[0] # Making the existing right pointer pointing to new node
    if head[0]:# make lefft pointer to none to make a linked list
        head[0].left = None
    head[0] = root # Updating the head pointer each time
    BSTtoSortedLL(root.left, head) # Recur for the left subtree



def sortedLLtoMinHeap(root, head):
    if not head:
        return
    q = list()
    root[0] = head[0]
    head[0] = head[0].right
    q.append(root[0])
    while head[0]:
        parent = q.pop(0)
        leftChild = head[0]
        head[0] = head[0].right
        leftChild.right = None
        q.append(leftChild)
        parent.left = leftChild
        if head[0]:
            rightChild = head[0]
            head[0] = head[0].right
            rightChild.right = None
            q.append(rightChild)
            parent.right = rightChild
            

def BSTtoMinHeap(root):
    head = [None]
    BSTtoSortedLL(root, head)
    root = [None]
    sortedLLtoMinHeap(root, head)
    return root[0]


if __name__ == '__main__':
    """ Constructing below tree  
                8  
               / \  
              4   12  
             / \ / \  
             2 6 10 14  
    """
    root = Node(8)
    root.left = Node(4)
    root.right = Node(12)
    root.right.left = Node(10)
    root.right.right = Node(14)
    root.left.left = Node(2)
    root.left.right = Node(6)
    root = BSTtoMinHeap(root)
    printLevelOrderTraversal(root)