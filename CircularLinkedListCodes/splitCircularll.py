class Node:
    def __init__(self, new_data):
        self.data = new_data
        self.next = None


class CLinkedList:
    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        temp = self.head
        if self.head is not None:
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
        else:
            new_node.next = new_node
        self.head = new_node

    def print_list(self):
        temp = self.head
        if self.head is not None:
            while True:
                print(temp.data, end=" ")
                temp = temp.next
                if temp == self.head:
                    break

    def split_circular_linked_list(self, head1, head2):
        slow_ptr = self.head
        fast_ptr = self.head
        if self.head is None:
            return
        while fast_ptr.next != self.head and fast_ptr.next.next != self.head:
            fast_ptr = fast_ptr.next.next
            slow_ptr = slow_ptr.next
        if fast_ptr.next.next == self.head:
            fast_ptr = fast_ptr.next
        head1.head = self.head
        if self.head.next != self.head:
            head2.head = slow_ptr.next
        fast_ptr.next = slow_ptr.next
        slow_ptr.next = self.head


if __name__ == '__main__':
    cl = CLinkedList()
    head1 = CLinkedList()
    head2 = CLinkedList()
    cl.push(12)
    cl.push(56)
    cl.push(2)
    cl.push(11)
    cl.push(23)
    cl.push(34)
    print("Original Linked List is:")
    cl.print_list()
    cl.split_circular_linked_list(head1, head2)
    print("\n")
    print("First half of original Circular Linked List:")
    head1.print_list()
    print("\n")
    print("second half of original Circular Linked List:")
    head2.print_list()

