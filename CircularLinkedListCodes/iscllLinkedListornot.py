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
            while temp is not None:
                while True:
                    print(temp.data, end=" ")
                    temp = temp.next
                    if temp == self.head:
                        break

    def isClinkedlist(self):
        temp = self.head
        if self.head is None:
            return True
        temp = self.head.next
        while temp is not None and temp != self.head:
            temp = temp.next
        if temp == self.head:
            return temp == self.head
        elif temp is None:
            return False


if __name__ == '__main__':
    llist = CLinkedList()
    llist.head = Node(1)
    second = Node(2)
    third = Node(3)
    fourth = Node(4)

    llist.head.next = second
    second.next = third
    third.next = fourth

    if llist.isClinkedlist():
        print('Yes')
    else:
        print('No')

    fourth.next = llist.head

    if llist.isClinkedlist():
        print('Yes')
    else:
        print('No')
