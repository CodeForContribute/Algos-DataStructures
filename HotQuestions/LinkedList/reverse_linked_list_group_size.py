class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def reverse(head,k):
    if not head:
        return
    prev = None
    next_node  = None
    current = head
    count = 0
    while current and count < k:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
        count += 1

    if next_node is not None:
        head.next = reverse(next_node, k)

    head = prev
    return head

def reverseLinkedListUsingStack(head, k):
    if not head:
        return
    if k < 0 :
        return
    if k ==0:
        return head
    Stack = list()
    temp = head
    prev = None
    while temp is not None:
        new_val = 0
        while temp and new_val < k:
            Stack.append(temp.data)
            temp = temp.next
            new_val += 1

        while Stack:
            if not prev:
                prev = Node(Stack.pop())
                head = prev
            else:
                prev.next = Node(Stack.pop())
                prev = prev.next
    prev.next = None
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
    head = reverse(head, 2)
    print("\n")
    printList(head)
    print("\n")
    head = reverseLinkedListUsingStack(head, k=2)
    printList(head)
