class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def detectLoopUsingSet(head):
    if not head:
        return
    temp = head
    s = set()
    while temp:
        if temp.data in s:
            return True
        s.add(temp.data)
        temp = temp.next

def detectLoop(head):
    if not head:
        return
    slow_ptr  = head
    fast_ptr = head
    while slow_ptr and fast_ptr and fast_ptr.next:
        slow_ptr = slow_ptr.next
        fast_ptr =fast_ptr.next.next
        if slow_ptr == fast_ptr:
            print("Loop Found")
            return True
    return False


if __name__ == '__main__':
    head = Node(1)
    head.next = Node(23)
    head.next.next = Node(2)
    head.next.next.next = Node(46)
    head.next.next.next.next = Node(3)
    head.next.next.next.next.next = Node(69)
    head.next.next.next.next.next.next = head
    temp = detectLoop(head)
    if not temp:
        print("Not Found")
    temp2 = detectLoopUsingSet(head)
    if temp2:
        print("Loop Found")
    else:
        print("Not Found")
