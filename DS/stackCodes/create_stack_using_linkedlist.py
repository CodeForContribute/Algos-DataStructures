from sys import maxsize


class StackNode:
    def __init__(self, new_data):
        self.data = new_data
        self.next = None


class Stack:
    def __init__(self):
        self.root = None

    def is_empty(self):
        return True if self.root is None else False

    def push(self, new_data):
        new_node = StackNode(new_data)
        new_node.next = self.root
        self.root = new_node
        print("Pushed Node to stack is: %d" % new_data)

    def pop_stack(self):
        if self.is_empty():
            return float(-maxsize-1)
        temp = self.root
        self.root = self.root.next
        popped = temp.data
        temp = None
        return popped

    def peek(self):
        if self.is_empty():
            return float(-maxsize-1)
        return self.root.data


if __name__ == '__main__':
    stack = Stack()
    stack.push(10)
    stack.push(20)
    stack.push(30)
    print(stack.pop_stack())
    print(stack.pop_stack())
    print(stack.pop_stack())
    print(stack.peek())
    print(stack.is_empty())
