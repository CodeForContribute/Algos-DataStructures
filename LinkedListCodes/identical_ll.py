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

    @staticmethod
    def identical_linked_lists(head1, head2):
        a = head1
        b = head2
        while a is not None and b is not None:
            if a.data != b.data:
                return False
            a = a.next
            b = b.next
        if a is None and b is None:
            return True


if __name__ == '__main__':
    llist1 = LinkedList()
    llist2 = LinkedList()
    llist1.push(1)
    llist1.push(2)
    llist1.push(3)
    llist2.push(1)
    llist2.push(2)
    llist2.push(3)
    if llist1.identical_linked_lists(llist1.head, llist2.head) is True:
        print("Identical ")
    else:
        print("Not identical ")

