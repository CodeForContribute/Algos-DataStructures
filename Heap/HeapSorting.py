def heapify(arr, n, index):
    largest = index
    left_node = 2 * index + 1
    right_node = 2 * index + 2
    if left_node < n and arr[left_node] > arr[largest]:
        largest = left_node
    if right_node < n and arr[right_node] > arr[largest]:
        largest = right_node
    if largest != index:
        arr[index], arr[largest] = arr[largest], arr[index]
        heapify(arr, n, largest)


def heap_sort_binary(arr, n):
    for i in range(n - 2 // 2, -1, -1):
        heapify(arr, n, i)
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)


def print_array(arr, n):
    for i in range(n):
        print(arr[i], end=" ")


if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6, 7]
    n = len(arr)
    # heap_sort(arr, n) 13 11 12 5 6 7
    heap_sort_binary(arr, n)
    print_array(arr, n)
