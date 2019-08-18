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
        if temp is None:
            return
        while temp:
            print(temp.data, end=" ")
            temp = temp.next

    def delete_linked_list(self):
        temp = self.head
        if temp is None:
            return
        while temp is not None:
            prev_node = temp.next
            del temp.data
            temp = prev_node
        if temp is None:
            self.head = None
            return self.head

    def remove_every_kth_node(self, k):
        if k <= 0:
            print("kth node can not be negative or 0")
            return
        if self.head is None:
            return
        if k == 1:
            self.delete_linked_list()
            return
        prev = None
        temp = self.head
        count = 0
        while temp is not None:
            count += 1
            if count == k:
                prev.next = temp.next
                temp = None
                temp = prev.next
                count = 0
            else:
                prev = temp
                temp = temp.next


if __name__ == '__main__':
    ll = LinkedList()
    ll.push(2)
    ll.push(3)
    ll.push(4)
    ll.push(5)
    ll.push(6)
    ll.push(3)
    ll.push(7)
    ll.push(8)
    ll.push(9)
    ll.push(11)
    ll.push(13)
    print("Created Linked List is:")
    ll.print_list()
    print("\n")
    print("Linked list after deleting every kth node is:")
    ll.remove_every_kth_node(1)
    ll.print_list()




