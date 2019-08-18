class Node:
    def __init__(self, new_data):
        self.data = new_data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def get_middle_node_in_ll(self):
        count = 0
        temp = self.head
        while temp is not None:
            count += 1
            temp = temp.next

        temp = self.head
        for i in range(0, int(count/2)):
            temp = temp.next
        print(temp.data)

    def get_middle_node_using_slow_fast_ptr(self):
        slow_ptr = self.head
        fast_ptr = self.head
        while fast_ptr is not None and fast_ptr.next is not None:
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next
        print(slow_ptr.data)

    def get_middle_node(self):
        count = 0
        mid = self.head
        while self.head is not None:
            if count & 1:
                mid = mid.next
            count += 1
            self.head = self.head.next
        print(mid.data)

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.data)
            temp = temp.next


if __name__ == '__main__':
    ll = LinkedList()
    ll.push(90)
    ll.push(23)
    ll.push(34)
    ll.push(45)
    ll.push(56)
    # ll.push(67)
    print("created Linked list is :\n")
    ll.print_list()
    print("Middle element of linked List is:")
    ll.get_middle_node_in_ll()
    ll.get_middle_node_using_slow_fast_ptr()
    ll.get_middle_node()