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
            print(temp.data, end= " ")
            temp = temp.next

    def reverse_linked_list(self):
        prev = None
        current = self.head
        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        # current.next = prev
        self.head = prev

    def reverse_linked_list_recursive(self, head):
        if head is None:
            return
        first = head
        rest = first.next
        if rest is None:
            return
        self.reverse_linked_list_recursive(rest)
        first.next.next = first
        first.next = None
        head = rest


if __name__ == '__main__':
        ll = LinkedList()
        ll.push(90)
        ll.push(89)
        ll.push(78)
        ll.push(67)
        ll.push(56)
        print("\n")
        print("Created Linked List is :")
        ll.print_list()
        # ll.reverse_linked_list()
        ll.reverse_linked_list_recursive(ll.head)
        print("\n")
        print("Reversed Linked List is:")
        ll.print_list()
