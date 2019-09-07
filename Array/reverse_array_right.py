def reverse_array(arr, start, end):
    while start < end:
        arr[start] ,arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

def rightRotateArray(arr, d, n):
    reverse_array(arr, 0, n-1)
    reverse_array(arr, 0, d-1)
    reverse_array(arr, d, n-1)

def printArray(arr, n):
    for i in range(n):
        print(arr[i] ,end=" ")

if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    n = len(arr)
    k = 3

    # Function call
    rightRotateArray(arr, k, n)
    printArray(arr, n)
