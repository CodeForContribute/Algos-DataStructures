class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, x, y):
        new_node = Node(x, y)
        new_node.next = self.head
        self.head = new_node

    def print_list(self):
        temp = self.head
        while temp:
            print((temp.x, temp.y), end=" ")
            temp = temp.next

    # Recursive method
    def remove_middle_points_of_line_segments(self):
        if self.head is None or self.head.next is None or self.head.next.next is None:
            return self.head
        next_node = self.head.next
        next_next_node = next_node.next
        if self.head.x == next_node.x:
            while next_next_node is not None and next_node.x == next_next_node.x:
                self.head.next = next_node.next
                next_node.next = None
                next_node = next_next_node
                next_next_node = next_next_node.next
        elif self.head.y == next_node.y:
            while next_next_node is not None and next_node.y == next_next_node.y:
                self.head.next = next_node.next
                next_node.next = None
                next_node = next_next_node
                next_next_node = next_next_node.next
        else:
            print("Given list is not valid")
            return None
        temp = self.head
        self.head = self.head.next
        self.remove_middle_points_of_line_segments()
        self.head = temp
        return self.head

    # Iterative method
    def delete_middle_points_line_segment(self, head):
        temp = head.next
        prev = head
        while temp:
            if temp.x == prev.x:
                current = prev
                prev = temp
                temp = temp.next
                while temp and temp.x == prev.x:
                    pass


if __name__ == '__main__':
    ll = LinkedList()
    ll.push(40, 5)
    ll.push(20, 5)
    ll.push(7, 5)
    ll.push(7, 10)
    ll.push(5, 10)
    ll.push(1, 10)
    ll.push(0, 10)
    print("Created Linked List is:")
    ll.print_list()
    print("\n")
    print("Linked List after deleting the middle points of line segment is:")
    ll.remove_middle_points_of_line_segments()
    ll.print_list()

