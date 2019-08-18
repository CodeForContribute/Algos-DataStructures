class Queue:
    def __init__(self):
        self.stack1 = list()
        self.stack2 = list()

    # Method1 : By making enQueue operation Costly
    def enqueue(self, data):
        while len(self.stack1) != 0:
            self.stack2.append(self.stack1.pop())
        self.stack1.append(data)

        while len(self.stack2) != 0:
            self.stack1.append(self.stack2.pop())

    def de_queue(self):
        if len(self.stack1) == 0:
            print("Queue is Empty")
            return
        return self.stack1.pop()

    # Method2 : Making DeQueue Costly
    def enqueue_less_costly(self, data):
        self.stack1.append(data)

    def dequeue_costly(self):
        if len(self.stack1) == 0 and len(self.stack2) == 0:
            print("Queue is Empty")
            return
        if len(self.stack2) == 0:
            while len(self.stack1) != 0:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()

    # Method: dequeue_costly using function call stack
    # def enqueue_less_costly(self, data):
    #     self.stack1.append(data)
    #
    # def dequeue_less_costly_recursion(self):
    #     if len(self.stack1) == 0:
    #         return
    #     x = None
    #     if len(self.stack1) == 1:
    #         x = self.stack1.pop()
    #         return x
    #     res = self.dequeue_less_costly_recursion()
    #     self.stack1.append(x)
    #     return res


if __name__ == '__main__':
    queue = Queue()
    queue.enqueue_less_costly(1)
    queue.enqueue_less_costly(2)
    queue.enqueue_less_costly(3)
    queue.enqueue_less_costly(4)
    queue.enqueue_less_costly(5)
    queue.enqueue_less_costly(6)
    queue.enqueue_less_costly(7)
    # print(queue.dequeue_costly())
    print(queue.dequeue_costly())
    for i in range(len(queue.stack2)):
        print(queue.stack2[i], end=" ")
    # for i in range(len(queue.stack1)):
    #     print(queue.stack1[i], end=" ")
