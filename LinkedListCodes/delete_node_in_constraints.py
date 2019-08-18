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

    def delete_a_node_in_constraint(self, head, node_to_be_deleted):
        if head is None:
            return
        if head.data == node_to_be_deleted:
            if head.next is None:
                print("There is only one node so list can't be made empty")
                return
            head.data = head.next.data
            n = head.data
            head.next = head.next.next
            n = None
            return
        temp = head
        while temp:
            if temp.data == node_to_be_deleted:
                next_node = temp.next
                prev.next = next_node
                temp = None
                temp = next_node
            else:
                prev = temp
                temp = temp.next


if __name__ == '__main__':
    ll = LinkedList()
    ll.push(9)
    ll.push(3)
    ll.push(4)
    ll.push(5)
    ll.print_list()
    print("\n")
    print("Linked list after deleting a node is :")
    ll.delete_a_node_in_constraint(ll.head, 4)
    ll.print_list()


