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

    # Method1: Using pcrawl and pkey pointers
    def move_all_occurrences_of_element_to_end(self, key):
        pcrawl = self.head
        pkey = self.head
        while pcrawl is not None:
            if pcrawl != pkey and pcrawl.data != key:
                pkey.data = pcrawl.data
                pcrawl.data = key
                pkey = pkey.next

            if pkey.data != key:
                pkey = pkey.next
            pcrawl = pcrawl.next

    # Method2:
    def move_all_occurrences_element_to_end(self, head, key):
        last = head
        if head is None:
            return
        while last.next is not None:
            last = last.next
        last_node = last
        prev = None
        prev2 = None
        current = self.head
        while current != last_node:
            if current.data == key and prev2 is None:
                prev = current
                current = current.next
                head = current
                last_node.next = prev2
                last_node = last_node.next
                last_node.next = None
                prev = None
            else:
                if current.data == key and prev2 is not None:
                    prev = current
                    current = current.next
                    prev2.next = current
                    last_node.next = prev
                    last_node = last_node.next
                    last_node.next = None
                elif current != last:
                    prev2 = current
                    current = current.next
        return head


if __name__ == '__main__':
    ll = LinkedList()
    ll.push(3)
    ll.push(4)
    ll.push(2)
    ll.push(2)
    ll.push(1)
    print("Created 1st Linked list is:")
    ll.print_list()
    print("\n")
    print("Linked List after moving all the occurrences to end using pcrawl and pkey pointers:")
    ll.move_all_occurrences_of_element_to_end(2)
    ll.print_list()
    print("\n")
    print("Linked List after moving all the occurrences to end:")
    ll.move_all_occurrences_element_to_end(ll.head, 2)
    ll.print_list()
