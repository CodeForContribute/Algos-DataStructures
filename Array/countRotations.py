######### Time Complexity : O(n) #########
def countRotations(arr, n):
    for i in range(n):
        if arr[i] > arr[i+1]:
            return i+1

#######Using Binary Search #######
def binarySearchRotations(arr, low, high):
    if high < low:
        return 0
    if high == low:
        return low
    mid = low + (high-low)//2
    ## check if mid+1 is min element
    if mid < high and arr[mid+1] < arr[mid]:
        return mid+1
    ### check if mid itself is min element
    if mid > low and arr[mid] < arr[mid-1]:
        return mid
    ### Decide weather we need to go to left or right half
    if arr[high] > arr[mid]:
        return binarySearchRotations(arr, low, mid-1)
    return binarySearchRotations(arr, mid+1, high)


if __name__ == '__main__':
    arr = [15, 18,90, 2, 3, 6, 12]
    n = len(arr)
    print(countRotations(arr, n))
    print(binarySearchRotations(arr,0, n-1))