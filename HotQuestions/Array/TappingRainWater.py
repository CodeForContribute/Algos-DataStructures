def findWaterTrapped(arr, n):
    result = 0
    left_max = 0
    right_max = 0
    low = 0
    high = n-1
    while low <= high:
        if arr[low] < arr[high]:
            if arr[low] > left_max:
                left_max = arr[low]
            else:
                result += left_max-arr[low]
            low += 1
        else:
            if arr[high] > right_max:
                right_max = arr[high]
            else:
                result += right_max - arr[high]
            high -= 1

    return result

if __name__ == '__main__':
    arr = [3, 0, 0, 2, 0, 4]
    n = len(arr)
    print("Maximum water that can be accumulated is:")
    print(findWaterTrapped(arr, n))