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
    def is_sum_sorted(head1, head2, head3, given_sum):
        a = head1
        while a is not None:
            b = head2
            c = head3
            while b is not None and c is not None:
                sum_triplet = a.data + b.data + c.data
                if sum_triplet == given_sum:
                    print("Triplet Found:(%d,%d,%d)" % (a.data, b.data, c.data))
                    return True
                elif sum_triplet < given_sum:
                    b = b.next
                else:
                    c = c.next
            a = a.next

        print("No such Triplet Found:")
        return False


if __name__ == '__main__':
    l1 = LinkedList()
    l2 = LinkedList()
    l3 = LinkedList()
    print("First Linked List created is:")
    l1.push(20)
    l1.push(4)
    l1.push(15)
    l1.push(10)
    l1.print_list()
    print("\n")
    print("Second Linked List Created Is:")
    l2.push(10)
    l2.push(9)
    l2.push(4)
    l2.push(2)
    l2.print_list()
    print("\n")
    print("Third Linked List Created Is:")
    l3.push(1)
    l3.push(2)
    l3.push(4)
    l3.push(8)
    l3.print_list()
    print("\n")
    given_sum = 10
    linked_list_new = LinkedList()
    linked_list_new.is_sum_sorted(l1.head, l2.head, l3.head, given_sum)






