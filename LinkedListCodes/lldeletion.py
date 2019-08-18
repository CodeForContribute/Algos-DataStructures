
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def delete_node(self, key):
        temp = self.head
        prev = None
        if temp is not None:
            if temp.data == key:
                self.head = temp.next
                temp = None
                return

        while temp is not None:
            if temp.data == key:
                break
            prev = temp
            temp = temp.next
        if temp is None:
            return
        prev.next = temp.next
        temp = None

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next



if __name__ == '__main__':
    llist = LinkedList()
    llist.push(34)
    llist.push(2)
    llist.delete_node(34)
    llist.delete_node(2)
    print("created linked list is :")
    llist.print_list()

