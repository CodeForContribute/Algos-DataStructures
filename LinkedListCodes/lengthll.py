
"""
Author:Raushan Kumar
Date:25/07/2019
This is iterative approach of counting number of nodes
"""

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#
# class LinkedList:
#     def __init__(self):
#         self.head = None
#
#     def push(self,new_data):
#         new_node = Node(new_data)
#         new_node.next = self.head
#         self.head = new_node
#
#     def count_number_nodes(self):
#         temp = self.head
#         count = 0
#         while temp is not None:
#             count += 1
#             temp = temp.next
#         return count
#
#     def print_list(self):
#         temp = self.head
#         while temp is not None:
#             print(temp.data)
#             temp = temp.next
#
# if __name__ == '__main__':
#     ll = LinkedList()
#     ll.push(89)
#     ll.push(90)
#     ll.push(8)
#     ll.push(9)
#     ll.push(890)
#     ll.push(0)
#     print("Created Linked list is :")
#     ll.print_list()
#     print("Number of nodes in Linked list is :")
#     print(ll.count_number_nodes())

"""
This is Recursive approach
For counting number of nodes
"""
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

    def count_number_nodes(self,node):
        if node is None:
            return 0
        else:
            return 1 + self.count_number_nodes(node.next)

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.data)
            temp = temp.next

if __name__ == '__main__':
    ll = LinkedList()
    ll.push(89)
    ll.push(90)
    ll.push(8)
    ll.push(9)
    ll.push(890)
    ll.push(0)
    print("Created Linked list is :")
    ll.print_list()
    print("Number of nodes in Linked list is :")
    print(ll.count_number_nodes(ll.head))


