import sys


def restore_down(arr, n, index, k):
    child_nodes = [None] * (k + 1)
    while True:
        for i in range(1, k + 1):
            child_nodes[i] = (k * index + i) if (k * index + i) < n else -1

        max_child = -1
        max_child_index = None

        for i in range(1, k + 1):
            if child_nodes[i] != -1 and arr[child_nodes[i]] > max_child:
                max_child = arr[child_nodes[i]]
                max_child_index = child_nodes[i]

        if max_child == -1:
            break

        if arr[index] < arr[max_child_index]:
            arr[index], arr[max_child_index] = arr[max_child_index], arr[index]

        index = max_child_index


def restore_up(arr, n, index, k):
    parent = (index - 1) // k
    while parent >= 0:
        if arr[index] > arr[parent]:
            arr[index], arr[parent] = arr[parent], arr[index]
            index = parent
            parent = (index - 1) // k
        else:
            break


def build_heap(arr, n, k):
    for i in range((n - 1) // k, -1, -1):
        restore_down(arr, n, i, k)


def extract_min(arr, n, k):
    maximum_number = arr[0]
    arr[0] = arr[n - 1]
    n = n - 1
    restore_down(arr, n, 0, k)
    # del arr[n-1]
    return maximum_number


def insert(arr, n, k, item):
    arr[n - 1] = item
    # n = n + 1
    restore_up(arr, n, n - 1, k)


def print_heap(arr, n):
    for i in range(n):
        print(arr[i], end=" ")


if __name__ == '__main__':
    arr = [4, 5, 6, 7, 8, 9, 10]
    n = len(arr)
    k = 3
    build_heap(arr, n, k)
    insert(arr, n, k, 100)
    print_heap(arr, n)
    print("\n")
    print(extract_min(arr, n, k))
    print_heap(arr, n)
