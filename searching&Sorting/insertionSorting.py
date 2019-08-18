def insertion_sorting(arr, n):
    for j in range(1, n):
        i = j - 1
        key = arr[j]
        while i >= 0 and arr[i] > key:
            arr[i + 1] = arr[i]
            i -= 1
        arr[i + 1] = key


if __name__ == '__main__':
    arr = [9, 8, 4, 10, 3, 5]
    n = len(arr)
    insertion_sorting(arr, n)
    for i in range(n):
        print(arr[i], end=" ")
