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

    def check_whether_linked_list_is_even_odd(self):
        temp = self.head
        length = 0
        while temp:
            length += 1
            temp = temp.next
        if length % 2 == 0:
            print("Linked List is even")
        else:
            print("Linked List is odd")


if __name__ == '__main__':
    ll = LinkedList()
    ll.push(3)
    ll.push(4)
    ll.push(5)
    ll.push(6)
    ll.push(7)
    print("Created Linked List is:")
    ll.print_list()
    print("\n")
    ll.check_whether_linked_list_is_even_odd()