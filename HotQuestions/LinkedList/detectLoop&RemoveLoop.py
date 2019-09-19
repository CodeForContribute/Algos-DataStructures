class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def detectLoopremoveLoop(head):
    if not head:
        return
    slow_ptr = head
    fast_ptr = head
    while slow_ptr and fast_ptr and fast_ptr.next:
        slow_ptr = slow_ptr.next
        fast_ptr = fast_ptr.next.next
        if slow_ptr == fast_ptr:
            removeLoop(slow_ptr)
            return True
    return 0

def removeLoop(slow_ptr):
    ptr1 = slow_ptr
    ptr2 = slow_ptr
    k = 1
    while ptr1.next != ptr2:
        ptr1 = ptr1.next
        k += 1

    ptr1 = head
    ptr2 = head

    for i in range(k):
        ptr2 = ptr2.next

    while ptr2 != ptr1:
        ptr1 = ptr1.next
        ptr2 = ptr2.next

    while ptr2.next != ptr1:
        ptr2 = ptr2.next
    ptr2.next = None



if __name__ == '__main__':
    head = Node(1)
    head.next = Node(23)
    head.next.next = Node(2)
    head.next.next.next = Node(46)
    head.next.next.next.next = Node(3)
    head.next.next.next.next.next = Node(69)
    head.next.next.next.next.next.next = head.next.next
    detectLoopremoveLoop(head)
    temp2 = head
    while temp2:
        print(temp2.data, end=" ")
        temp2 = temp2.next
