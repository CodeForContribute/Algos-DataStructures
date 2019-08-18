"""
Time Complexity : O(log(n))
Space Complexity :O(log(n)) - height of tree == number of recursive calls
"""
import sys


class MinHeap:
    def __init__(self, capacity):
        self.arr = [None]*capacity
        self.capacity = capacity
        self.heap_size = 0

    def min_heapify(self, index):
        left = self.left_node(index)
        right = self.right_node(index)
        smallest = index
        if left <= self.heap_size and self.arr[left] < self.arr[index]:
            smallest = left
        if right <= self.heap_size and self.arr[right] < self.arr[smallest]:
            smallest = right
        if smallest != index:
            self.arr[index], self.arr[smallest] = self.arr[smallest], self.arr[index]
            self.min_heapify(smallest)

    def parent_node(self, index):
        return (index - 1) // 2

    def left_node(self, index):
        return 2 * index + 1

    def right_node(self, index):
        return 2 * index + 2

    def extract_min(self):
        if self.heap_size <= 0:
            return sys.maxsize
        if self.heap_size == 1:
            self.heap_size -= 1
            return self.arr[0]
        root = self.arr[0]
        self.heap_size -= 1
        self.min_heapify(0)
        return root

    def decrease_key(self, index, new_value):
        self.arr[index] = new_value
        while index > 1 and self.arr[self.parent_node(index)] > self.arr[index]:
            self.arr[index], self.arr[self.parent_node(index)] = self.arr[self.parent_node(index)], self.arr[index]
            index = self.parent_node(index)

    def increase_key(self, index, new_value):
        self.arr[index] = new_value
        while index > 1 and self.arr[self.parent_node(index)] > self.arr[index]:
            self.arr[index], self.arr[self.parent_node(index)] = self.arr[self.parent_node(index)], self.arr[index]
            index = self.parent_node(index)

    def get_min(self):
        return self.arr[0]

    def delete_key(self, index):
        self.decrease_key(index, -sys.maxsize)
        self.extract_min()

    def insert_key(self, key):
        if self.heap_size == self.capacity:
            print("OverFlow:Could not insert key\n")
            return
        self.heap_size += 1
        i = self.heap_size - 1
        self.arr[i] = key
        while i > 1 and self.arr[self.parent_node(i)] > self.arr[i]:
            self.arr[i], self.arr[self.parent_node(i)] = self.arr[self.parent_node(i)], self.arr[i]
            i = self.parent_node(i)


#
# def max_heapify(arr, index):
#     left = 2 * index
#     right = 2 * index + 1
#     if left <= arr.heap_size() and arr[left] > arr[index]:
#         largest = left
#     else:
#         largest = index
#     if right <= arr.heap_size() and arr[right] > largest:
#         largest = right
#     if largest != index:
#         arr[index], arr[largest] = arr[largest], arr[index]
#     max_heapify(arr, largest)
#
#
# def construct_binary_tree(arr, n):
#     heap_size = n
#     import math
#     for i in range(math.floor(n/2), 0):
#         max_heapify(arr, i)
#
# def heap_extract_max(arr, n):
#     if n < 1:
#         print("")


if __name__ == '__main__':
    arr = [14, 8, 10, 4, 7, 9, 3, 2, 1, 6]
    n = len(arr)
    min_heap = MinHeap(11)
    min_heap.insert_key(3)
    min_heap.insert_key(2)
    min_heap.insert_key(1)
    min_heap.insert_key(15)
    min_heap.insert_key(5)
    min_heap.insert_key(4)
    min_heap.insert_key(45)
    # print(min_heap.extract_min())
    # min_heap.decrease_key(2, 0)
    for i in range(len(min_heap.arr)):
        print(min_heap.arr[i], end=" ")
    min_heap.decrease_key(2, 0)
    print(min_heap.get_min())
    for i in range(len(min_heap.arr)):
        print(min_heap.arr[i], end=" ")
    print(min_heap.extract_min())
    print("\n")
    for i in range(len(min_heap.arr)):
        print(min_heap.arr[i], end=" ")
