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

    def delete_alternate_nodes(self, head):
        if head is None:
            return
        prev = head
        node = head.next
        while prev is not None and node is not None:
            prev.next = node.next
            node = None
            prev = prev.next
            if prev is not None:
                node = prev.next

    def delete_alternate_nodes_recursive(self, head):
        if head is None:
            return
        node = head.next
        if node is None:
            return
        head.next = node.next
        node = None
        self.delete_alternate_nodes_recursive(head.next)


if __name__ == '__main__':
    ll = LinkedList()
    ll.push(90)
    ll.push(89)
    ll.push(78)
    ll.push(67)
    ll.push(56)
    ll.push(45)
    ll.push(34)
    print("\n")
    print("Created Linked List is :")
    ll.print_list()
    ll.delete_alternate_nodes_recursive(ll.head)
    print("\n")
    print("Linked List after deleting alternate nodes:")
    ll.print_list()
