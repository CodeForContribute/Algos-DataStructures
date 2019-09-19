class Node:
    def __init__(self, data):
        self.data = data
        self.next  = None



def reverseLinkedList(head):
    prev = None
    current = head
    while current is not None:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    head = prev
    return head


def printList(head):
    if not head:
        return
    temp = head
    while temp:
        print(temp.data,end=" ")
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
    head = reverseLinkedList(head)
    print("\n")
    printList(head)