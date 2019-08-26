def heapify(arr, n, index):
    largest = index
    left = 2*index + 1
    right = 2*index + 2
    if left < n and arr[index] < arr[left]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right
    if largest != index:
        arr[index], arr[largest] = arr[largest],arr[index]
        heapify(arr, n, largest)


def heapSort(arr,n):
    for i in range(n, -1, -1):
        heapify(arr, n, i)
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i,0)

if __name__ == '__main__':
    # Driver code to test above
    arr = [12, 11, 13, 5, 6, 7]
    heapSort(arr,len(arr))
    n = len(arr)
    print("Sorted array is")
    for i in range(n):
        print(arr[i],end=" "),
