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
            print(temp.data)
            temp = temp.next

    def swap_nodes_without_swapping_data(self, key1, key2):
        if key2 == key1:
            return
        temp1 = self.head
        prev1 = None
        while temp1:
            if temp1.data == key1:
                break
            prev1 = temp1
            temp1 = temp1.next
        next1 = temp1.next

        temp2 = self.head
        prev2 = None
        while temp2 is not None:
            if temp2.data == key2:
                break
            prev2 = temp2
            temp2 = temp2.next
        next2 = temp2.next
        if temp2 is None and temp1 is None:
            return
        if prev1 is not None:
            prev1.next = temp2
        else:
            self.head = temp2
        if prev2 is not None:
            prev2.next = temp1

        else:
            self.head = temp1

        temp2.next = next1
        temp1.next = next2


if __name__ == '__main__':
    ll = LinkedList()
    ll.push(14)
    ll.push(20)
    ll.push(13)
    ll.push(12)
    ll.push(15)
    ll.push(10)
    ll.print_list()
    print("Swapping two nodes without swapping data")
    ll.swap_nodes_without_swapping_data(12, 20)
    ll.print_list()
