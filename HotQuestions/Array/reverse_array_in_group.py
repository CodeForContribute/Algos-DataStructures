# Time Complexity : O(n)
# Space Complexity: O(1)
def reverse_array_in_group(arr, n, k):
    i = 0
    while i < n:
        left = i
        right = min(i+k-1, n)
        while left < right:
            arr[left], arr[right] = arr[right],arr[left]
            left += 1
            right -= 1
        i += k


def printArray(arr, n):
    for i in range(n):
        print(arr[i], end=" ")


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6]
    k = 2
    n = len(arr)
    printArray(arr, n)
    reverse_array_in_group(arr, n, k)
    print("\n")
    printArray(arr, n)
