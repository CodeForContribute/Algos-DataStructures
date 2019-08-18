class Node:
    def __init__(self,data):
        self.data = data
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

    def pairwise_swap_nodes(self):
        temp = self.head
        if temp is None:
            return
        while temp is not None and temp.next is not None:
            temp.data, temp.next.data = temp.next.data,temp.data

            temp = temp.next.next


if __name__ == '__main__':
    llist = LinkedList()
    llist.push(5)
    llist.push(4)
    llist.push(3)
    llist.push(2)
    llist.push(1)
    print("Linked list before calling pairWiseSwap() ")
    llist.print_list()
    llist.pairwise_swap_nodes()
    print("\nLinked list after calling pairWiseSwap()")
    llist.print_list()

