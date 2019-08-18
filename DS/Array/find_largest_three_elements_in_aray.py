from sys import maxsize


def largest_three_elements(arr, n):
    if len(arr) < 3:
        print("Invalid Input\n")
        return
    third = second = first = -maxsize
    for i in range(n):
        if arr[i] > first:
            third = second
            second = first
            first = arr[i]
        elif arr[i] > second:
            third = second
            second = arr[i]
        elif arr[i] > third:
            third = arr[i]
    print(first, second, third, end=" ")


# Method 2: Using Sorting algorithm
def find3largest_element(arr, n):
    arr.sort()
    for i in range(3):
        print(arr[n - i-1], end=" ")


if __name__ == '__main__':
    arr1 = [12, 13, 1, 10, 34, 1]
    n = len(arr1)
    largest_three_elements(arr1, n)
    print("\n")
    find3largest_element(arr1, n)
