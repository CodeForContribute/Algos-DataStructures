def heap_sort_iterative(arr, n):
    build_max_heap(arr, n)
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        while True:
            j = 0
            index = 2 * j +1
            if index < (i-1) and arr[index] < arr[index+1]:
                index += 1


def build_max_heap(arr, n):
    for i in range(n):
        # parent = i // 2
        if arr[i] > arr[int((i-1)/2)]:
            j = i
            while arr[j] > arr[int((j-1)/2)]:
                arr[j], arr[int((j-1)/2)] = arr[int((j-1)/2)], arr[j]
                j = int((j-1)/2)


def print_array(arr, n):
    for i in range(n):
        print(arr[i], end=" ")


if __name__ == '__main__':
    arr = [10, 20, 15, 17, 9, 21]
    n = len(arr)
    build_max_heap(arr, n)
    print_array(arr, n)
