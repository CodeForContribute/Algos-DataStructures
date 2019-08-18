class Node:
    def __init__(self, new_data):
        self.data = new_data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.new_head_ll = None

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def append(self, head, new_data):
        new_node = Node(new_data)
        if head is None:
            new_node.next = head
            head = new_node
        last = head
        while last.next:
            last = last.next
        last.next = new_node
        # return head

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next

    def add_two_numbers_linked_list(self, head1, head2):
        temp = head1
        temp2 = head2
        number1 = 0
        number2 = 0
        while temp:
            number1 = number1 * 10 + temp.data
            temp = temp.next
        while temp2:
            number2 = number2 * 10 + temp2.data
            temp2 = temp2.next
        sum_numbers = number2 + number1
        while int(sum_numbers / 10) > 0:
            new_data = sum_numbers % 10
            new_node = Node(new_data)
            new_node.next = self.new_head_ll
            self.new_head_ll = new_node
            sum_numbers = int(sum_numbers / 10)
        # print(sum_numbers)
        new_node = Node(sum_numbers)
        new_node.next = self.new_head_ll
        self.new_head_ll = new_node
        temp = self.new_head_ll
        while temp:
            print(temp.data, end=" ")
            temp = temp.next

    def add_two_linked_lists(self, first_list, second_list):
        prev = None
        temp_node = None
        carry = 0
        while first_list is not None or second_list is not None:
            first_data = 0 if first_list is None else first_list.data
            second_data = 0 if second_list is None else second_list.data

            sum_numbers = carry + first_data + second_data

            carry = 1 if sum_numbers >= 10 else 0
            sum_numbers = sum_numbers if sum_numbers < 10 else sum_numbers % 10
            temp_node = Node(sum_numbers)

            if self.head is None:
                self.head = temp_node
            else:
                prev.next = temp_node
            prev = temp_node
            if first_list is not None:
                first_list = first_list.next
            if second_list is not None:
                second_list = second_list.next

        if carry > 0:
            temp_node.next = Node(carry)


if __name__ == '__main__':
    first = LinkedList()
    # second = LinkedList()

    # Create first list
    first.push(6)
    first.push(4)
    first.push(9)
    first.push(5)
    first.push(7)

    print("Created 1st Linked List is :")
    first.print_list()

    second = LinkedList()
    second.push(4)
    second.push(8)
    print("\n")
    print("Created 2nd Linked List is :")
    second.print_list()

    print("\n")
    print("New Linked List after adding 2 numbers")
    res = LinkedList()
    res.add_two_linked_lists(first.head, second.head)
    res.print_list()

