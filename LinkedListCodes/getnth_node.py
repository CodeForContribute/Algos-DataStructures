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

    # Iterative way
    def get_nth__node_iterative(self, index):
        # count = 0
        temp = self.head
        while temp is not None and index > 0:
            index = index-1
            temp = temp.next
        if temp is None:
            print("The given Index is not available in the LL\n")
            return
        if temp is not None and index == 0:
            return temp.data

    # Recursive way
    def get_nth_node_recursive(self, li, index):
        count = 0
        if not li:
            print("The given node is not available in LL")
            return
        if index < 0:
            print("The index can not be negative")
            return
        if li:
            if count == index:
                print(li.data)
            else:
                self.get_nth_node_recursive(li.next, index-1)

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.data, end=" ")
            temp = temp.next


if __name__ == '__main__':
    ll = LinkedList()
    ll.push(90)
    ll.push(0)
    ll.push(9)
    ll.push(78)
    ll.push(45)
    ll.push(34)
    print("Created Linked List is:")
    ll.print_list()
    print("\n")
    print("Nth node in the Linked list is:")
    ll.get_nth_node_recursive(ll.head, 5)

