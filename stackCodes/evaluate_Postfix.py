from sys import maxsize


class EvaluatePostfix:
    def __init__(self, capacity):
        self.top = -1
        self.capacity = capacity
        self.array = list()

    def is_empty(self):
        return True if self.top == -1 else False

    def peek(self):
        if self.is_empty():
            return str(-maxsize-1)
        return self.array[-1]

    def pop(self):
        if self.is_empty():
            return "$"
        else:
            self.top -= 1
            return self.array.pop()

    def push(self, op):
        self.top += 1
        self.array.append(op)

    def evaluate_postfix_exp(self, exp):
        for i in exp:
            if i.isdigit():
                self.push(i)
            else:
                val1 = self.pop()
                val2 = self.pop()
                self.push(str(eval(val2 + i + val1)))
        return int(self.pop())


if __name__ == '__main__':
    exp = "231*+9-"
    obj = EvaluatePostfix(len(exp))
    print(obj.evaluate_postfix_exp(exp))
