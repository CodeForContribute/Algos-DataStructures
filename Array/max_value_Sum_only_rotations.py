def maxSum(arr, n):
    sum_arr_sum = 0
    currentVal = 0
    for i in range(n):
        sum_arr_sum += arr[i]
        currentVal += i * arr[i]
    max_val = currentVal
    for j in range(1, n):
        currentVal = currentVal + sum_arr_sum - n * arr[n - j]
        if currentVal > max_val:
            max_val = currentVal
    return max_val


if __name__ == '__main__':
    arr = [10, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    n = len(arr)
    print(maxSum(arr, n))
