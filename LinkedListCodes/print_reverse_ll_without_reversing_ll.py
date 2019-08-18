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

    def print_reverse_linked_list(self, head):
        temp = head
        if temp is None:
            return
        self.print_reverse_linked_list(temp.next)
        print(temp.data, end=" ")


if __name__ == '__main__':
    ll = LinkedList()
    ll.push(90)
    ll.push(89)
    ll.push(78)
    ll.push(67)
    print("\n")
    print("Created Linked list is :")
    ll.print_list()
    print("\n")
    print("Linked List after reversing the given linked list")
    ll.print_reverse_linked_list(ll.head)


