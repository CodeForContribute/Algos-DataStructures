class LinkedList:
    def __init__(self, data):
        self.data = data
        self.next = None



class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None



class Conversion:
    def __init__(self, data = None):
        self.head = None
        self.root = None

    def push(self, data):
        new_node = LinkedList(data)
        new_node.next = self.head
        self.head = new_node

    def convertList2Binary(self):
        queue = []
        if self.head is None:
            self.root = None
            return
        self.root = Node(self.head.data)
        queue.append(self.root)
        self.head = self.head.next
        while self.head:
            parent = queue.pop(0)
            rightChild = None
            leftChild = Node(self.head.data)
            queue.append(leftChild)
            self.head = self.head.next
            if self.head:
                rightChild = Node(self.head.data)
                queue.append(rightChild)
                self.head = self.head.next
            parent.left = leftChild
            parent.right = rightChild

    def Inorder(self, root):
        if not root:
            return
        self.Inorder(root.left)
        print(root.data, end=" ")
        self.Inorder(root.right)

if __name__ == '__main__':
    # Driver Program to test above function

    # Object of conversion class
    conv = Conversion()
    conv.push(36)
    conv.push(30)
    conv.push(25)
    conv.push(15)
    conv.push(12)
    conv.push(10)

    conv.convertList2Binary()

    print("Inorder Traversal of the contructed Binary Tree is:")
    conv.Inorder(conv.root)
