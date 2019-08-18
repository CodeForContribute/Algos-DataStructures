class Node:
    def __init__(self, new_data):
        self.data = new_data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.counter = 0

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def count_occur_node(self, key):
        count = 0
        temp = self.head
        while temp is not None:
            if temp.data == key:
                count += 1
            temp = temp.next
        return count

    def count_occurances_node_recursive(self, head, key):
        if not head:
            return self.counter
        if head.data == key:
            self.counter = self.counter + 1
        return self.count_occurances_node_recursive(head.next, key)

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.data, end=" ")
            temp = temp.next


if __name__ == '__main__':
    ll = LinkedList()
    ll.push(90)
    ll.push(8)
    ll.push(45)
    ll.push(56)
    ll.push(56)
    ll.push(56)
    ll.push(56)
    ll.push(56)
    ll.push(56)
    ll.push(78)
    ll.push(78)
    ll.push(78)
    ll.push(78)

    ll.print_list()
    node = 56
    count1 = ll.count_occur_node(node)
    print("\n")
    print("Count of %d is %d :" % (node, count1))
    ll.count_occurances_node_recursive(ll.head, node)
    count2 = ll.counter
    print("Count of %d is %d :" % (node, count2))
