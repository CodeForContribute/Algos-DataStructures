"""
Time Complexity: If elements are uniformly distributed, then O (log log n)). In worst case it can take upto O(n).
Auxiliary Space: O(1)
The Interpolation Search is an improvement over Binary Search for instances, where the values in a sorted array are
uniformly distributed. Binary Search always goes to the middle element to check. On the other hand, interpolation search
may go to different locations according to the value of the key being searched.
For example, if the value of the key is closer to the last element, interpolation search is likely to start search
toward the end side.
"""


def interpolation_search(arr, n, x):
    left = 0
    right = n - 1
    while left <= right and arr[left] <= x <= arr[right]:
        if left == right:
            if arr[left] == x:
                return left
            return -1
        position = left + int(((x - arr[left]) * (right - left) / (arr[right] - arr[left])))
        if arr[position] == x:
            return position
        elif arr[position] > x:
            right = position - 1
        elif arr[position] < x:
            left = position + 1
    return -1


if __name__ == '__main__':
    arr = [0, 1, 1, 2, 3, 5, 8, 13, 21,
           34, 55, 89, 144, 233, 377, 610]
    x = 55
    n = len(arr)
    print(interpolation_search(arr, n, 55))
