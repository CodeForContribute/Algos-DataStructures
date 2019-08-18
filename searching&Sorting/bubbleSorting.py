"""

Worst and Average Case Time Complexity: O(n*n). Worst case occurs when array is reverse sorted.
Best Case Time Complexity: O(n). Best case occurs when array is already sorted.
Auxiliary Space: O(1)
Boundary Cases: Bubble sort takes minimum time (Order of n) when elements are already sorted.
Sorting In Place: Yes
Stable: Yes
Due to its simplicity, bubble sort is often used to introduce the concept of a sorting algorithm.
"""


def bubble_sorting(arr, n):
    for i in range(n):
        # Last i items will be sorted
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if swapped is False:
            break
    for i in range(n):
        print(arr[i], end=" ")


if __name__ == '__main__':
    arr = [64, 34, 25, 12, 22, 11, 90]
    n = len(arr)
    bubble_sorting(arr, n)
