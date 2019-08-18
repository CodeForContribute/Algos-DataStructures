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

    def delete_at_given_position(self, position):
        temp = self.head
        if self.head is None:
            return
        if position == 0:
            self.head = temp.next
            temp = None
            return
        for i in range(position):
            prev = temp
            temp = temp.next
            if prev is None and temp is None:
                break

        if temp is None:
            return
        # if temp.next is None:
        #     return

        prev.next = temp.next
        temp = None

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next


if __name__ == '__main__':
    llist = LinkedList()
    llist.push(34)
    llist.push(2)
    llist.push(21)
    llist.push(24)

    # llist.delete_at_given_position(2)
    # llist.delete_at_given_position(1)
    llist.delete_at_given_position(3)
    print("created linked list is :")
    llist.print_list()


