class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def mergeSortedLists(head1,head2):
    if not head1:
        return head2
    if not head2:
        return head1
    if head1.data < head2.data:
        head1.next = mergeSortedLists(head1.next, head2)
    else:
        head2.next = mergeSortedLists(head1, head2.next)


def mergeSortedListsIterative(head1, head2):
    if not head1:
        return head2
    if not head2:
        return head1
    if head1.data < head2.data:
        return MergeUtil(head1, head2)
    else:
        return MergeUtil(head2, head1)


def MergeUtil(head1, head2):
    if not head1.next:
        head1.next = head2
        return head1
    current1 = head1
    current2 = head2
    next1 = head1.next
    next2 = head2.next
    while next1 and current2:
        if  current1.data <= current2.data <= next1.data:
            next2 = current2.next
            current1.next = current2
            current2.next = next1
            current1 = current2
            current2 = next2
        else:
            if next1.next:
                next1 = next1.next
                current1 = current1.next
            else:
                next1.next = current2
                return head1
