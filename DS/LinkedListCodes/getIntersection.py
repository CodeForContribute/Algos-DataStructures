# class Node:
#     def __init__(self, new_data):
#         self.data = new_data
#         self.next = None
#
#
# class LinkedList:
#     def __init__(self):
#         self.head = None
#
#     def push(self, new_data):
#         new_node = Node(new_data)
#         new_node.next = self.head
#         self.head = new_node
#
#     def print_list(self):
#         temp = self.head
#         while temp:
#             print(temp.data, end=" ")
#             temp = temp.next
#
#     @staticmethod
#     def get_intersection_point_using_hash(head1, head2):
#         s = set()
#         temp = head1
#         while temp:
#             s.add(temp.data)
#
#         temp2 = head2
#         while temp2:
#             if temp2.data in s:
#                 break
#             temp2 = temp2.next
#         return temp2.data
#
#     @staticmethod
#     def get_intersection_point_ll(head1, head2):
#         temp = head1
#         count1 = 0
#         while temp:
#             count1 += 1
#             temp = temp.next
#
#         temp2 = head2
#         count2 = 0
#         while temp2:
#             count2 += 1
#             temp2 = temp2.next
#         diff = abs(count1 - count2)
#         if count1 > count2:
#             temp = head1
#             while temp is not None and diff > 0:
#                 temp = temp.next
#                 diff = diff-1
#         elif count2 > count1:
#             temp = head2
#             while temp is not None and diff > 0:
#                 temp = temp.next
#                 diff -= 1
#         temp2 = head2
#         while temp2 is not None and temp is not None:
#             if temp2.data == temp.data:
#                 return temp.data
#             else:
#                 temp = temp.next
#                 temp2 = temp2.next
#
#     @staticmethod
#     def get_intersection_points(head1, head2):
#         temp = head1
#         while temp.next:
#             temp = temp.next
#         last_node = temp
#         temp.next = head1
#         slow_ptr = head2
#         fast_ptr = head2
#         while slow_ptr and fast_ptr and fast_ptr.next:
#             slow_ptr = slow_ptr.next
#             fast_ptr = fast_ptr.next.next
#
#
# if __name__ == '__main__':
#     ll = LinkedList()
#     ll.push(9)
#     ll.push(34)
#     ll.push(45)
#     ll.push(56)
#     ll.push(67)
#     ll.push(89)
#
#     ll2 = LinkedList()
#     ll2.push(23)
#     ll2.push(5)
#     ll2.head.next.next = ll.head.next.next.next
#
#     print("Created 1st Linked List is:")
#     ll.print_list()
#     print("\n")
#     print("Created 2nd Linked List is:")
#     ll2.print_list()
#     print("\n")
#     print(ll.get_intersection_point_ll(ll.head, ll2.head))
#     # (ll.get_intersection_point_using_hash(ll.head, ll2.head))


class Solution:
    # @param A : head node of linked list
    # @param B : head node of linked list
    # @return the head node in the linked list
    def getIntersectionNode(self, A, B):
        temp = A
        count1 = 0
        while temp:
            count1 += 1
            temp = temp.next

        temp2 = B
        count2 = 0
        while temp2:
            count2 += 1
            temp2 = temp2.next
        diff = abs(count1 - count2)
        if count1 > count2:
            temp = A
            while temp is not None and diff > 0:
                temp = temp.next
                diff = diff - 1
        elif count2 > count1:
            temp = B
            while temp is not None and diff > 0:
                temp = temp.next
                diff -= 1
        temp2 = B
        while temp2 is not None and temp is not None:
            if temp2.value == temp.value:
                return temp
            else:
                temp = temp.next
                temp2 = temp2.next


class Solution1(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        headADict = {}

        current = headA
        while current is not None:
            headADict[current] = True
            current = current.next

        current = headB
        while current is not None:
            if current in headADict:
                return current
            current = current.next
