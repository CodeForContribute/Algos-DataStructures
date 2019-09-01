def pivotBinarySearch(arr, n, key):
    pivot = findPivot(arr,0, n-1)
    if pivot == -1:
        return binarySearch(arr, 0, n, key)
    if arr[pivot] == key:
        return pivot
    if arr[0] <= key:
        return binarySearch(arr, 0, pivot-1, key)
    return binarySearch(arr, pivot+1, n-1, key)

def findPivot(arr,low,high):
    if high < low:
        return -1
    if high == low:
        return low
    mid = int((low+high)//2)
    if mid < high and arr[mid] > arr[mid+1]:
        return mid
    if mid > low and arr[mid] < arr[mid-1]:
        return mid-1
    if arr[low] >= arr[mid]:
        return findPivot(arr, low, mid-1)
    return findPivot(arr, mid+1, high)

def binarySearch(arr,low,high, data):
    if high < low:
        return -1
    mid = int((low + high)//2)
    if data == arr[mid]:
        return mid
    if arr[mid] > data:
        return binarySearch(arr,low, mid-1, data)
    return  binarySearch(arr, mid+1, high, data)

################# Improved Solution ##############################
def search(arr, low, high, data):
    if low > high:
        return -1
    mid = (low + high)//2
    if arr[mid] == data:
        return mid
    if arr[low] <= arr[mid]:
        if arr[low] <= data <= arr[mid]:
            return search(arr,low,mid-1, data)
        return search(arr, mid+1, high, data)
    if arr[mid] <= data <= arr[high]:
        return search(arr, mid+1, high, data)
    return search(arr,low, mid-1, data)

if __name__ == '__main__':
    arr = [5,6,7,8,9,10,1,2,3]
    n = len(arr)
    key = 3
    print("Index of the element is:",pivotBinarySearch(arr, n, key))
    print("\n")
    print("Index of the element is:",search(arr, 0, n-1, key))

