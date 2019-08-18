"""
Time Complexity: O(n^2)
space Complexity:O(1)
"""


def next_greater_element(arr, n):
    for i in range(n):
        next = -1
        for j in range(i + 1, n):
            if arr[j] > arr[i]:
                next = arr[j]
                break
        print(str(arr[i]) + "-->" + str(next))


def nge_using_stack(arr, n):
    stack = []
    next_greater = -1
    stack.append(arr[0])
    for j in range(1, n):
        element = stack.pop()
        if arr[j] > element:
            next_greater = arr[j]
            # break
            print(str(element) + "-->" + str(next))
        elif arr[j] < element:
            stack.append(element)
        stack.append(arr[j])
    while len(stack) != 0:
        element = stack.pop()
        next_greater = -1
        print(str(element) + "-->" + str(next_greater))


if __name__ == '__main__':
    arr = [11, 13, 21, 3]
    n = len(arr)
    # next_greater_element(arr, n)
    nge_using_stack(arr, n)
