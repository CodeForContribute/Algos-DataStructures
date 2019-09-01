def sort012(arr, n):
    low = 0
    mid = 0
    high = n-1
    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1

        else:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1

def printArray(arr, n):
    for i in range(n):
        print(arr[i], end=" ")

if __name__ == '__main__':
    arr = [ 0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]
    n = len(arr)
    sort012(arr, n)
    printArray(arr, n)