from heapq import heappop, heappushpop, heappush
import sys


class MinHeap:
    def __init__(self):
        self.heap = list()

    def parent(self, index):
        return (index - 1) // 2

    def insert_key(self, key):
        heappush(self.heap, key)

    def decrease_key(self, index, new_value):
        self.heap[index] = new_value
        while index != 0 and self.heap[self.parent(index)] > self.heap[index]:
            self.heap[index], self.heap[self.parent(index)] = self.heap[self.parent(index)], self.heap[index]
            index = self.parent(index)

    def extract_min(self):
        return heappop(self.heap)

    def delete_key(self, index):
        self.decrease_key(index, -sys.maxsize)
        self.extract_min()

    def get_min(self):
        return self.heap[0]


if __name__ == '__main__':
    heapObj = MinHeap()
    heapObj.insert_key(3)
    heapObj.insert_key(2)
    heapObj.delete_key(1)
    heapObj.insert_key(15)
    heapObj.insert_key(5)
    heapObj.insert_key(4)
    heapObj.insert_key(45)
    for i in range(len(heapObj.heap)):
        print(heapObj.heap[i], end=" ")
    print("\n")
    print(heapObj.extract_min())
    # print(heapObj.get_min())
    for i in range(len(heapObj.heap)):
        print(heapObj.heap[i], end=" ")

    heapObj.decrease_key(2, 1)
    print("\n")
    # print(heapObj.get_min())
    for i in range(len(heapObj.heap)):
        print(heapObj.heap[i], end=" ")
