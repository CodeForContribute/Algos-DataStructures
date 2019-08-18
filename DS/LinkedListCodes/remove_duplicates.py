class Node:
    def __init__(self, new_data):
        self.data = new_data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, data):
        new_node = Node(new_data=data)
        new_node.next = self.head
        self.head = new_node

    def delete_node(self, key):
        temp = self.head
        if temp is not None:
            if temp.data == key:
                self.head = temp.next
                temp = None
                return

        while temp is not None:
            if temp.data == key:
                break
            prev = temp
            temp = temp.next
            if temp is None:
                return
            prev.next = temp.next
            temp = None

    def remove_duplicates(self):
        temp = self.head
        if temp is None:
            return
        while temp.next is not None:
            if temp.data == temp.next.data:
                new_next = temp.next.next
                temp.next = None
                temp.next = new_next
            else:
                temp = temp.next
        # return self.head

    def remove_duplicates_recursive(self, head):
        if head is None:
            return
        if head.next is not None:
            if head.data == head.next.data:
                temp = head.next
                head.next = head.next.next
                temp = None
                self.remove_duplicates_recursive(head)
            else:
                self.remove_duplicates_recursive(head.next)

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.data, end=" ")
            temp = temp.next


if __name__ == '__main__':
    ll = LinkedList()
    ll.push(20)
    ll.push(13)
    ll.push(13)
    ll.push(13)
    ll.push(11)
    ll.push(11)
    ll.push(11)
    print("Created Linked List: ")
    ll.print_list()
    print()
    print("Linked List after removing",
          "duplicate elements:")
    # ll.remove_duplicates()
    ll.remove_duplicates_recursive(ll.head)
    ll.print_list()
