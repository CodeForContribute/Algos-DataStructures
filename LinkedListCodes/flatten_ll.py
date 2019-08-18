# class Node:
#     def __init__(self, new_data):
#         self.data = new_data
#         self.right = None
#         self.down = None
#
#
# class LinkedList:
#     def __init__(self):
#         self.head = None
#
#     def push(self, new_data):
#         new_node = Node(new_data)
#         new_node.right = None
#         new_node.down = self.head
#         self.head = new_node
#
#     def print_list(self):
#         temp = self.head
#         while temp is not None:
#             print(temp.data, end=" ")
#             temp = temp.down
#
#     def flatten_linked_list(self, root):
#         if root is None or root.right is None:
#             return root
#         return self.merge(root, self.flatten_linked_list(root.right))
#
#     def merge(self, head1, head2):
#         if head1 is None:
#             return head2
#         if head2 is None:
#             return head1
#         result = None
#         if head1.data < head2.data:
#             result = head1
#             result.down = self.merge(head1.down, head2)
#         else:
#             result = head2
#             result.down = self.merge(head1, head2.down)
#
#
# if __name__ == '__main__':
#     ll = LinkedList()
#     ll.push(30)
#     ll.push(8)
#     ll.push(7)
#     ll.push(5)
#     print("First Linked List is:")
#     ll.print_list()
#     print("\n")
#
#     l2 = LinkedList()
#     l2.push(20)
#     l2.push(10)
#     print("Second Linked List is:")
#     l2.print_list()
#
#     print("\n")
#     l3 = LinkedList()
#     l3.push(50)
#     l3.push(22)
#     l3.push(19)
#     print("Third linked List is:")
#     l3.print_list()
#
#     ll.right = l2
#     l2.right = l3
#     # ll_new = LinkedList()
#     root = ll.flatten_linked_list(ll.head)
#     ll.print_list()
