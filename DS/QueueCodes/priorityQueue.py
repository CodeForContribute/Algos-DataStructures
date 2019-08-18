class PriorityQueue(object):
    def __init__(self):
        self._queue = []

    def __str__(self):
        return ''.join([str[i] for i in self._queue])

    def is_empty(self):
        return len(self._queue) == []

    def insert(self, data):
        self._queue.append(data)

    def delete(self):
        try:
            max_value = 0
            for i in range(len(self._queue)):
                if self._queue[i] > self._queue[max_value]:
                    max_value = i

            item = self._queue[max_value]
            del self._queue[max_value]
            return item
        except IndexError:
            print("Priority Queue is Empty")
            exit()


if __name__ == '__main__':
    pq = PriorityQueue()
    pq.insert(12)
    pq.insert(1)
    pq.insert(14)
    pq.insert(7)
    # pq.__str__()
    print(pq.is_empty())
    print(pq.delete())
