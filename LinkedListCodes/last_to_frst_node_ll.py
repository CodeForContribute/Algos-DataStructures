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

    def move_last_first_node(self):
        temp = self.head
        if temp is None and temp.next is None:
            return
        while temp.next.next:
            temp = temp.next
        temp2 = temp.next
        temp.next = None
        temp2.next = self.head
        self.head = temp2


if __name__ == '__main__':
    llist = LinkedList()
    # swap the 2 nodes
    llist.push(5)
    llist.push(4)
    llist.push(3)
    llist.push(2)
    llist.push(1)
    print("Linked List before moving last to front\n ")
    llist.print_list()
    llist.move_last_first_node()
    print("Linked List after moving last to front ")
    llist.print_list()
