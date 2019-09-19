class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def getIntersectionPoint(head1, head2):
    temp1 = head1
    n1 = 0
    n2 = 0
    while temp1 is not None:
        n1 += 1
        temp1 = temp1.next
    temp2 =head2
    while temp2:
        n2 += 1
        temp2 = temp2.next
    temp1 = head1
    temp2 = head2
    if n1 > n2:
        diff = n1-n2
        while diff and temp1:
            temp1= temp1.next
            diff -= 1
    elif n1 < n2:
        diff = n2- n1
        while diff and temp2:
            temp2 = temp2.next
            diff -= 1
    while temp1 and temp2:
        if temp1.data == temp2.data:
            print(temp2.data,end=" ")
            break
        temp1 = temp1.next
        temp2 = temp2.next

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
    head1 = Node(123)
    head1.next = Node(423)
    head1.next.next = Node(22)
    head1.next.next.next = Node(46)
    head1.next.next.next.next = Node(3)
    head1.next.next.next.next.next = Node(69)
    head1.next.next.next.next.next.next = Node(70)
    print("\n")
    printList(head1)
    print("\n")
    getIntersectionPoint(head, head1)



