##################################################################################################################
### Time Complexity : O(n + k*log(n)) Worst case:O(nLog(n)) when k == n
class MinHeap:
    def __init__(self, heap_size):
        self._heap_size = heap_size
        self.harr = []

    def parent(self, index):
        return (index - 1) // 2

    def left(self, index):
        return (2 * index) + 1

    def right(self, index):
        return (2 * index) + 2

    def min_heap(self, arr, n):
        self._heap_size = n
        self.harr = arr
        index = (self._heap_size - 1) // 2
        while index >= 0:
            self.min_heapify(index)
            index -= 1

    def min_heapify(self, index):
        left = self.left(index)
        right = self.right(index)
        smallest = index
        if left < self._heap_size and self.harr[left] < self.harr[smallest]:
            smallest = left
        if right < self._heap_size and self.harr[right] < self.harr[smallest]:
            smallest = right
        if smallest != index:
            self.harr[index], self.harr[smallest] = self.harr[smallest], self.harr[index]
            self.min_heapify(smallest)

    def extract_min(self):
        import sys
        if self._heap_size == 0:
            return sys.maxsize
        root = self.harr[0]
        if self._heap_size > 1:
            self.harr[0] = self.harr[self._heap_size - 1]
            self.min_heapify(0)
        self._heap_size -= 1
        return root

    def getmin(self):
        return self.harr[0]

    def kthSmallest(self, arr, k, n):
        self.min_heap(arr, n)
        for i in range(0,k-1):
            self.extract_min()
        print(self.getmin())


if __name__ == '__main__':
    arr = [12, 3, 5, 7, 19]
    n = len(arr)
    k = 3
    cls = MinHeap(n)
    cls.min_heap(arr, n)
    cls.kthSmallest(arr, k, n)
