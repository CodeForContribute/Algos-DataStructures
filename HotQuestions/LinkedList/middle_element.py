class Node:
    def __init__(self, data):
        self.data = data
        self.next = None



def getMiddleElement(head):
    if not head:
        return
    slow_ptr = head
    fast_ptr = head
    if head:
        while fast_ptr is not None and fast_ptr.next is not None:
            fast_ptr = fast_ptr.next.next
            slow_ptr = slow_ptr.next
        print(slow_ptr.data,end=" ")

def getMiddleUsingMidPointer(head):
    if not head:
        return
    mid = head
    count = 0
    while head:
        if count & 1:
            mid = mid.next
        count += 1
        head = head.next
    print(mid.data,end=" ")

def push(head,new_data):
    new_node = Node(new_data)
    new_node.next = head
    head.next = head


def printList(head):
    # temp = head
    while head is not None:
        print(head.data,end=" ")
        head = head.next


if __name__ == '__main__':
    head = Node(1)
    head.next = Node(23)
    head.next.next = Node(2)
    head.next.next.next = Node(46)
    head.next.next.next.next = Node(3)
    head.next.next.next.next.next = Node(69)
    head.next.next.next.next.next.next = Node(70)

    printList(head)
    print("\n")
    getMiddleElement(head)
    getMiddleUsingMidPointer(head)

