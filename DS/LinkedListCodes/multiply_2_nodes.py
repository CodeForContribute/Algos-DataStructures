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
        while temp is not None:
            print(temp.data, end=" ")
            temp = temp.next

    @staticmethod
    def multiply_nodes_of_two_linked_lists(head1, head2):
        temp1 = head1
        temp2 = head2
        number1 = temp1.data
        number2 = temp2.data
        temp1 = temp1.next
        temp2 = temp2.next
        while temp1 is not None:
            number1 = number1*10 + temp1.data
            temp1 = temp1.next
        print(number1)
        while temp2 is not None:
            number2 = number2 * 10 + temp2.data
            temp2 = temp2.next
        print(number2)
        return number2 * number1


if __name__ == '__main__':
    ll = LinkedList()
    ll.push(6)
    ll.push(4)
    ll.push(9)
    print("created 1st Linked list is:")
    ll.print_list()
    ll2 = LinkedList()
    ll2.push(4)
    ll2.push(8)
    print("Created 2nd Linked List is:")
    ll2.print_list()
    print("\n")
    print("Mul output of two Linked list is:")
    print(LinkedList.multiply_nodes_of_two_linked_lists(ll.head, ll2.head))

