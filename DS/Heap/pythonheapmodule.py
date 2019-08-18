import heapq

if __name__ == '__main__':
    # initializing list 1
    li1 = [5, 7, 9, 4, 3]

    # initializing list 2
    li2 = [5, 7, 9, 4, 3]
    # Using heapify() to convert list into heap
    heapq.heapify(li1)
    heapq.heapify(li2)
    for i in range(len(li1)):
        print(li1[i], end=" ")
    # Using heappushpop() to push and pop items simultaneously
    # print(heapq.heappushpop(li1, 2))
