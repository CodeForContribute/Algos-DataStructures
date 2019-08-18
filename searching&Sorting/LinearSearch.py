"""
Time Complexity of Linear Search is O(n), so practically rarely used
"""


def linear_search(arr, n, x):
    for i in range(n):
        if arr[i] == x:
            return i

    return -1


if __name__ == '__main__':
    arr = [12, 3, 5, 6]
    n = len(arr)
    x = 6
    print(linear_search(arr, n, x))
