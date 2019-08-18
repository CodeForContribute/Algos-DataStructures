from sys import maxsize


class Stack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.top = -1
        self.stack = list()

    def is_empty(self):
        return True if self.top == -1 else False

    def pop_stack(self):
        if self.is_empty():
            return str(-maxsize - 1)
        else:
            self.top -= 1
            return self.stack.pop()

    def push(self, new_data):
        if self.top == len(self.stack):
            print("Stack OverFLow")
        self.stack.append(new_data)
        self.top += 1

    def peek(self):
        return self.stack[-1]

    def reverse_string(self, exp):
        if exp is None:
            print("string is empty")
            return
        length = len(exp)
        for i in range(0, length, 1):
            self.push(exp[i])
        print(self.stack)
        reverse_string = ""
        for i in range(0, len(exp), 1):
            reverse_string += self.stack.pop()
        print(reverse_string)

    def reverse_string_aux(self, string):
        reversed_string = string[::-1]
        print(reversed_string)


if __name__ == '__main__':
    exp = "Raushan"
    stack = Stack(len(exp))
    # stack.reverse_string(exp)
    stack.reverse_string_aux(exp)
