class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def push(self,new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def append(self, new_node):
        # new_node = Node(data=new_data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next


class MergeSortedLinkedList:

    def __init__(self):
        self.merged_linked_list_head = None
        self.merged_linked_list = LinkedList()

    def merge_sorted_linked_list(self, node1 ,node2):
        if node1 is None:
            self.merged_linked_list = node1
        if node2 is None:
            self.merged_linked_list = node2
        while node1 is not None and node2 is not None:
            if node1.data <= node2.data:
                self.merged_linked_list.push(node1.data)
                node1 = node1.next
            elif node1.data > node2.data:
                self.merged_linked_list.push(node2.data)
                node2 = node2.next
        if node2 is None and  node1 is not None:
            self.merged_linked_list.append(node1)
        if node1 is None and node2 is not None:
            self.merged_linked_list.append(node2)

        return self.merged_linked_list

    def print_list(self):
        temp = self.merged_linked_list.head
        while temp:
            print(temp.data)
            temp = temp.next


if __name__ == '__main__':
    ll1 = LinkedList()
    ll1.push(2)
    ll1.push(3)
    ll1.push(4)
    ll1.push(45)
    # ll1.push(67)

    ll2 = LinkedList()
    ll2.push(3)
    ll2.push(5)
    ll2.push(43)
    ll2.push(78)

    print("Created linked list1 is :")
    ll1.print_list()

    print("Created Linked List2 is :")
    ll2.print_list()

    print("Sorted Linked List is :")
    sorted_merged_list = MergeSortedLinkedList()
    sorted_merged_list.merge_sorted_linked_list(ll1.head,ll2.head)
    # print(sorted_merged_list)
    sorted_merged_list.print_list()


