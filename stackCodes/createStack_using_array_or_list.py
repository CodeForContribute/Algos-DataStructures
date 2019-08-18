from sys import maxsize


# Using array/list
class Stack:
    def __init__(self):
        self.stack = list()

    def is_empty(self):
        return len(self.stack) == 0

    def push(self, data):
        self.stack.append(data)
        print("Item  pushed to stack is %d:" % data)

    def pop_stack(self):
        if self.is_empty():
            return str(-maxsize - 1)
        return self.stack.pop()

    def peek(self):
        if self.is_empty():
            return str(-maxsize - 1)
        return self.stack[len(self.stack)-1]


if __name__ == '__main__':
    stack = Stack()
    stack.push(12)
    stack.push(34)
    stack.push(45)
    print(stack.pop_stack())
    print(stack.peek())

