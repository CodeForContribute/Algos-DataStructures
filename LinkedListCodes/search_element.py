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

    # Iterative method
    # def search_element(self, key):
    #     temp = self.head
    #     # if self.head.data == key:
    #     #     return True
    #     while temp is not None:
    #         if temp.data == key:
    #             break
    #         temp = temp.next
    #
    #     if temp is None:
    #         return False
    #
    #     return True

    # Recursive method
    def search_element(self, li, key):
        if not li:
            return False
        if li.data == key:
            return True
        return self.search_element(li.next, key)

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.data)
            temp = temp.next


if __name__ == '__main__':
    ll = LinkedList()
    ll.push(89)
    ll.push(8)
    ll.push(9)
    ll.push(76)
    ll.push(7)
    print("Created Linked List is :")
    ll.print_list()
    print(ll.search_element(ll.head, 97))
