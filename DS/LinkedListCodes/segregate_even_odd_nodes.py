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

    def append(self, head, new_data):
        new_node = Node(new_data)
        last = head
        while last.next:
            last = last.next
        last.next = new_node

    # 1.Get pointer to the last node
    # 2.Move all the odd nodes to the end:
    # a.Consider all the odd nodes before the first even node and move them to end
    # b.Change the head pointer to the first even node
    # c. Consider all odd nodes after the first even node and move them to the end
    # def segregate_even_odd_nodes_ll(self):
    #     end = self.head
    #     prev = None
    #     current = self.head
    #     while end is not None:
    #         end = end.next
    #     new_end = end
    #     while current.data % 2 != 0 and current != end:
    #         new_end.next = current
    #         current = current.next
    #         new_end.next.next = None
    #         new_end = new_end.next
    #         if current.data % 2 == 0:
    #             self.head = current
    #             while current.data != end:
    #                 if current.data % 2 == 0:
    #                     prev = current
    #                     current = current.next
    #                 else:
    #                     prev.next = current.next
    #                     current.next = None
    #                     new_end.next = current
    #                     new_end = current
    #                     current = prev.next
    #
    #         else:
    #             prev = current
    #         if new_end != end and end.data %2 != 0:
    #             prev.next = end.next
    #             end.next = None
    #             new_end.next = end

    def segregate_odd_even_nodes(self):
        even_start = None
        odd_start = None
        even_end = None
        odd_end = None
        current = self.head
        while current is not None:
            data = current.data
            if data % 2 == 0:
                if even_start is None:
                    even_start = current
                    even_end = even_start
                else:
                    even_end.next = current
                    even_end = even_end.next

            else:
                if odd_start is None:
                    odd_start = current
                    odd_end = odd_start
                else:
                    odd_end.next = current
                    odd_end = odd_end.next
            current = current.next

        if odd_start is None or even_start is None:
            return
        even_end.next = odd_start
        odd_end.next = None
        self.head = even_start


if __name__ == '__main__':
    ll = LinkedList()
    ll.push(8)
    ll.push(5)
    ll.push(3)
    ll.push(4)
    ll.push(1)
    ll.print_list()
    ll.segregate_odd_even_nodes()
    print("\n")
    print("segregated Linked List is:")
    ll.print_list()
