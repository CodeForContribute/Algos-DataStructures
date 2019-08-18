# class Node:
#     def __init__(self, new_data):
#         self.data = new_data
#         self.next = None
#
#
# class CircularLinkedList:
#     def __init__(self):
#         self.head = None
#
#     def push(self, new_data):
#         new_node = Node(new_data)
#         temp = self.head
#         new_node.next = self.head
#         if self.head is not None:
#             while temp is not None:
#                 while temp.next != self.head:
#                     temp = temp.next
#                 temp.next = new_node
#         else:
#             new_node.next = new_node
#
#         self.head = new_node
#
#     def print_list(self):
#         temp = self.head
#         if self.head is not None:
#             while True:
#                 print(temp.data, end=" ")
#                 temp = temp.next
#                 if temp == self.head:
#                     break
#
#
# if __name__ == '__main__':
#     cl = CircularLinkedList()
#     print("CL")
#     cl.push(1)
#     cl.push(2)
#     cl.push(3)
#     cl.push(4)
#     cl.push(5)
#     print("Created Circular Linked List is:")
#     cl.print_list()
# Python program to demonstrate
# circular linked list traversal

# Structure for a Node


class Node:

    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:

    # Constructor to create a empty circular linked list
    def __init__(self):
        self.head = None

    # Function to insert a node at the beginning of a
    # circular linked list
    def push(self, data):
        ptr1 = Node(data)
        temp = self.head

        ptr1.next = self.head

        # If linked list is not None then set the next of
        # last node
        if self.head is not None:
            while temp.next != self.head:
                temp = temp.next
            temp.next = ptr1

        else:
            ptr1.next = ptr1  # For the first node

        self.head = ptr1

    # Function to print nodes in a given circular linked list
    def printList(self):
        temp = self.head
        if self.head is not None:
            while temp.next != self.head:
                print(temp.data, end=" "),
                temp = temp.next
            print(temp.data)


if __name__ == '__main__':
    cllist = CircularLinkedList()
    cllist.push(12)
    cllist.push(56)
    cllist.push(2)
    cllist.push(11)
    print("Contents of circular Linked List")
    cllist.printList()


