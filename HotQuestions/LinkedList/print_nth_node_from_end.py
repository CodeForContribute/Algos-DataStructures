class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def printNthNode(head, n):
    slow_ptr = head
    fast_ptr = head
    count = 0
    if not head:
        return
    while count < n:
        if not fast_ptr:
            return
        fast_ptr = fast_ptr.next
        count += 1
    while fast_ptr:
        slow_ptr = slow_ptr.next
        fast_ptr = fast_ptr.next
    print(slow_ptr.data, end=" ")

    ###################### Below code is to delete the nth node from the end##########################################
    # while fast_ptr.next:
    #     slow_ptr = slow_ptr.next
    #     fast_ptr = fast_ptr.next
    # print(slow_ptr.data,end=" ")
    # temp = slow_ptr.next
    # slow_ptr.next = slow_ptr.next.next
    # temp = None


def printList(head):
    if not head:
        return
    temp = head
    while temp:
        print(temp.data, end=" ")
        temp = temp.next


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
    printNthNode(head, 4)
    print("\n")
    printList(head)
