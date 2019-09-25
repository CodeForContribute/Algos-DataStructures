class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class LLNode:
    def __init__(self, data):
        self.data = data
        self.next = None


def push(head, data):
    new_node = LLNode(data)
    new_node.next = head
    head = new_node
    return head


def printList(head):
    temp = head
    while temp:
        print(temp.data, end=" ")
        temp = temp.next


def ConstructBinaryTreeLL(head):
    if not head:
        return None
    q = []
    root = Node(head.data)
    q.append(root)
    head = head.next
    while head:
        parent = q.pop(0)
        rightChild = None
        leftChild = Node(head.data)
        q.append(leftChild)
        head = head.next
        if head:
            rightChild = Node(head.data)
            q.append(rightChild)
            head = head.next
        parent.left = leftChild
        parent.right = rightChild
    return root


def inorder(root):
    if not root:
        return
    inorder(root.left)
    print(root.data, end=" ")
    inorder(root.right)


if __name__ == '__main__':
    head = None
    head = push(head, 10)
    head = push(head, 12)
    head = push(head, 15)
    head = push(head, 25)
    head = push(head, 30)
    head = push(head, 36)
    printList(head)
    print("\n")
    root = ConstructBinaryTreeLL(head)
    inorder(root)
