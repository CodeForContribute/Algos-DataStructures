def countingRotations(arr, n):
    for i in range(n-1):
        if arr[i] > arr[i+1]:
            return i+1
    return 0

# Time complexity of the search can be reduced by using binary search -> O(log(n))

def countingRotations_using_binarySearch(arr,low, high):
    if high < low:
        return 0
    if high == low:
        return 0
    mid = low + int((high-low))//2
    if mid < high and arr[mid+1] < arr[mid]:
        return mid+1
    if mid > low and arr[mid] < arr[mid-1]:
        return mid
    if arr[high] > arr[mid]:
        return countingRotations_using_binarySearch(arr, low, mid-1)
    return countingRotations_using_binarySearch(arr, mid+1, high)

if __name__ == '__main__':
    arr = [7, 9, 11, 12, 5]
    n = len(arr)
    a = countingRotations(arr, n)
    print(a)
    b = countingRotations_using_binarySearch(arr, 0, n-1)
    print(b)