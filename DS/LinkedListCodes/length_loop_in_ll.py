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

    def find_loop(self):
        slow_ptr = self.head
        fast_ptr = self.head
        while slow_ptr and fast_ptr and fast_ptr.next:
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next
            if slow_ptr == fast_ptr:
                return True, slow_ptr,fast_ptr

    def length_loop(self):
        found, slow_ptr, fast_ptr = self.find_loop()
        count = 1
        if found:
            slow_ptr = slow_ptr.next
            while slow_ptr != fast_ptr:
                slow_ptr = slow_ptr.next
                count += 1

            return count
        else:
            print("Loop not found in the Linked List")

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next


if __name__ == '__main__':
    ll = LinkedList()
    ll.push(90)
    ll.push(89)
    ll.push(78)
    ll.push(34)
    ll.head.next.next.next.next = ll.head
    print("\n")
    # ll.print_list()
    print(ll.length_loop())
