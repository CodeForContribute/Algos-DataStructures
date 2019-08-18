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
            print(temp.data,end=" ")
            temp = temp. next

    # Method 1:using HashMap
    def detect_loop(self):
        s = set()
        temp = self.head
        while temp:
            if temp in s:
                print("Loop found in Linked List")
                return True
            s.add(temp)

        return False

    # Method2 :using Floyd’s Cycle-Finding Algorithm
    def detect_loop_in_linked_list(self):
        slow_ptr = self.head
        fast_ptr = self.head
        while slow_ptr and fast_ptr and fast_ptr.next:
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next
            if slow_ptr == fast_ptr:
                print("Found Loop in Linked List")
                return True

    # Method3 : using a temporary node
    def detect_loop_in_linked_list_using_temp_node(self):
        temp = Node(0)
        while self.head is not None:
            if self.head.next is None:
                return False
            if self.head.next == temp:
                print("Found Loop in Linked List")
                return True
            next_node = self.head.next
            self.head.next = temp
            self.head = next_node


if __name__ == '__main__':
    ll = LinkedList()
    ll.push(90)
    ll.push(89)
    ll.push(78)
    ll.push(34)
    ll.head.next.next.next.next = ll.head.next.next
    print("\n")
    ll.detect_loop()
    ll.detect_loop_in_linked_list()
    ll.detect_loop_in_linked_list_using_temp_node()
