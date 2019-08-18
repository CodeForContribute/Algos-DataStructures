"""
Time Complexity of Binary Search is O(log(n))
Binary Search: Search a sorted array by repeatedly dividing the search interval in half.
Begin with an interval covering the whole array. If the value of the search key is less than the item in the middle of
the interval,narrow the interval to the lower half.
Otherwise narrow it to the upper half. Repeatedly check until the value is found or the interval is empty.
"""


# Recursive approach
def binary_search(arr, l, r, x):
    if l <= r:
        mid = int(l + (r - l) / 2)
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary_search(arr, l, mid - 1, x)
        elif arr[mid] < x:
            return binary_search(arr, mid + 1, r, x)
    else:
        return -1


# Iterative approach
def binary_iterative_approach(arr, left, right, x):
    while left <= right:
        mid = left + int((right - left) / 2)
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            right = mid - 1
        elif arr[mid] < x:
            left = mid + 1
    return -1


if __name__ == '__main__':
    arr = [12, 3, 5, 6]
    n = len(arr)
    x = 6
    print(binary_search(arr, 0, n - 1, x))
    print(binary_iterative_approach(arr,0,n-1,x))
