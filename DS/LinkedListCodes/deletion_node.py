class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def append(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def insert_after(self, prev_node, new_data):
        new_node = Node(new_data)
        if prev_node is None:
            print("The given previous node is Null so returning")
            return
        new_node.next = prev_node.next
        prev_node.next = new_node


    def delete_node(self, key):
        current = self.head
        if current is not None:
            if current.data == key:
                self.head = current.next
                current = None
                return
        while current is not None:
            if current.data == key:
                break
            prev = current
            current = current.next
        if current is None:
            return
        prev.next = current.next
        current = None

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next


if __name__ == '__main__':
    ll = LinkedList()
    ll.push(34)
    ll.push(90)
    ll.push(89)
    ll.push(78)
    ll.push(67)
    ll.append(90)
    ll.delete_node(90)
    # ll.head = 9
    ll.print_list()

