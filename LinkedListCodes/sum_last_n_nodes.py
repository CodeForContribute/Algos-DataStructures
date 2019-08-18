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

    # Method1 : using system call stack
    def sum_last_n_nodes_util(self, head, n, sums):
        if head is None:
            return
        self.sum_last_n_nodes_util(head.next, n, sums)
        if n > 0:
            sums += head.data
            n = n-1
        return sums

    # Method1 : using system call stack
    def sum_last_n_nodes(self, head, n):
        if n <= 0:
            return 0
        sums = 0
        self.sum_last_n_nodes_util(head.next, n, sums)
        if n > 0:
            sums += head.data
            n = n - 1
        return sums

    # Method2: Using user defined stack
    def sum_last_n_nodes_using_stack(self, n):
        if self.head is None:
            return
        if n <= 0:
            return 0
        s = list()
        temp = self.head
        while temp:
            s.append(temp.data)
            temp = temp.next
        sum_last_n_nodes = 0
        while n > 0:
            try:
                sum_last_n_nodes += s.pop()
                n = n - 1
            except IndexError as ex:
                print("please enter valid number of nodes")
                sum_last_n_nodes = None
                break
        return sum_last_n_nodes

    # Method3 : Using reversing the Linked List
    def reverse_linked_list(self):
        prev = None
        current = self.head
        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    # Method3 : Using reversing the Linked List
    def sum_n_nodes_in_reversed_list(self, n):
        self.reverse_linked_list()
        if self.head is None:
            return
        if n <= 0:
            return 0
        sum_n_nodes = 0
        temp = self.head
        while n > 0 and temp is not None:
            sum_n_nodes += temp.data
            n = n - 1
            temp = temp.next
        self.reverse_linked_list()
        return sum_n_nodes

    # Method4: Using the length of Linked List
    def sum_n_nodes_ll_using_length_list(self, n):
        temp = self.head
        length = 0
        while temp:
            length += 1
            temp = temp.next
        if n > length:
            print("No of nodes provided is greater than the length of linked List")
            return
        temp = self.head
        for i in range(0, length-n):
            temp = temp.next
        sums = 0
        while temp is not None:
            sums += temp.data
            temp = temp.next
        return sums

    # Method 5 :using slow_ptr and fast_ptr
    def sum_n_nodes_using_slow_fast_ptr(self, n):
        if n <= 0:
            return 0
        if self.head is None:
            return
        slow_ptr = self.head
        fast_ptr = self.head
        while fast_ptr is not None and n > 0:
            fast_ptr = fast_ptr.next
            n = n - 1
        sums = 0
        while slow_ptr is not None and fast_ptr is not None:
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next
        while slow_ptr is not None:
            sums += slow_ptr.data
            slow_ptr = slow_ptr.next
        return sums


if __name__ == '__main__':
    ll = LinkedList()
    ll.push(34)
    ll.push(2)
    ll.push(3)
    ll.push(4)
    ll.push(5)
    print("Created Linked Lis is:")
    ll.print_list()
    print("\n")
    no_nodes = 5
    print("Sum of last {} nodes using user system call stack:".format(no_nodes))
    print(ll.sum_last_n_nodes(ll.head, no_nodes))
    print("Sum of last {} nodes using user defined stack:".format(no_nodes))
    print(ll.sum_last_n_nodes_using_stack(no_nodes))
    print("Sum of last {} nodes using reversing the linked list:".format(no_nodes))
    print(ll.sum_n_nodes_in_reversed_list(no_nodes))
    print("Sum of last {} nodes using length of linked list:".format(no_nodes))
    print(ll.sum_n_nodes_ll_using_length_list(no_nodes))
    print("Sum of last {} nodes using slow_ptr and fast_ptr in  linked list:".format(no_nodes))
    print(ll.sum_n_nodes_using_slow_fast_ptr(no_nodes))

