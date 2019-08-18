"""
Time Complexity : O(Log n)
Auxiliary Space : The above implementation of Binary Search is recursive and requires O(Log n) space. With iterative
Binary Search, we need only O(1) space.

Applications of Exponential Search:
  1. Exponential Binary Search is particularly useful for unbounded searches, where size of array is infinite.
  2.It works better than Binary Search for bounded arrays, and also when the element to be searched is closer to the
    first element.
"""


def exponential_search(arr, n, x):
    if arr[0] == x:
        return 0
    i = 1
    while i < n and arr[i] < x:
        i *= 2
    return binary_search(arr, i // 2, min(i, n), x)


def binary_search(arr, left, right, x):
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
    arr = [0, 1, 1, 2, 3, 5, 8, 13, 21,
           34, 55, 89, 144, 233, 377, 610]
    x = 55
    n = len(arr)
    print(exponential_search(arr, n, 55))
