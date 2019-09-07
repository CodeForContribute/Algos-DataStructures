import sys
def findElement(arr, n):
    leftMax = [None]*n
    leftMax[0] = -sys.maxsize
    for i in range(1, n):
        leftMax[i] = max(leftMax[i-1], arr[i-1])
    right_min = sys.maxsize
    for j in range(n-1,-1, -1):
        if leftMax[j] < arr[j] < right_min:
            return j
        right_min = min(right_min, arr[j])

    return -1

if __name__ == '__main__':
    arr = [5, 1, 4, 3, 6, 8, 10, 7, 9]
    n = len(arr)
    print("Index of the element is", findElement(arr, n))