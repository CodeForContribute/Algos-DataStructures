"""
Time Complexity is O(n*log(n)) if we use merge_sort or heap_Sort
                   O(n^2) if we use Quick Sort
Space Complexity: O(n) auxiliary space for merge Sort
                   O(1) for heap Sort
    *** Better performance can be achieved through Hashing--> See in Hashing Module
"""


def pair_in_array_with_given_sum(arr, n, given_sum):
    arr.sort()
    start = 0
    end = n-1
    while start < end:
        if arr[start] + arr[end] == given_sum:
            return arr[start], arr[end]
        elif arr[start] + arr[end] < given_sum:
            start += 1
        else:
            end -= 1


if __name__ == '__main__':
    arr1 = [12, 2, 56, 3, 8, 9]
    m = len(arr1)
    print(pair_in_array_with_given_sum(arr1, m, 58))
