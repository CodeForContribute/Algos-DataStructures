class Node:
    def __init__(self, new_data):
        self.data = new_data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.Set1 = set()
        self.Set2 = set()

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.data, end=" ")
            temp = temp.next

    def store_element_in_map(self, head1, head2):
        temp1 = head1
        temp2 = head2
        while temp1 is not None or temp2 is not None:
            if temp1 is not None:
                self.Set1.add(temp1.data)
                temp1 = temp1.next
            if temp2 is not None:
                self.Set2.add(temp2.data)
                temp2 = temp2.next


def union_and_intersection_of_two_lists(head1, head2):
    result = LinkedList()
    result.store_element_in_map(head1, head2)
    print("\n")
    print("Intersection of two Linked List is:")
    print(result.Set1.intersection(result.Set2))
    print("\n")
    print("Union of two Linked List is:")
    print(result.Set1.union(result.Set2))
    for x in result.Set2:
        print(x)


if __name__ == '__main__':
    ll = LinkedList()
    ll.push(12)
    ll.push(13)
    ll.push(14)
    ll.push(45)
    print("Created 1st Linked List is:")
    ll.print_list()

    ll2 = LinkedList()
    ll2.push(2)
    ll2.push(3)
    ll2.push(14)
    ll2.push(15)
    print("\n")
    print("Created 2nd Linked List is:")
    ll2.print_list()
    union_and_intersection_of_two_lists(ll.head, ll2.head)


