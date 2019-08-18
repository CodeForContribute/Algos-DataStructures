def fill_next(next_arr, arr, n):
    stack = list()
    stack.append(0)
    for i in range(1, n):
        while len(stack) != 0:
            current = stack.pop()
            if arr[current] < arr[i]:
                next_arr[current] = i
            else:
                break
        stack.append(i)
    while len(stack) != 0:
        current = stack.pop()
        next_arr[current] = -1
    return next_arr


def count(arr, n, index):
    next_arr = [0]*n
    dp = [0]*n
    next_array = fill_next(next_arr, arr, n)
    for i in range(len(next_array)):
        print(next_array[i], end=" ")
    n = len(next_array)
    next_array.reverse()
    print("\n")
    for i in range(len(next_array)):
        print(next_array[i], end=" ")
    for i in range(n-1):
        if next_array[i] == -1:
            dp[i] = 0
        else:
            dp[i] = 1 + dp[next_array[i]]

    return dp[index]


if __name__ == '__main__':
    arr = [3, 4, 2, 7, 5, 8, 10, 6]
    n = len(arr)
    # print("\n")
    print(count(arr, n, 3))
