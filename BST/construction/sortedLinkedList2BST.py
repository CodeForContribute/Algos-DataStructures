class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class LLNode:
    def __init__(self, data):
        self.data = data
        self.next = None


def pushLL(head, data):
    # if not head:
    #     return LLNode(data)
    new_node = LLNode(data)
    new_node.next = head
    head.next = new_node


def getMiddle(head):
    if not head:
        return
    slow_ptr = head
    fast_ptr = head
    while slow_ptr and fast_ptr and fast_ptr.next:
        slow_ptr = slow_ptr.next
        fast_ptr = fast_ptr.next.next
    return slow_ptr


def sortedLL2BST(head):
    if not head:
        return
    temp = getMiddle(head)
    temp2 = temp.next
    temp.next = None
    root = Node(temp.data)
    root.left = sortedLL2BST(head)
    root.right = sortedLL2BST(temp2)
    return root

def printList(head):
    # if not head:
    #     return
    current = head
    while current:
        print(current.data,end=" ")
        current = current.next

def preOrder(root):
    if not root:
        return
    print(root.data,end=" ")
    preOrder(root.left)
    preOrder(root.right)

if __name__ == '__main__':
    head = LLNode(1)
    head.next = LLNode(2)
    head.next.next = LLNode(3)
    head.next.next.next = LLNode(4)
    head.next.next.next.next = LLNode(5)
    head.next.next.next.next.next = LLNode(6)
    head.next.next.next.next.next.next = LLNode(7)
    print ("Given Linked List ")
    printList(head)
    root = sortedLL2BST(head)
    print( "\nPreOrder Traversal of constructed BST ")
    preOrder(root)
