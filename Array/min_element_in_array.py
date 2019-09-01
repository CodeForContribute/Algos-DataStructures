def findMinElementSortedRotatedArray(arr, low, high):
    if high < low:
        return  arr[0]
    if high == low:
        return arr[0]
    mid = low + (high-low)//2
    if mid < high and arr[mid+1] < arr[mid]:
        return arr[mid+1]
    if mid > low and arr[mid-1] > arr[mid]:
        return arr[mid]
    if arr[high] > arr[mid]:
        return findMinElementSortedRotatedArray(arr, low, mid-1)
    return findMinElementSortedRotatedArray(arr, mid+1, high)

if __name__ == '__main__':
    arr = [5, 6, 1, 2, 3, 4]
    n = len(arr)
    print(findMinElementSortedRotatedArray(arr, 0, n-1))