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
            print(temp.data)
            temp = temp.next

    def get_nth_node_from_last_in_ll(self, index):
        temp = self.head
        length = 0
        while temp is not None:
            temp = temp.next
            length += 1

        if index > length:
            print("This index is not available in the given LL")
            return
        temp = self.head
        for i in range(0, length-index):
            temp = temp.next
        print(temp.data)

    def get_nth_from_last_ref_ptr(self, n):
        slw_ptr = self.head
        ref_ptr = self.head
        count = 0
        if self.head is not None:
            while count < n:
                if ref_ptr is None:
                    return
                ref_ptr = ref_ptr.next
                count += 1

        while ref_ptr is not None:
            slw_ptr = slw_ptr.next
            ref_ptr = ref_ptr.next

        print(slw_ptr.data)


if __name__ == '__main__':
    ll = LinkedList()
    ll.push(90)
    ll.push(23)
    ll.push(34)
    ll.push(45)
    ll.push(56)
    print("Created Linked list is:\n")
    ll.print_list()
    index = 5
    print("{} node in the given LL is:".format(index))
    ll.get_nth_node_from_last_in_ll(index)
    print("{} node in the given LL is:".format(index))
    ll.get_nth_from_last_ref_ptr(index)
