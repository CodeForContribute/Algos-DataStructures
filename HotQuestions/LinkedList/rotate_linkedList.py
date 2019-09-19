
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def rotateLinkedList(head, k):
    if not head:
        return
    if k < 0:
        print("k can not be negative!")
        return
    if k == 0:
        return head
    last = head
    while last.next is not None:
        last = last.next
    while k > 0:
        temp = head.next
        head.next = None
        last.next = head
        last = last.next
        head = temp
        k -= 1
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
    head = rotateLinkedList(head, 3)
    print("\n")
    printList(head)

