"""
Method1 : Brute Force Time complexity O(m*n)
"""


def is_subarray(arr1, arr2, m, n):
    for i in range(n):
        for j in range(m):
            if arr2[i] == arr1[j]:
                break
            if j == m:
                return 0
        return 1


"""
  Method2: Using Sorting and Binary Search
  Time Complexity : O(m*log(n))
"""


def binary_search(A, low, high, x):
    if high > low:
        mid = low + (high - low) // 2
        if (mid == 0 or x > A[mid]) and A[mid] == x:
            return mid
        elif x > A[mid]:
            binary_search(A, mid + 1, high, x)
        else:
            binary_search(A, low, mid - 1, x)


def is_sub_array(arr1, arr2, m, n):
    i = 0
    quick_sort(arr1, 0, m - 1)
    for i in range(n):
        if binary_search(arr1, 0, m - 1, arr2[i] == -1):
            return 0
    return 1


def partition(arr, start, end):
    x = arr[end]
    i = start - 1
    for j in range(start, end):
        if arr[j] <= x:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[end] = arr[end], arr[i + 1]
    return i + 1


def quick_sort(A, si, ei):
    if si < ei:
        pi = partition(A, si, ei)
        quick_sort(A, si, pi - 1)
        quick_sort(A, pi + 1, ei)


def is_sub_array_of_array(arr1, arr2, m, n):
    i = 0
    j = 0
    if m < n:
        return 0
    arr1.sort()
    arr2.sort()
    while i < n and j < m:
        if arr1[j] < arr2[i]:
            j += 1
        elif arr1[j] == arr2[i]:
            i += 1
            j += 1
        elif arr1[j] > arr2[i]:
            return 0
    return 0 if i < n else 1


if __name__ == '__main__':
    arr1 = [11, 1, 13, 21, 3, 7]
    arr2 = [11, 3, 7, 1]
    m = len(arr1)
    n = len(arr2)
    if is_sub_array_of_array(arr1, arr2, m, n) is True:
        print("arr2 is subarray of arr1")
    else:
        print("arr2 is not subarray of arr1")
