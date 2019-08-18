class Node:
    def __init__(self, new_data):
        self.data = new_data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next= self.head
        self.head = new_node

    def append(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
        last = self.head
        while last is not  None:
            last = last.next
        last.next = new_node

    @staticmethod
    def insert_after_another_node(prev_node, new_data):
        if prev_node is None:
            return
        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_linked_list(self):
        temp = self.head
        if temp is None:
            return
        while temp is not None:
            prev_node = temp.next
            temp = None
            temp = prev_node

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.data, end=" ")
            temp = temp.next


if __name__ == '__main__':
    ll = LinkedList()
    ll.push(90)
    ll.push(34)
    ll.push(4)
    ll.push(3)
    ll.push(340)
    ll.print_list()
    ll.delete_linked_list()
    print("\n")
    # print(ll.head)
    # ll.print_list()
