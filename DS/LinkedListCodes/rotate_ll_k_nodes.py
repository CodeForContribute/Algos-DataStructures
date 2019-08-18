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
        while temp is not None:
            print(temp.data, end=" ")
            temp = temp.next

    def rotate_ll_k_nodes(self, k):
        if self.head is None:
            return
        if k == 0:
            return
        current = self.head
        count = 1
        while count < k and current is not None:
            current = current.next
            count += 1
        if current is None:
            return
        kth_node = current
        while current.next is not None:
            current = current.next
        current.next = self.head
        self.head = kth_node.next
        kth_node.next = None


if __name__ == '__main__':
    ll = LinkedList()
    for i in range(10, 60, 10):
        ll.push(i)
    print("Created Linked List:")
    ll.print_list()
    print("\n")
    k = 4
    print("Linked List after rotating the List by:", k)
    ll.rotate_ll_k_nodes(k)
    ll.print_list()
