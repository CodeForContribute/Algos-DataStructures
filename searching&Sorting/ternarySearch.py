"""
The following is recursive formula for counting comparisons in worst case of Binary Search.

   T(n) = T(n/2) + 2,  T(1) = 1
The following is recursive formula for counting comparisons in worst case of Ternary Search.

   T(n) = T(n/3) + 4, T(1) = 1
In binary search, there are 2Log2n + 1 comparisons in worst case. In ternary search, there are 4Log3n + 1 comparisons
in worst case.

Time Complexity for Binary search = 2clog2n + O(1)
Time Complexity for Ternary search = 4clog3n + O(1)
Therefore, the comparison of Ternary and Binary Searches boils down the comparison of expressions 2Log3n and Log2n .
The value of 2Log3n can be written as (2 / Log23) * Log2n . Since the value of (2 / Log23) is more than one,
Ternary Search does more comparisons than Binary Search in worst case.

Exercise:
Why Merge Sort divides input array in two halves, why not in three or more parts?
"""


def ternary_search(arr, left, right, x):
    if right >= left:
        mid1 = left + (right - left) // 3
        mid2 = mid1 + (right - left) // 3
        if arr[mid1] == x:
            return mid1
        if arr[mid2] == x:
            return mid2
        if arr[mid1] > x:
            return ternary_search(arr, left, mid1 - 1, x)
        if arr[mid1] > x:
            return ternary_search(arr, mid1 + 1, right, x)
        if arr[mid2] > x:
            return ternary_search(arr, left, mid2 - 1, x)
        if arr[mid2] < x:
            return ternary_search(arr, mid2 + 1, right, x)
    return -1


if __name__ == '__main__':
    arr = [0, 1, 1, 2, 3, 5, 8, 13, 21,
           34, 55, 89, 144, 233, 377, 610]
    x = 55
    n = len(arr)
    print(ternary_search(arr, 0, n - 1, x))
