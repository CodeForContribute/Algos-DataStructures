def subarraySum(arr, n, sum):
    curr_sum = arr[0]
    start = 0
    i=1
    while i <= n:
        while curr_sum > sum and start < i-1:
            curr_sum = curr_sum - arr[start]
            start += 1
        if curr_sum == sum:
            print(start, i-1)
        if i < n:
            curr_sum = curr_sum + arr[i]
        i += 1
    return -1

if __name__ == '__main__':
    arr = [15, 2, 4, 8, 9, 5, 10, 23]
    n = len(arr)
    sum = 23
    subarraySum(arr, n, 23)