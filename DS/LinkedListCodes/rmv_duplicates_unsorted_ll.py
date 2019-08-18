class Node:
    def __init__(self, new_data):
        self.data = new_data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

    @staticmethod
    def remove_duplicates_unsorted_ll(head):
        ptr1 = head
        while ptr1 is not None and ptr1.next is not None:
            ptr2 = ptr1
            while ptr2 is not None and ptr2.next is not None:
                if ptr1.data == ptr2.next.data:
                    dup = ptr2.next
                    ptr2.next = ptr2.next.next
                    dup = None
                else:
                    ptr2 = ptr2.next
            ptr1 = ptr1.next

    @staticmethod
    def remove_duplicates_ll_unsorted(head):
        temp = head
        prev = None
        s = set()
        while temp is not None:
            if temp.data in s:
                prev.next = temp.next
            else:
                s.add(temp.data)
                prev = temp
            temp = prev.next


if __name__ == '__main__':
    ll = LinkedList()
    ll.push(20)
    ll.push(17)
    ll.push(12)
    ll.push(13)
    ll.push(11)
    ll.push(12)
    ll.push(11)
    print("Created Linked List: ")
    ll.print_list()
    print()
    print("Linked List after removing",
          "duplicate elements:")
    # ll.remove_duplicates_unsorted_ll(ll.head)
    ll.remove_duplicates_ll_unsorted(ll.head)
    ll.print_list()

