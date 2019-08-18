class Node:
    def __init__(self, new_data):
        self.data = new_data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def append_node(self, head, new_data):
        new_node = Node(new_data)
        if head is None:
            head.next = new_node
        last = head
        while last.next:
            last = last.next
        last.next = new_node

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next

    def sorted_intersect_2ll(self, head1, head2):
        if head1 is None or head2 is None:
            return None
        if head1.data < head2.data:
            return self.sorted_intersect_2ll(head1.next, head2)
        if head1.data > head2.data:
            return self.sorted_intersect_2ll(head1, head2.next)


    def sorted_intersection_2ll(self, head1, head2):
        dummy = None
        if head2 is None or head1 is None:
            return
        while head1 is not None and head2 is not None:
            if head1.data == head2.data:
                new_node = Node(head1.data)
                new_node.next = dummy
                dummy = new_node
            elif head1.data < head2.data:
                head1 = head1.next
            elif head1.data > head2.data:
                head2 = head2.next
        temp = dummy
        while temp:
            print(temp.data, end=" ")
            temp = temp.next


if __name__ == '__main__':
    ll = LinkedList()
    ll.push(1)
    ll.push(2)
    ll.push(3)
    # ll.push(56)
    # ll.push(67)
    # ll.push(78)
    # ll.push(89)
    print("Created 1st Linked List is:")
    ll.print_list()

    ll2 = LinkedList()
    ll2.push(1)
    ll2.push(2)
    ll2.push(3)
    # ll2.push(6)
    # ll2.push(67)
    # ll2.push(78)
    # ll2.push(8)
    print("\n")
    print("Created 2nd Linked List is:")
    ll2.print_list()
    print("\n")
    print("Sorted Linked List from 2ll")
    ll.sorted_intersection_2ll(ll.head, ll2.head)
