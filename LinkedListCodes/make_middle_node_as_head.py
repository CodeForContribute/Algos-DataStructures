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

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next

    def middle_to_head_linked_list(self):
        slow_ptr = self.head
        fast_ptr = self.head
        while slow_ptr and fast_ptr and fast_ptr.next is not None:
            prev = slow_ptr
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next
        mid = slow_ptr
        prev.next = slow_ptr.next
        mid.next = self.head
        self.head = mid


if __name__ == '__main__':
    ll = LinkedList()
    ll.push(90)
    ll.push(89)
    ll.push(78)
    ll.push(67)
    ll.push(45)
    print(" created Linked list is:")
    ll.print_list()
    print("\n")
    print("Linked list after making middle node as head")
    ll.middle_to_head_linked_list()
    ll.print_list()

