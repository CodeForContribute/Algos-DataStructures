class Node:
    def __init__(self, new_data):
        self.data = new_data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.stack = list()

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data,end=" ")
            temp = temp.next

    def is_palindrome(self):
        temp = self.head
        while temp:
            self.stack.append(temp.data)
            temp = temp.next

        temp2 = self.head
        while temp2:
            if temp2.data != self.stack.pop():
                break
            temp2 = temp2.next
        if temp2 is None:
            return True
        return False

    def get_middle_node(self):
        slow_ptr = self.head
        fast_ptr = self.head
        while slow_ptr and fast_ptr and fast_ptr.next:
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next
        return slow_ptr

    @staticmethod
    def reverse_linked_list(head):
        prev = None
        current = head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        head = prev
        return head

    @staticmethod
    def compare_two_linked_lists(head1, head2):
        if head1 is None:
            return False
        if head2 is None:
            return False
        while head1 and head2:
            if head1.data != head2.data:
                break
            head1 = head1.next
            head2 = head2.next
        if head2 is None and head1 is None:
            return True
        return False

    @staticmethod
    def merge_linked_lists(head1, head3):
        temp = head1
        while temp.next:
            temp = temp.next
        # temp2 = head3
        # while temp2:
        #     temp.next = temp2
        #     temp2 = temp2

    def is_palindrome_reversing_list(self):
        mid = self.get_middle_node()
        head1 = self.head
        head2 = self.reverse_linked_list(mid)
        is_palindrome = self.compare_two_linked_lists(head1, head2)
        head3 = self.reverse_linked_list(head2)
        print(head3.data)
        self.merge_linked_lists(head1, head3)
        return is_palindrome


if __name__ == '__main__':
    ll = LinkedList()
    ll.push('a')
    ll.push('b')
    ll.push('c')
    ll.push('b')
    ll.push('a')
    print("Created Linked List:")
    ll.print_list()
    print("\n")
    print(ll.is_palindrome())
    print(ll.is_palindrome_reversing_list())
    ll.print_list()
