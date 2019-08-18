class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def push(self,new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def append(self,data):
        new_node = Node(data)
        last = self.head
        if self.head is None:
            self.head = new_node

        while last and last.next is not None:
            last = last.next
        last.next = new_node

    @staticmethod
    def insert_after(prev_node, new_data):
        if prev_node is None:
            print("The given previous node does not exist")
            return
        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def print_list(self):
        node = self.head
        while node:
            print(node.data, end="\n")
            node = node.next


if __name__ == '__main__':
    ll = LinkedList()
    ll.push(90)
    ll.append(8)
    ll.push(80)
    ll.append(7)
    ll.print_list()
