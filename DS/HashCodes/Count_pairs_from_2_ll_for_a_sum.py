class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def print_ll(self):
        temp = self.head
        while temp is not None:
            print(temp.data, end=" ")
            temp = temp.next


def count_pair_sum(head1, head2, sum):
    count = 0
    temp1 = head1
    temp2 = head2
    while temp1 is not None and temp2 is not None:
        if temp1.data + temp2.data == sum:
            count += 1
        temp1 = temp1.next
        temp2 = temp2.next
    print(count)


# Using Merge Sort Technique
def merge_sort(head):
    temp = head
    if temp is None or temp.next is None:
        return
    a, b = front_back_split(temp)
    merge_sort(a)
    merge_sort(b)
    head_ref = sorted_merge(a, b)
    return head_ref


def front_back_split(source):
    slow = source
    fast = source
    while fast is not None and fast.next.next is not None:
        slow = slow.next
        fast = fast.next.next
    front_ref = source
    back_ref = slow.next
    slow.next = None
    return front_ref, back_ref


def sorted_merge(head1, head2):
    if head1 is None:
        return head2
    if head2 is None:
        return head1
    if head1.data < head2.data:
        result = head1
        result.next = sorted_merge(head1.next, head2)
    else:
        result = head2
        result.next = sorted_merge(head1, head2.next)

    return result


def count_sum_pairs_in_ll(head1, head2, sum):
    temp1 = head1
    temp2 = head2
    count = 0
    while temp1 is not None and temp2 is not None:
        if temp1.data + temp2.data == sum:
            count += 1
            temp1 = temp1.next
            temp2 = temp2.next
        elif temp1.data + temp2.data > sum:
            temp2 = temp2.next
        else:
            temp1 = temp1.next
    print(count)


if __name__ == '__main__':
    l1 = LinkedList()
    l2 = LinkedList()
    l1.push(7)
    l1.push(5)
    l1.push(1)
    l1.push(3)

    l2.push(3)
    l2.push(5)
    l2.push(2)
    l2.push(8)

    x = 10
    count_pair_sum(l1.head, l2.head, x)
    l2.head = merge_sort(l2.head)
    count_sum_pairs_in_ll(l1.head, l2.head, x)



