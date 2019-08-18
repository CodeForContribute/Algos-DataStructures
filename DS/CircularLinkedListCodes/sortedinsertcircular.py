class Node:
    def __init__(self, new_data):
        self.data = new_data
        self.next = None


class CLinkedList:
    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        temp = self.head
        if self.head is not None:
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
        else:
            new_node.next = new_node
        self.head = new_node

    def print_list(self):
        temp = self.head
        if self.head is not None:
            while True:
                print(temp.data, end=" ")
                temp = temp.next
                if temp == self.head:
                    break

    def sorted_insert(self, new_node):
        current = self.head
        if current is None:
            new_node.next = new_node
            self.head = new_node
        elif current.data >= new_node.data:
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head
            self.head = new_node
        else:
            while current.next != self.head and current.next.data < new_node.data:
                current = current.next
            new_node.next = current.next
            current.next = new_node


if __name__ == '__main__':
    cl = CLinkedList()
    arr = [1, 3, 2, 4, 6, 5]
    length = len(arr)
    for i in range(length):
        temp = Node(arr[i])
        cl.sorted_insert(temp)
    cl.print_list()
