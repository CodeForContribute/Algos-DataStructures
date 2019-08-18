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
        while temp:
            print(temp.data, end=" ")
            temp = temp.next

    @staticmethod
    def alternate_odd_even_nodes(head):
        odd = list()
        even = list()
        position = 1
        while head is not None:
            if head.data % 2 != 0 and position % 2 == 0:
                odd.append(head)
            elif head.data % 2 == 0 and position % 2 != 0:
                even.append(head)
            head = head.next
            position += 1
        while len(even) != 0 and len(odd) != 0:
            temp = odd.pop().data
            temp2 = even.pop().data
            temp3 = temp
            temp = temp2
            temp2 = temp3
            # node = even.pop()
            # print(node.data)

    # segregate odd and even nodes
    # split the list into odd and even lists
    # Merge even list into odd lists
    def alternate_nodes_ll_using_splitting(self, ):
        # segregate odd and even nodes
        current = self.head.next
        prev = self.head
        while current is not None:
            # Back up the next pointer of current
            temp = current.next
            if current.data % 2 != 0:
                prev.next = temp
                current.next = self.head
                self.head.next = current
            else:
                prev = current
            # Advance current pointer
            current = temp
        # step2: split the Lists into even and odd nodes
        current = self.head.next
        prev = self.head
        while current is not None and current.data % 2 != 0:
            prev = current
            current = current.next
        even = current
        prev.next = None
        i = self.head
        j = even
        while j is not None and i is not None:
            k = i.next
            l = j.next
            i.next = j
            j.next = k
            ptr = j
            i = k
            j = l
            if i is None:
                ptr.next = j
        return self.head


if __name__ == '__main__':
    ll = LinkedList()
    ll.push(9)
    ll.push(1)
    ll.push(2)
    ll.push(4)
    ll.push(5)
    ll.push(6)
    ll.push(7)
    print("Created Linked List is:")
    ll.print_list()
    print("\n")
    print("Linked List after alternating even and odd nodes:")
    ll.alternate_nodes_ll_using_splitting()
    ll.print_list()
