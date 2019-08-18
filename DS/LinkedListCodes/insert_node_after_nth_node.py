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

    # Method 1:Brute force technique
    def insert_node_after_nth_node(self, nth_node, data):
        if self.head is None:
            return
        new_node = Node(data)
        length = 0
        temp = self.head
        while temp:
            length += 1
            temp = temp.next
        temp = self.head
        for i in range(length-nth_node):
            temp = temp.next
        next_node = temp.next
        temp.next = new_node
        new_node.next = next_node
        
    # Method2 : using slow and fast pointer
    def insert_node_after_nth_node_using_ptr(self, nth_node, data):
        if self.head is None:
            return
        new_node = Node(data)
        slow_ptr = self.head
        fast_ptr = self.head
        for i in range(nth_node-1):
            fast_ptr = fast_ptr.next
        while fast_ptr.next is not None:
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next
        new_node.next = slow_ptr.next
        slow_ptr.next = new_node


if __name__ == '__main__':
    ll = LinkedList()
    ll.push(5)
    ll.push(4)
    ll.push(3)
    ll.push(1)
    print("Created Linked List is:")
    ll.print_list()
    # ll.insert_node_after_nth_node(4, 2)
    ll.insert_node_after_nth_node_using_ptr(4,2)
    print("\n")
    print("Linked list after inserting 2:")
    ll.print_list()

