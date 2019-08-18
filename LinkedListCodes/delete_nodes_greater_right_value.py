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

    # Algorithms:
    # 1. First reverse the given list
    # 2. keep track of max node till then:
    #                if max node is greater than next node delete the next node
    #                  else max node will be next node
    # 3.Reverse the given list back
    def reverse_linked_list(self):
        prev = None
        current = self.head
        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def delete_nodes_greater_right_value(self, head):
        max_node = head
        current = head
        while current is not None and current.next is not None:
            if current.next.data >= current.data:
                current = current.next
                max_node = current
            else:
                temp = current.next
                current.next = temp.next
                temp = None


if __name__ == '__main__':
    ll = LinkedList()
    ll.push(3)
    ll.push(2)
    ll.push(6)
    ll.push(5)
    ll.push(11)
    ll.push(10)
    ll.push(15)
    ll.push(12)
    print("Created Linked List is:")
    ll.print_list()
    print("\n")
    print("Linked List after deleting grater right value")
    ll.reverse_linked_list()
    ll.delete_nodes_greater_right_value(ll.head)
    ll.reverse_linked_list()
    ll.print_list()
